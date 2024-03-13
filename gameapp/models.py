from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg
from django.core.validators import MaxValueValidator, MinValueValidator
from taggit.managers import TaggableManager

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
class Platform(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Game(models.Model):
    name = models.CharField(max_length=255,default='')
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(default='')
    release_date = models.DateField()
    cover_img = models.ImageField(upload_to='cover/', default="media/temp-image.jpg")
    header_img = models.ImageField(upload_to='header/', default="media/temp-image.jpg")
    likes = models.IntegerField(default=0)
    plays = models.IntegerField(default=0)
    publisher = models.ManyToManyField(Publisher, related_name='game_pub')
    tags = TaggableManager()
    platforms = models.ManyToManyField(Platform, related_name='games_plat')

    def adv_rating(self) -> float:
        return Review.objects.filter(game=self).exclude(0).aggregate(Avg('rating'))['avg_rating']
    def __str__(self):
        return self.name


class Review(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_reviews')
    title = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    rating = models.PositiveSmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    heart = models.BooleanField(default=False)

    def __str__(self):
        return self.user
