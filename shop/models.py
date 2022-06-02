from django.db import models
from django.utils import timezone


class Member(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.CharField(max_length=150)
    user_pw = models.CharField(max_length=255)
    user_name = models.CharField(max_length=10)
    user_nick = models.CharField(max_length=150)
    user_phone = models.CharField(max_length=100)
    user_birthdate = models.DateTimeField()
    user_gender = models.CharField(max_length=10)
    user_post = models.CharField(max_length=10)
    user_address1 = models.CharField(max_length=150)
    user_address2 = models.CharField(max_length=150)
    user_category = models.CharField(max_length=50, null=True)
    user_img = models.CharField(max_length=255, null=True)
    user_msg = models.TextField(null=True)
    reg_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    user_grade = models.CharField(max_length=45)
