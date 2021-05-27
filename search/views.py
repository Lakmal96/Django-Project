from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView

from products.models import Item

# Create your views here.


class SearchItemView(ListView):
    #queryset = Item.objects.all()
    template_name = "search/view.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        query = request.GET.get('q')
        if query is not None:
            lookups = Q(name__icontains=query) | Q(
                description__icontains=query) | Q(tags__name__icontains=query)
            return Item.objects.filter(lookups).distinct()
        return Item.objects.none()
