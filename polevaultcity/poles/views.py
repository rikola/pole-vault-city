from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.shortcuts import get_object_or_404
from django.views import generic

from .models import Pole


class IndexView(generic.ListView):
    model = Pole
    template_name = 'poles/index.html'
    context_object_name = 'pole_list'

    def get_queryset(self):
        '''Return all the poles'''
        return Pole.objects.all()


# TODO: Include a dashboard with pole metric charts.
# def index(request: HttpRequest):
#     pole_list: [Pole] = Pole.objects.all()
#     context = {'pole_list': pole_list}
#     return render(request, 'poles/index.html', context)


def detail(request: HttpRequest, pole_id: int):
    '''Get details about a specific pole by ID'''
    p = get_object_or_404(Pole, pk=pole_id)
    context = {'pole':p}
    return render(request, 'poles/detail.html', context)


def rent(request: HttpRequest, pole_id: int):
    return HttpResponse('Render a rental form for a pole')

