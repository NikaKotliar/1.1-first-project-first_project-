import csv
import os

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

from pagination.settings import BASE_DIR


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
        # получите текущую страницу и передайте ее в контекст
    file_path = os.path.join(BASE_DIR, 'data-398-2018-08-30.csv')
    with open(file_path, encoding='utf-8', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        bus_stations = []
        for row in reader:
            bus_station = {}
            bus_station['Name'] = row['Name']
            bus_station['Street'] = row['Street']
            bus_station['District'] = row['District']
            bus_stations.append(bus_station)

        paginator = Paginator(bus_stations, 10)
        page_number = int(request.GET.get('page', 1))
        page = paginator.get_page(page_number)

    # также передайте в контекст список станций на странице

        context = {
            'bus_stations': bus_stations,
            'page': page
            #     'bus_stations': ...,
            #     'page': ...,
        }
        return render(request, 'stations/index.html', context)
