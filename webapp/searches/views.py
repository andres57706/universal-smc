from django.shortcuts import render

# Create your views here.
from searches.models import Search


def index(request):
    s_list = Search.objects.all()
    return render(request, 'index/show.html', context={'items': s_list})


def search(request):
    return render(request, 'results/show.html',
                  context={'status': 200, 'message': f'your message: {request.POST["query-item"]}'})
