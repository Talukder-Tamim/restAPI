from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    

    def __str__(self):
        return self.name


class Framework(models.Model):
    name = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return self.name 


