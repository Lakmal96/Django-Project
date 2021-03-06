from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView

from products.models import Item

# Create your views here.


class SearchItemView(ListView):
    template_name = "search/view.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        query = request.GET.get('q')
        if query is not None:
            lookups = Q(name__icontains=query) | Q(
<<<<<<< HEAD
                description__icontains=query) | Q(selling_price__icontains=query) | Q(tags__name__icontains=query)
=======
                description__icontains=query) | Q(tags__name__icontains=query)
>>>>>>> e3e133833a4b7782be97c8884b89e5fab0d26d75
            return Item.objects.filter(lookups).distinct()
        return Item.objects.none()
