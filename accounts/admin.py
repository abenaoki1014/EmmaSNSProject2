from django.contrib import admin

from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    '''管理ページのレコード一覧に表示するカラムを設定するクラス
    '''

    list_display = ('id', 'username')
    '''レコード一覧にidとusernameを表示'''
    list_display_links = ('id', 'username')
    '''表示するカラムにリンクを設定'''

admin.site.register(CustomUser, CustomUserAdmin)