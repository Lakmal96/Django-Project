from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from . import views

from products.models import Item, Category
# Create your views here.


class CategoryList(ListView):
    queryset = Category.objects.all()
    template_name = 'categories/category_list.html'


def CategoryView(request, cat_id):
    category = Category.objects.get(id=cat_id)
    items = Item.objects.filter(category=category)
    return render(request, 'categories/category_list_view.html', {'items': items})


# class CategoryListView(ListView):
#     queryset = Item.objects.all()
#     # queryset = Category.objects.all()
#     template_name = 'categories/category_list_view.html'

#     def get_queryset(self, *args, **kwargs):
#         categories = Category.objects.all()
#         return categories

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['items'] = Item.objects.all()
#         return context

# def CategoryView(request, category_slug=None):
#     category = None
#     categories = Category.objects.all()
#     items = Item.objects.all()

#     if category_slug:
#         category = get_object_or_404(Category, slug=category_slug)
#         items = items.filter(category=category)

#     return render(request, 'categories/category_list_view.html', {'category_slug': category_slug, 'category': category, 'items': items})
