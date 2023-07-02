from django.db import models

# Create your models here.

class login(models.Model):
    ID = models.PositiveSmallIntegerField(primary_key=True)
    password =models.CharField(max_length=13)
    fname=models.CharField(max_length=13 , null=True)
    lname=models.CharField(max_length=13, null=True)
    chours=models.PositiveSmallIntegerField()
    gpa=models.DecimalField(max_digits=5, decimal_places=3)
    finance=models.PositiveIntegerField(null=True)



    def _str_(self):
      return self.ID
    
    empAuth_objects =models.Manager()




# ##########################################

# class courses(models.Model):
#     name =models.CharField(max_length=50)
#     Code =models.CharField(max_length=50)
#     CRN = models.IntegerField(5)
#     hours = models.IntegerField(3)


# class student(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     age = models.PositiveSmallIntegerField()
#     email =models.CharField(max_length=50 , unique= True)
#     phone_num=models.PositiveSmallIntegerField()
#     college =models.CharField(max_length=30)
#     major = models.CharField(max_length=30)
#     y=[
#         (1,1),
#         (2,2),
#         (3,3),
#         (4,4),
#     ]
#     current_year =models.PositiveSmallIntegerField(3 , choices= y)
#     current_GPA =models.DecimalField(max_digits=7, decimal_places=3)
#     hours =models.PositiveSmallIntegerField()
#     img =models.ImageField(upload_to='photoes')


#     past_courses =models.ManyToManyField( courses )
#     account = models.OneToOneField(login , on_delete=models.CASCADE ) 

    
# class finance(models.Model):
#     stu_id = models.OneToOneField(student, on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=5)
#     payment=models.BooleanField(default= True)





