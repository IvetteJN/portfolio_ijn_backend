from django.db import models

class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
    description = models.TextField()
    more_info = models.TextField()

    def __str__(self):
        return self.title

class Education(models.Model):
    certificate_image = models.ImageField(upload_to='education_certificates')

    def __str__(self):
        return f"Education Certificate {self.id}"