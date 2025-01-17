from django.db import models

# Create your models here.
class CartItem(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    item = models.ForeignKey('marketplace.Item', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.quantity} of {self.item.name}"