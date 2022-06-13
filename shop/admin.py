from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import *
from .forms import *


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email']


admin.site.register(member)
admin.site.register(bbs_Document)
admin.site.register(bbs_Comment)
admin.site.register(bbs_File)
admin.site.register(bbs_Cate)
admin.site.register(notice)
admin.site.register(faq)
admin.site.register(qna)
admin.site.register(qna_Answer)
admin.site.register(n_Product)
admin.site.register(d_Product)
