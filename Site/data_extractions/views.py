from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

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

