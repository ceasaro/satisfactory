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
    def factory(self):
        return Factory.objects.get(produced_products__product=self)

    @property
    def resources(self):
        requires = set()
        for product in self.factory.requires:
            requires.add(product)
            requires = set.union(requires, product.resources)
        return requires

    @property
    def required_base_products(self):
        base_products = set()
        for product in self.factory.requires:
            if product.is_base_resource:
                base_products.add(product)
            else:
                base_products = set.union(base_products, product.required_base_products)
        return base_products

    @property
    def is_base_resource(self):
        return Factory.objects.filter(produced_products__product=self, resources__isnull=True).exists()

    @classmethod
    def get_or_create_product(cls, name, code, produced_amount, resources=None):
        product, created = cls.objects.get_or_create(code=code, defaults={'name': name})
        if not created:
            factory = product.factory
            # delete previous set resources
            factory.resources.all().delete()
            # delete previous set produced products
            factory.produced_products.all().delete()
        else:
            factory = Factory.objects.create()

        for resource_code, amount in resources or []:
            factory.add_resource(resource=Product.objects.get(code=resource_code), amount=amount)
        factory.add_product(product=product, amount=produced_amount)
        return product

    def get_produced(self):
        return self.factory.produced_products.get(product=self)

    def __str__(self):
        return f"{self.name} ({self.code})"


class Construction(BaseModel):
    class Meta:
        abstract = True
    name = models.CharField(max_length=255)


class Factory(Construction):

    @property
    def produces(self):
        return Product.objects.filter(produced_by__factory=self)

    @property
    def requires(self):
        return Product.objects.filter(used_by__factory=self)

    def add_product(self, product, amount, production_time=timedelta(minutes=1)):
        ProducedProduct.objects.create(product=product, factory=self, amount=amount, production_time=production_time)

    def add_resource(self, resource, amount, production_time=timedelta(minutes=1)):
        Resource.objects.create(resource=resource, factory=self, amount=amount, process_time=production_time)

    def resources(self):
        pass

    def __str__(self):
        return f"Factory of '{', '.join([str(p) for p in self.produces])}'"


class ProducedProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='produced_by')
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE, related_name='produced_products')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    production_time = models.DurationField()


class Resource(models.Model):
    resource = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='used_by')
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE, related_name='resources')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    process_time = models.DurationField()
