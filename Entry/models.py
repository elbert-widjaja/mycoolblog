from django.db import models
from django.utils import timezone
# Create your models here.
from django.contrib.auth.models import User


class Categories(models.Model):
    category = models.CharField(max_length = 50)
    created_at = models.DateTimeField(timezone.now())
    def __str__(self):
        return self.category
    class Meta:
        verbose_name_plural = 'Categories'

class Posts(models.Model):
    category = models.ForeignKey(Categories, on_delete= models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    post_name = models.CharField(max_length = 50)
    post_description = models.CharField(max_length = 200)
    post_like = models.IntegerField(default = 0)
    created_at = models.DateTimeField(timezone.now())

    def __str__(self):
        return self.post_name
    class Meta:
        verbose_name_plural = 'Posts'

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    comment = models.CharField(max_length = 200)
    is_hidden = models.BooleanField(default = False)
    created_at = models.DateTimeField(timezone.now())

    def __str__(self):
        return self.comment
    class Meta:
        verbose_name_plural = 'Comments'

