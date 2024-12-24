from django.db import models

class iPhone(models.Model):
    color_choices = [
        ("Nero", "Nero"),
        ("Bianco", "Bianco"),
        ("Oro", "Oro"),
        ("Blu", "Blu"),
        ("Verde", "Verde"),
        ("Rosso", "Rosso"),
        ("Giallo", "Giallo"),
    ]

    space_choices = [
        (64, 64),
        (128, 128),
        (256, 256),
        (512, 512),
        (1024, 1024),
    ]

    display_choices = [
        (6.1, 6.1),
        (6.7, 6.7),
    ]

    name = models.CharField(max_length=100)
    price = models.IntegerField()
    color = models.CharField(max_length=50,choices=color_choices, default='Nero') 
    space = models.IntegerField(choices=space_choices, default=64)
    display = models.FloatField(choices=display_choices, default=6.1)

    def __str__(self):
        return f"{self.name} - {self.price} - {self.color} - {self.space} - {self.display}"
