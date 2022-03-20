from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    if request.method == 'POST':
        return HttpResponse(request.POST['item_text'])
    return render(request, 'todo/home_page.html')
