# 管理者ページ
from django.contrib import admin
from .models import Post

# Postモデルを管理者ページに登録。
admin.site.register(Post)