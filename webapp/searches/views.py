from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index/show.html')

def search(request):
    return render(request, 'results/show.html', context={'status': 200, 'message': f'your message: {request.POST["query-item"]}'})