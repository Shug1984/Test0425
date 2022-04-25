from django.shortcuts import render

from .models import Items


def item_list(request):
    items = Items.objects.all()
    return render(request, 'store/item_list.html', context={'items':items})


def item_detail(request, id):
    item = Items.objects.filter(pk=id).first()
    return render(request, 'store/item_detail.html', context={'item':item})
