import csv
from typing import Dict, Any

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    ## form a list of data from csv file
    databank = open('data-bus-stations.csv', 'r', encoding='UTF-8')
    csv_block = csv.DictReader(databank)
    rows = list(csv_block)
    databank.close()
    ## create pagination
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(rows, 10)
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': page,
        'page': page
    }
    return render(request, 'stations/index.html', context)
