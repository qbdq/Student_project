from django.db import models
from django.utils import timezone
# Create your models here.



#! Student abstract model
class Student(models.Model):
    name = models.CharField( max_length=50)
    dob = models.DateField(default=timezone.now)

    class Meta:
        abstract = True
        verbose_name = "Student"
        verbose_name_plural = "Students"


# ! Bachelor model
class Bachelor(Student):
    # Defining a class for year_of_study_choices 

    class education(models.Choices):
        first_year = ("1st" , "First year")
        second_year = ("2nd" , "Second year")
    
    Year_of_study = models.CharField(max_length=50)
    
    class Meta:
        db_name = "Bachelor"
        verbose_name = "Bachelor"
        verbose_name_plural = "Bachelor"



# ! Terminal model
class Terminal(Student):
    
    espmark = models.DecimalField( max_digits=2, decimal_places=2)

    class Meta:
        db_name = "Terminal"
        verbose_name = "Terminal"
        verbose_name_plural = "Terminals"