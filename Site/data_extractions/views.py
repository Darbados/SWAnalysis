import sendfile
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from data_extractions.collectors.characters_collector import CharactersDataCollector
from data_extractions.models import DataExport


def exports(request):
    extractions_qs = DataExport.objects.filter(
        collection_type=DataExport.COLLECTION_CHARACTERS,
    ).order_by('-created_at')
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
    export = get_object_or_404(DataExport, id=export_id)

    return sendfile.sendfile(
        request,
        export.export.path,
        attachment=True,
        attachment_filename=export.export_name,
    )


@require_POST
def export_collection_data(request):
    # This view could be easily extended to export data based on user choice.
    collector = CharactersDataCollector()
    collector.collect()

    with transaction.atomic():
        DataExport.create_from_fetched_data(collector.results)
    messages.success(request, 'People collection is saved successfully.')
    return redirect('data_extractions:exports')
