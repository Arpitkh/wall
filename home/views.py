from django.shortcuts import render, get_object_or_404
from .models import Item


def index(request):
    all_items = Item.objects.all()
    return render(request, 'home/index.html', {'reqd_items': all_items})


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'home/detail.html', {'item': item})


def search(request):
    all_items = list(Item.objects.all())
    searched_item = request.POST.get('textfield')
    searched_item_words = searched_item.split()
    var = []
    for item in all_items:
        count = 0
        item_name = item.item_name
        for char in item_name:
            if char in "():,+":
                item_name = item_name.replace(char, '')
        temp = item_name.split()

        for word in temp:
            for sword in searched_item_words:
                if word.lower() == sword.lower():
                    count += 1
        var.append(count)
        for i in range(len(var)):
            for j in range(0, len(var)-i-1):
                if var[j] > var[j + 1]:
                    var[j], var[j + 1] = var[j + 1], var[j]
                    all_items[j], all_items[j + 1] = all_items[j + 1], all_items[j]

    var.reverse()
    all_items.reverse()

    for i in range(len(var)):
        if var[i] is 0:
            del var[i:]
            del all_items[i:]
            break

    return render(request, 'home/index.html', {'reqd_items': all_items})
