from django.db import models

# Create your models here.
class Order(models.Model):
    PENDING = 'Pending'
    DELIVERED = 'Delivered'
    CANCELLED =  'Cancelled'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (DELIVERED, 'Delivered'),
        (CANCELLED, 'Cancelled'),
    ]


    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    recurring = models.CharField(max_length=50, choices=[('Bi-weekly', 'Bi-weekly'), ('Monthly', 'Monthly')], blank=True)

    def __str__(self):
        return f"Order by {self.user.username}"
    


class OrderItem(models.Model):
        order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
        item = models.ForeignKey("marketplace.Item",  on_delete=models.CASCADE)
        quantity = models.PositiveIntegerField()
    