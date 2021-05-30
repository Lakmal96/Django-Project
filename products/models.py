from django.db import models
from django.db.models.signals import pre_save
from .utils import unique_slug_generator
from django.urls import reverse

from tags.models import Tag
from catogories.models import Category

# Create your models here.


# class ItemManager(models.Manager):
#     def get_by_id(self, id):
#         qs = self.get_queryset().filter(id=id)  # Item.objects == self.get_queryset()
#         if qs.count() == 1:
#             return qs.first()
#         return None


class Item(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(blank=True, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    features = models.CharField(max_length=200, null=True)
    marked_price = models.DecimalField(
        max_digits=15, decimal_places=2, default=0.00)
    selling_price = models.DecimalField(
        max_digits=15, decimal_places=2, default=0.00)
    tags = models.ManyToManyField(Tag, blank=True)
    view_count = models.IntegerField(default=0)

    # objects = ItemManager()

    def get_absolute_url(self):
        return "/products/{slug}/".format(slug=self.slug)
        # when we use reverse
        # return reverse("detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.name


def item_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(item_pre_save_receiver, sender=Item)
