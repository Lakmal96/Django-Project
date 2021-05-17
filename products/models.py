from django.db import models
from django.db.models.signals import pre_save
from .utils import unique_slug_generator
from django.urls import reverse

from tags.models import Tag

# Create your models here.


class ItemManager(models.Manager):
    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)  # Item.objects == self.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None


class Item(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=15, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    quantity = models.IntegerField()
    tags = models.ManyToManyField(Tag, blank=True)

    objects = ItemManager()

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
