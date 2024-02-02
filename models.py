from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from sklearn.tree import DecisionTreeClassifier
import joblib
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms

# Create your models here.
GENDER = (
    (0, 'Female'),
    (1, 'Male'),
)


class Data(models.Model):
    name = models.CharField(max_length=100, null=True)
    sex = models.PositiveIntegerField(null=True)
    Age = models.PositiveIntegerField( null=True)
    EDUC = models.PositiveIntegerField(null=True)
    SES=models.PositiveIntegerField(null=True)
    MMSE=models.PositiveIntegerField(null=True)
    eTIV=models.PositiveIntegerField(null=True)
    nWBV=models.FloatField(null=True)
    ASF=models.FloatField(null=True)
    predictions = models.PositiveIntegerField( blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        ml_model = joblib.load('ml_model/xgboost.joblib')
        self.predictions = ml_model.predict(
            [[self.sex, self.Age, self.EDUC,self.SES,self.MMSE,self.eTIV,self.nWBV,self.ASF]])
        return super().save(*args, *kwargs)
       

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name



from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')