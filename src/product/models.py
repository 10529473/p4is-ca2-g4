from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers
import json


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    level = models.SmallIntegerField(verbose_name='Level',default=1)
    subcategories = models.ManyToManyField('self',verbose_name="Subcategories",blank=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

    def getParentCategories(self):
        parents=[]
        for obj in Category.objects.filter(level__gt=self.level):
            try:
                obj.subcategories.get(pk=self.pk)
                parents.append(obj)
            except ObjectDoesNotExist:
                pass
        return parents

    def getTree():
        json_data = serializers.serialize("json", Category.objects.all())
        data = {i['pk']:i['fields'] for i in json.loads(json_data)}
        category_tree = []
        for k,v in data.items():
            v['subcategories']=[data[subcategory] for subcategory in v['subcategories']]
            v['id']=k
            if v['level']==1:
                category_tree.append(v)
        return category_tree
                

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    size = models.CharField(max_length=1)
    price = models.FloatField()
    picture = models.ImageField(upload_to='products/', null=False, blank=False)
    category = models.ManyToManyField(Category, verbose_name="Category")

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.title

    def categoryBreadcrumbs(self):
        return ' > '.join(
            self.category.all().order_by('-level').values_list('title',flat=True))