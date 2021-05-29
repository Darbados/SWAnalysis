import sendfile
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from characters.models import Character
from data_extractions.collectors.characters_collector import CharactersDataCollector
from data_extractions.collectors.worlds_collector import WorldsDataCollector
from data_extractions.models import DataExport


def exports(request):
    extractions_qs = DataExport.objects.filter(collection_type=DataExport.COLLECTION_CHARACTERS)
    paginator = Paginator(extractions_qs, 25)
    page = request.GET.get('page')

    try:
        extractions = paginator.page(page)
    except PageNotAnInteger:
        extractions = paginator.page(1)
    except EmptyPage:
        extractions = paginator.page(paginator.num_pages)

    data = {
        'extractions': extractions,
    }
    return render(request, 'data_extractions/extractions.html', data)


def export_download(request, export_id):
    try:
        export = DataExport.objects.get(id=export_id)
    except DataExport.DoesNotExist:
        messages.error(request, 'Requested export does not exist anymore.')
        return redirect('data_extractions:exports')

    return sendfile.sendfile(
        request,
        export.export.path,
        attachment=True,
        attachment_filename=export.export_name,
    )


def export_inspect(request, export_id):
    # Move that code into decorator
    try:
        export = DataExport.objects.get(id=export_id)
    except DataExport.DoesNotExist:
        messages.error(request, 'Requested export does not exist anymore.')
        return redirect('data_extractions:exports')

    rows_multiplier = int(request.GET.get('multiplier', 1))

    rows_to_display = export.get_rows_to_display(rows_multiplier)

    data = {
        'export': export,
        'Character': Character,
        'multiplier': rows_multiplier + 1,
        'rows_to_display': rows_to_display,
    }
    return render(request, 'data_extractions/inspect.html', data)


@require_POST
def save_collection_data(request):
    # This view could be easily extended to export data based on user choice.
    character_collector = CharactersDataCollector()
    character_collector.collect()

    # Obtain planets data
    worlds_collector = WorldsDataCollector()
    worlds_collector.collect()

    with transaction.atomic():
        DataExport.create_from_fetched_data(
            character_collector.results, worlds_collector.get_url_name_dict())
        messages.success(request, 'People collection is saved successfully.')
    return redirect('data_extractions:exports')
