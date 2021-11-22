from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Nombre',)

    def __str__(self) -> str:
        return f'{self.name}'


class Meal(models.Model):
    DAY_TIME_CHOICES = [
        ('LN', 'Almuerzo'),
        ('DN', 'Cena'),
        ('DL', 'Almuerzo/Cena'),
    ]
    TAG_CHOICES = [
        ('VG','Vegano'),
        ('VT','Vegetariano'),
        ('OM','Omnívoro'),
        ('CL','Celíaco'),
    ]
    name = models.CharField(max_length=50, verbose_name='Nombre')
    cooking_time = models.CharField(max_length=10, verbose_name='Tiempo de cocción')
    tags = models.CharField(
        max_length=2,
        choices=TAG_CHOICES,
        default='',
        verbose_name='Etiquetas',
    )
    day_time = models.CharField(
        max_length=2,
        choices=DAY_TIME_CHOICES,
        default='BR',
        verbose_name='Momento del día',
    )
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f'{self.name}'


class Recipe(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE,  verbose_name='Comida')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='Ingredients', verbose_name='Ingrediente')
    quantity =   models.FloatField(verbose_name='Cantidad')

    def __str__(self) -> str:
        return f'{self.meal}'


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Categoría')

    def __str__(self) -> str:
        return f'{self.name}'
    


