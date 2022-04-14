from django.db import models

LABELS = (
    ('NEW', 'New'),
    ('BEST', 'BEST'),
    ('RECENT', "Recent"),
)


class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    post_image = models.ImageField(upload_to='post', blank=True)
    labels = models.CharField(choices=LABELS, max_length=6, default='RECENT')

    def __str__(self):
        return self.title
