from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from .models import Menu


def main(request: HttpRequest) -> HttpResponse:
    context = {'menu': Menu.objects.all()}

    return render(request, 'app/main.html', context)


def draw_menu(request: HttpRequest, path: str) -> HttpResponse:
    path = path.split('/')
    assert len(path) > 0, '! path is not correct !'
    context = {'menu_name': path[0], 'menu_item': path[-1]}
    
    return render(request, 'app/main.html', context)
