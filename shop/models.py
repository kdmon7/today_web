from django.db import models
from django.utils import timezone


class member(models.Model):
    user_num = models.IntegerField(primary_key=True)
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


class bbs_Document(models.Model):
    bbs_doc_code = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=255)
    product_content = models.TextField(null=True)
    product_price
    sold
    edit_date
    reg_date
    cate
    member_user_code


class bbs_Comment(models.Model):
    bbs_cmt_code = models.IntegerField(primary_key=True)
    comment
    reg_date
    edit_date
    member_user_code
    bbs_document_bbs_doc_code


class bss_file(models.Model):
    bbs_file_code = models.IntegerField(primary_key=True)
    origin_name
    file_path
    content_type
    file_size
    reg_date
    edit_date
    bbs_document_bbs_doc_code


class bss_cate(models.Model):
    cate_code = models.IntegerField(primary_key=True)
    user_cate
    edit_date
    reg_date
    bbs_document_bbs_doc_code


class notice(models.Model):
    notice_code = models.IntegerField(primary_key=True)
    title
    context
    edit_date
    reg_date
    member_user_code


class faq(models.Model):
    faq_code = models.IntegerField(primary_key=True)
    title
    context
    edit_date
    reg_date
    member_user_code


class qna(models.Model):
    qna_code = models.IntegerField(primary_key=True)
    type
    title
    content
    edit_date
    reg_date
    member_user_code


class qna_answer(models.Model):
    qna_aw_code = models.IntegerField(primary_key=True)
    answer
    edit_date
    reg_date
    qna_qna_code


class n_product(models.Model):
    n_code = models.IntegerField(primary_key=True)
    n_name
    n_img
    n_price


class d_product(models.Model):
    d_code = models.IntegerField(primary_key=True)
    d_name
    d_img
    d_price