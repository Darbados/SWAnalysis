import petl
import sendfile
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import transaction
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from people.models import Person
from data_collections.collectors.people_collector import PeopleDataCollector
from data_collections.collectors.worlds_collector import WorldsDataCollector
from data_collections.forms import ValueCountsForm
from data_collections.models import DataCollection
from data_collections.transformers.character_transformer import PeopleDataTransformer
from data_collections.utils import get_rows_to_display


def index(request):
    collections_qs = DataCollection.objects.filter(
        collection_type=DataCollection.COLLECTION_PEOPLE)
    paginator = Paginator(collections_qs, 25)
    page = request.GET.get('page')

    try:
        collections = paginator.page(page)
    except PageNotAnInteger:
        collections = paginator.page(1)
    except EmptyPage:
        collections = paginator.page(paginator.num_pages)

    data = {
        'collections': collections,
    }
    return render(request, 'data_collections/collections.html', data)


def download(request, collection_id):
    try:
        collection = DataCollection.objects.get(id=collection_id)
    except DataCollection.DoesNotExist:
        messages.error(request, 'Requested collection does not exist anymore.')
        return redirect('data_collections:index')

    return sendfile.sendfile(
        request,
        collection.file.path,
        attachment=True,
        attachment_filename=collection.collection_file_name,
    )


def inspect(request, collection_id):
    try:
        collection = DataCollection.objects.get(id=collection_id)
    except DataCollection.DoesNotExist:
        messages.error(request, 'Requested collection does not exist anymore.')
        return redirect('data_collections:index')

    de_table = petl.fromcsv(collection.file.path, encoding='utf-8')
    rows_multiplier = int(request.GET.get('multiplier', 1))
    rows_to_display = get_rows_to_display(de_table, rows_multiplier)

    data = {
        'collection': collection,
        'Character': Person,
        'multiplier': rows_multiplier + 1,
        'table_header': petl.header(de_table),
        'rows_to_display': rows_to_display,
    }
    return render(request, 'data_collections/inspect.html', data)


def collection_value_counts(request, collection_id):
    try:
        collection = DataCollection.objects.get(id=collection_id)
    except DataCollection.DoesNotExist:
        messages.error(request, 'Requested collection does not exist anymore.')
        return redirect('data_collections:index')

    de_table = petl.fromcsv(collection.file.path, encoding='utf-8')
    counts_form = ValueCountsForm(request.GET or None, header_fields=petl.header(de_table))
    value_counts = counts_form.get_changed_fields()
    value_counts_data = []
    if value_counts:
        # Remove the frequency column from the end data result
        value_counts_data = petl.cutout(petl.valuecounts(de_table, *value_counts), 'frequency')

    data = {
        'counts_form': counts_form,
        'de_table': de_table,
        'collection': collection,
        'value_counts_data': value_counts_data,
    }
    return render(request, 'data_collections/value_counts.html', data)


@require_POST
@transaction.atomic
def resolve(request, collection_id):
    try:
        collection = DataCollection.objects.select_for_update().get(id=collection_id)
    except DataCollection.DoesNotExist:
        messages.error(request, 'Requested collection does not exist anymore.')
        return redirect('data_collections:index')

    if collection.resolved_at:
        messages.error(request, f'Collection {collection.collection_file_name} is already resolved')
        return redirect('data_collections:index')

    collection.resolve()
    messages.success(request, f'Collection {collection.collection_file_name} is marked as resolved')
    return redirect('data_collections:index')


@require_POST
def delete(request, collection_id):
    try:
        export = DataCollection.objects.get(id=collection_id)
    except DataCollection.DoesNotExist:
        messages.error(request, 'Requested collection does not exist anymore.')
        return redirect('data_collections:index')

    export.delete()
    messages.success(request, f'Collection {collection_id} has been deleted')
    return redirect('data_collections:index')


@require_POST
def save_collection_data(request):
    """
    Normally I won't implement such view for production, as making requests usually should be
    placed in async tasks without making the user to wait for them within the initial request.
    """

    # This view could be easily extended to export data based on user choice.
    people_collector = PeopleDataCollector().collect()

    # Obtain planets data needed for homeworld transformation
    worlds_collector = WorldsDataCollector().collect()
    worlds_data = worlds_collector.get_url_name_dict()

    people_transformer = PeopleDataTransformer(people_collector.results)
    people_transformer.transform_data(worlds_data=worlds_data)

    with transaction.atomic():
        DataCollection.create_from_fetched_data(people_transformer.data)
        messages.success(request, 'People collection is saved successfully.')
    return redirect('data_collections:index')
