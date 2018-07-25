from django.shortcuts import render,get_object_or_404
from .models import Item


def index(request):
    all_items = Item.objects.all()
    return render(request, 'home/index.html', {'all_items': all_items})


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'home/detail.html', {'item': item})

def search(request):
    searched_item = request.POST.get('textfield')
    return render(request, 'home/index.html')








