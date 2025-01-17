from django.db import models

# Create your models here.
class HealthTip(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.CharField(max_length=50, choices=[('Recipe', 'Recipe'), ('Diet', 'Diet'), ("Meditation", 'Meditation')])


    def __str__(self):
        return self.title