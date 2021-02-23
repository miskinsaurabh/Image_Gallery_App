from django.db import models

# model of different categories.
class Category(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    def __str__(self):
        return self.name

# model for different images going to store.
class Image(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    img = models.ImageField(null=False, blank=False)
    
    