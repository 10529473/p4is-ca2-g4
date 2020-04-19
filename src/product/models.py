from django.db import models
from django.core.exceptions import ObjectDoesNotExist


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
        category_tree = []
        topLevel = Category.objects.all().order_by('-level').first().level

        Category.objects.filter(level=topLevel)


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

class Cart(models.Model):
    productList = []
    
    def addProduct(self,product = Product):
        self.productList.append(product)
