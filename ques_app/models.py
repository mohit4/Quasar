from django.db import models

# Create your models here.
class Question(models.Model):
    '''
    Structure of a Question Model
    '''
    text = models.TextField(max_length=1000)
    author = models.CharField(max_length=50)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        '''String representation of a model object'''
        return self.text[:20]+'...'

class Answer(models.Model):
    '''
    Structure of an Answer Model
    '''
    text = models.TextField(max_length=5000)
    author = models.CharField(max_length=50, default='Anonymous')
    date_created = models.DateField(auto_now_add=True)
    votes = models.IntegerField(default=0)
    is_approved = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        '''String representation of a model object'''
        return self.text[:30]+'...'