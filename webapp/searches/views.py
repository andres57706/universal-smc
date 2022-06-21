from django.shortcuts import render, redirect

# Create your views here.
from searches.models import Search


def index(request):
    s_list = Search.objects.all()
    return render(request, 'index/show.html', context={'items': s_list})


def search(request):
    return render(request, 'results/show.html',
                  context={'status': 200, 'message': f'your message: {request.POST["query-item"]}'})


def create(request):
    if request.POST:
        new_search = Search(
            keywords=request.POST["query-item"],
            customer_ip="0.0.0.0")
        new_search.save()
        # breakpoint()
        return redirect(to="searches:index")