from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import transaction
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from data_collections.collectors.people_collector import PeopleDataCollector
from data_collections.collectors.worlds_collector import WorldsDataCollector
from people.models import Person


def index(request):
    people_qs = Person.objects.all().order_by('-created_at')

    paginator = Paginator(people_qs, 25)
    page = request.GET.get('page')

    try:
        people = paginator.page(page)
    except PageNotAnInteger:
        people = paginator.page(1)
    except EmptyPage:
        people = paginator.page(paginator.num_pages)

    data = {
        'people': people,
    }
    return render(request, 'people/index.html', data)


@require_POST
def save_people(request):
    people_collector = PeopleDataCollector().collect()
    worlds_collector = WorldsDataCollector().collect()

    with transaction.atomic():
        Person.create_from_fetched_data(
            people_collector.results, worlds_collector.get_url_name_dict())
        messages.success(request, 'Successfully created Person records')
    return redirect('people:index')
