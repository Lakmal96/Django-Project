from django.db import models

# Create your models here.


# class CategoryManager(models.Manager):
#     def get_by_id(self, id):
#         qs = self.get_queryset().filter(id=id)
#         if qs.count() == 1:
#             return qs.first()
#         return None


class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(unique=True, null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='catogories/', null=True)

    # objects = CategoryManager()

    def get_absolute_url(self):
        return "/category/{id}/".format(id=self.id)

    def __str__(self):
        return self.name
