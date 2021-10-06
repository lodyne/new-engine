from django.db import models

# Create your models here.
Grade = [
    ('EXCELENT',1),
    ('AVERAGE',0),
    ('BAD',-1)
]

class Post(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    uploaded = models.DateTimeField(auto_now_add=True)
    rating = models.CharField(choices=Grade, default='AVERAGE', max_length=50)

    class Meta:
        ordering = ['uploaded']

    def __str__(self):
        return self.name