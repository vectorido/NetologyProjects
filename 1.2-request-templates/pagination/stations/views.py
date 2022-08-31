import csv
from typing import Dict, Any

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    databank = open('data-bus-stations.csv', 'r', encoding='UTF-8')
    csv_block = csv.DictReader(databank)
    rows = list(csv_block)
    table = []
    for row in rows:
        my_dict = {}
        for column in row:
            my_dict[column] = row[column]
        table.append(my_dict)
    databank.close()
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(table, 10)
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': page,
        'page': page
    }
    return render(request, 'stations/index.html', context)
