from django.db import models

""" Thing do when change model 
1. python manage.py makemigrations  (create migrations to DB)
2. python manage.py migrate (apply change to DB) 
"""


# Create your models here.
class Question (models.Model):

    #  like a field in java
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


    # like a method tostring in java 
    def __str__(self):
        return self.question_text
    
    def test(self):
        return "Method Testing Complete"


    


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text

    



