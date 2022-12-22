from django.db import models

# Create your models here.
class QuesModel(models.Model):
   question= models.CharField(max_length=200, null=False)
   opt1=models.CharField(max_length=200, null=False)
   opt2=models.CharField(max_length=200, null=False)
   opt3=models.CharField(max_length=200, null=False)
   opt4=models.CharField(max_length=200, null=False)
   ans=models.CharField(max_length=200, null=False)


   def __str__(self):
      return self.question

      