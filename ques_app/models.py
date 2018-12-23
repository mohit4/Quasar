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