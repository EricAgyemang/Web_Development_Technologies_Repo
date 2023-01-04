from django.shortcuts import render
from django.views import generic
from items.models import Item
from django.http import HttpResponse


# Create your views here.

class ItemList(generic.ListView):
    template_name = 'items/itemlist.html'
    context_object_name = 'item_list'
    model = Item

    def post(self, request, *args, **kwargs):
        Item.objects.create(text=request.POST["text"])
        return HttpResponse("Success!")
 

