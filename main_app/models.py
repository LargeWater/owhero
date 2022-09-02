from django.db import models


class Hero(models.Model):
  name = models.CharField(max_length=20)
  role = models.CharField(max_length=8)
  rating = models.IntegerField()
  description = models.CharField(max_length=500)
  weapon = models.CharField(max_length=50)
  abilties = models.CharField(max_length=200)
  background = models.CharField(max_length=200)
  portrait = models.CharField(max_length=200)

  def __str__(self):
    return self.name


# class Hero(models.Model):
#   def __init__(self, name, role, rating, description, weapon, abilities, background, portrait):
#     self.name = name
#     self.role = role
#     self.rating = rating
#     self.description = description
#     self.weapon = weapon
#     self.abilities = abilities
#     self.background = background
#     self.portrait = portrait




