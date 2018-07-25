from django.shortcuts import render,get_object_or_404
from .models import Item
from wall.settings import BASE_DIR


def index(request):
    print("wassups")
    all_items = Item.objects.all()
    print(BASE_DIR)
    return render(request, 'home/index.html', {'all_items': all_items})


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'home/detail.html', {'item': item})

