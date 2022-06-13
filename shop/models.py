from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # Any extra fields would go here
    def __str__(self):
        return self.email


class member(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    user_num = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=150)
    user_pw = models.CharField(max_length=255)
    user_name = models.CharField(max_length=10)
    user_nick = models.CharField(max_length=150)
    user_phone = models.CharField(max_length=100)
    user_birthdate = models.DateField()
    user_gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    user_post = models.CharField(max_length=10)
    user_address1 = models.CharField(max_length=150)
    user_address2 = models.CharField(max_length=150)
    user_category = models.CharField(max_length=50, null=True, blank=True)
    user_img = models.CharField(max_length=255, null=True, blank=True)
    user_msg = models.TextField(null=True, blank=True)
    reg_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    user_grade = models.CharField(max_length=45)


class bbs_Document(models.Model):
    bbs_doc_code = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)
    product_content = models.TextField()
    product_price = models.CharField(max_length=255)
    product_img = models.CharField(max_length=255, null=True, blank=True)
    sold = models.CharField(max_length=1)
    edit_date = models.DateTimeField(auto_now=True)
    reg_date = models.DateTimeField(auto_now_add=True)
    cate = models.CharField(max_length=15)
    member_user_code = models.ForeignKey(member, on_delete=models.CASCADE)


class bbs_Comment(models.Model):
    bbs_cmt_code = models.AutoField(primary_key=True)
    comment = models.TextField()
    reg_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    member_user_code = models.ForeignKey(member, on_delete=models.CASCADE)
    bbs_document_bbs_doc_code = models.ForeignKey(bbs_Document, on_delete=models.CASCADE)


class bbs_File(models.Model):
    bbs_file_code = models.AutoField(primary_key=True)
    origin_name = models.CharField(max_length=255)
    file_path = models.CharField(max_length=255)
    content_type = models.CharField(max_length=50)
    file_size = models.IntegerField()
    reg_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    bbs_document_bbs_doc_code = models.ForeignKey(bbs_Document, on_delete=models.CASCADE)


class bbs_Cate(models.Model):
    cate_code = models.AutoField(primary_key=True)
    user_cate = models.CharField(max_length=15, null=True)
    edit_date = models.DateTimeField(auto_now=True)
    reg_date = models.DateTimeField(auto_now_add=True)
    bbs_document_bbs_doc_code = models.ForeignKey(bbs_Document, on_delete=models.CASCADE)


class notice(models.Model):
    notice_code = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    context = models.TextField()
    edit_date = models.DateTimeField(auto_now=True)
    reg_date = models.DateTimeField(auto_now_add=True)
    member_user_code = models.ForeignKey(member, on_delete=models.CASCADE)


class faq(models.Model):
    faq_code = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    context = models.TextField()
    edit_date = models.DateTimeField(auto_now=True)
    reg_date = models.DateTimeField(auto_now_add=True)
    member_user_code = models.ForeignKey(member, on_delete=models.CASCADE)


class qna(models.Model):
    qna_code = models.AutoField(primary_key=True)
    type = models.CharField(max_length=2)
    title = models.CharField(max_length=150)
    content = models.TextField()
    edit_date = models.DateTimeField(auto_now=True)
    reg_date = models.DateTimeField(auto_now_add=True)
    member_user_code = models.ForeignKey(member, on_delete=models.CASCADE)


class qna_Answer(models.Model):
    qna_aw_code = models.AutoField(primary_key=True)
    answer = models.TextField()
    edit_date = models.DateTimeField(auto_now=True)
    reg_date = models.DateTimeField(auto_now_add=True)
    qna_qna_code = models.ForeignKey(qna, on_delete=models.CASCADE)


class n_Product(models.Model):
    n_code = models.AutoField(primary_key=True)
    n_name = models.CharField(max_length=45, null=True, blank=True)
    n_img = models.CharField(max_length=45, null=True, blank=True)
    n_price = models.IntegerField()


class d_Product(models.Model):
    d_code = models.AutoField(primary_key=True)
    d_name = models.CharField(max_length=45, null=True, blank=True)
    d_img = models.CharField(max_length=45, null=True, blank=True)
    d_price = models.IntegerField()
