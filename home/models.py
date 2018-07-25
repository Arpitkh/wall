from django.db import models



class Item(models.Model):
    item_name = models.CharField(max_length=250)
    company = models.CharField(max_length=250)
    item_price = models.CharField(max_length=10)
    item_details = models.CharField(max_length=3000)
    item_img = models.FileField()

    def __str__(self):
        return self.item_name


