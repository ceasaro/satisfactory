from datetime import timedelta

from django.db import models


# Create your models here.
class BaseModel(models.Model):
    class Meta:
        abstract = True
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


class BaseCodeModel(BaseModel):
    class Meta:
        abstract = True
    code = models.CharField(unique=True, max_length=32)


class Product(BaseCodeModel):
    name = models.CharField(max_length=255)

    @property
    def is_base_resource(self):
        return Factory.objects.filter(produced_products__product=self, resources__isnull=True).exists()

    def __str__(self):
        return f"{self.name} ({self.code})"


class Construction(BaseModel):
    class Meta:
        abstract = True
    name = models.CharField(max_length=255)


class Factory(Construction):

    def __str__(self):
        return f"Factory of '{', '.join([str(p) for p in self.produces])}'"

    @property
    def produces(self):
        return [p.product for p in self.produced_products.all()]

    @property
    def requires(self):
        return [r.resource for r in self.resources.all()]

    def add_product(self, product, amount, production_time=timedelta(minutes=1)):
        ProducedProducts.objects.create(product=product, factory=self, amount=amount, production_time=production_time)

    def add_resource(self, resource, amount, production_time=timedelta(minutes=1)):
        Resource.objects.create(resource=resource, factory=self, amount=amount, process_time=production_time)

    def resources(self):
        pass


class ProducedProducts(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='produced')
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE, related_name='produced_products')
    amount = models.IntegerField()
    production_time = models.DurationField()


class Resource(models.Model):
    resource = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='used_by')
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE, related_name='resources')
    amount = models.IntegerField()
    process_time = models.DurationField()
