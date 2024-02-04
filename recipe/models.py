from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


#User Model
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
    

#Profile Model
class UserProfile(models.Model):
    name = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    bio = models.TextField()
    picture = models.ImageField(upload_to='profile_pictures', blank=True, null=True)
    def __str__(self):
        return self.name.username


#Recipe Model
class Recipe(models.Model):
    DIFFICULTY_CHOICES = (
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('difficult', 'Difficult'),
    )
    CATEGORY_CHOICES = (
        ('main course', 'Main Course'),
        ('snaks', 'Snaks'),
        ('deserts', 'Deserts'),
    )
    title = models.CharField(max_length=250)
    description = models.TextField()
    ingredients = models.ManyToManyField('Ingredient')
    instructions = models.TextField()
    cooking_time = models.PositiveIntegerField()
    difficulty_level = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='authored_recipes')
    Category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    favorited_by = models.ManyToManyField(CustomUser, related_name='favorite_recipes')

    def __str__(self):
        return self.title
    

    
#ingredient Model
class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    


#Rating Model    
class Rating(models.Model):
    RATING_CHOICES = (
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    def __str__(self):
        return self.user.username
    

    

    




    

    