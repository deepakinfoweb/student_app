from django.db import models
from datetime import datetime,timedelta
import uuid
from rest_framework import serializers

class users(models.Model):
    user_id = models.AutoField(primary_key=True) 
    user_email = models.CharField(max_length =100, default = None, null=False)
    password = models.CharField(max_length =100, default = None, null=False)
    isactive = models.BooleanField(default=True) #1=> Active, 2=> inactive
    def __str__(self):
        return str(self.user_id)

class marks(models.Model):
    marks_id = models.AutoField(primary_key=True) 
    mark = models.DecimalField(max_digits=100, decimal_places=2)
    semester = models.CharField(max_length =100, default = None, null=False)
    isactive = models.BooleanField(default=True) #1=> Active, 2=> inactive
    def __str__(self):
        return str(self.marks_id)
    

class student(models.Model):
    profile_id  = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, blank=False)
    department = models.CharField(max_length=100, blank=False)
    age=models.IntegerField(null=False, blank=False,unique=True)
    address = models.TextField(max_length=100, blank=False)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    mark = models.ForeignKey(marks, on_delete=models.CASCADE, default = 1)
    isactive = models.BooleanField(default=True) #1=> Active, 2=> inactive

    def __str__(self):
        return str(self.profile_id)

class usersSerializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = '__all__'

class marksSerializer(serializers.ModelSerializer):
    class Meta:
        model = marks
        fields = '__all__'

class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = '__all__'

