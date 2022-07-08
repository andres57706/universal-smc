from django.shortcuts import render, redirect

from .decorators.fetch_request_ipaddress import fetch_request_ipaddress

# Create your views here.
from .models import Search


def index(request):
    s_list = Search.objects.all()
    return render(request, 'index/show.html', context={'items': s_list})


def search(request):
    return render(request, 'results/show.html',
                  context={'status': 200, 'message': f'your message: {request.POST["query-item"]}'})


@fetch_request_ipaddress
def create(request):
    if request.POST:
        new_search = Search(
            keywords=request.POST["query-item"],
            customer_ip=request.ip_address)
        new_search.save()
        return redirect(to="searches:index")
