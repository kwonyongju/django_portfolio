from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length = 100)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = 'images/', blank=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:208]

    def format_date(self):
        return self.pub_date.strftime("%Y-%m-%d")
