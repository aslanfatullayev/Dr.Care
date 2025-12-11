from django.db import models
from django.utils.text import slugify
from django.utils import timezone

class News(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    slug = models.TextField(null=True, blank=True)
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    
    def save(self, **kwargs):
        self.slug = slugify(self.title)
        super().save(**kwargs)

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"