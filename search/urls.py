from django.urls import path
from .views import SearchItemView

urlpatterns = [
    path('', SearchItemView.as_view(), name="query"),
]
