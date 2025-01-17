from django.db import models

# Create your models here.
class dolls(models.Model):
    title = models.CharField(max_length=55)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default='bird.png',blank=True)

    def __str__(self):
        return self.title
