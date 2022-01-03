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


class Resource(BaseCodeModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} ({self.code})"


class Construction(BaseModel):
    class Meta:
        abstract = True
    name = models.CharField(max_length=255)


class Factory(Construction):
    produces = models.ForeignKey(Resource, on_delete=models.CASCADE)
    amount = models.IntegerField()
    production_time = models.DurationField()

    def __str__(self):
        return f"Factory of '{self.produces}'"

