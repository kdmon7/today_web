from django.db import models


class Category(models.Model):
    ca_id = models.AutoField(primary_key=True)
    ca_name = models.CharField(max_length=45)


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_title = models.CharField(max_length=45)
    post_content = models.CharField(max_length=45)
    created_at = models.DateTimeField()
    post_img = models.CharField(max_length=45, blank=True, null=True)
    category = models.ForeignKey(Category, models.DO_NOTHING, blank=True, null=True)
