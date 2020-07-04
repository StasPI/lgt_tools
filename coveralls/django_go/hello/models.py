from django.db import models
from django.utils import timezone


class Staff(models.Model):
    personnel_number = models.PositiveIntegerField(primary_key=True)
    full_name = models.CharField(max_length=100)
    email_adress = models.EmailField
    department = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.personnel_number, self.full_name, self.email_adress, self.department, self.job_title}'


# ------------------------------------------------------------------------------------------
# Models for building clothing
# ------------------------------------------------------------------------------------------


class Supplier(models.Model):
    supplier = models.CharField(max_length=200)


class ClothingSize(models.Model):
    clothing_size = models.CharField(max_length=100)


class TypeOfClothing(models.Model):
    type_of_clothing = models.CharField(max_length=100)
    clothing_size = models.ForeignKey(ClothingSize, on_delete=models.CASCADE)


class Clothes(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    type_of_clothing = models.ForeignKey(TypeOfClothing,
                                         on_delete=models.CASCADE)
    product_title = models.CharField(max_length=200)
    article = models.CharField(max_length=200)
    operational_life_in_months = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{ self.supplier, self.type_of_clothing, self.product_title, self.article, self.operational_life_in_months}'


# ------------------------------------------------------------------------------------------
# пример выборки из 2 баз в одну по id
# ------------------------------------------------------------------------------------------


class Supp1(models.Model):
    supp1 = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.supp1}'


class Supp2(models.Model):
    supp2 = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.supp2}'


class JobTitles(models.Model):
    job = models.ForeignKey(Supp1, on_delete=models.CASCADE)
    job1 = models.ForeignKey(Supp2, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.job, self.job1}'


# python manage.py makemigrations
# python manage.py migrate
# python manage.py createsuperuser