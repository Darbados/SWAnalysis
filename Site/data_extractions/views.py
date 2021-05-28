import csv
import io

from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from characters.data_collector import CharactersDataCollector
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


@require_POST
def fetch_collection_data(request):
    collector = CharactersDataCollector()
    collector.collect()

    DataExport.create_from_fetched_data(collector.results)
    messages.success(request, 'People collection was saved successfully.')
    return redirect('data_extractions:exports')
