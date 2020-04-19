from django.db import models

class WhatToDo(models.Model):
    title = models.TextField(max_length=200)
    image = models.ImageField(upload_to='images/')


    def __str__(self):
        return self.title

