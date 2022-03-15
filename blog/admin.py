from django.contrib import admin
# modelsからBlogPostをインポート
from .models import BlogPost

# Django管理サイトにBlogPostを登録する
admin.site.register(BlogPost)