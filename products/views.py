from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . import views

from . models import Item

# Create your views here.


class ItemListView(ListView):
    queryset = Item.objects.all()
    template_name = "products/item_list.html"

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     return Item.objects.all()


def item_detail(request, slug):
    item = Item.objects.get(slug=slug)
    item.view_count += 1
    item.save()
    return render(request, 'products/item_details.html', {'item': item})


# class ItemDetailView(DetailView):
#     queryset = Item.objects.all()
#     template_name = "products/item_details.html"

    # def get_object(self, *args, **kwargs):
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #     instance = Item.objects.get_by_id(pk)
    #     if instance is None:
    #         raise Http404("Item doesn't exists")
    #     return instance

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #     return Item.objects.filter(pk=pk)
