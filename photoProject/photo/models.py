from distutils.command import upload
from django.db import models

from accounts.models import CustomUser

class Category(models.Model):
    title = models.CharField(
        verbose_name='カテゴリ',
        max_length=20
    )

    def __str__(self):
        '''オブジェクトを文字列に変換して返す
        
        Return(str): カテゴリ名
        '''

        return self.title

class PhotoPost(models.Model):
    '''モデルクラス
    '''

    user = models.ForeignKey(
        CustomUser,
        verbose_name='ユーザー',
        on_delete=models.CASCADE    # ユーザーを削除する場合、投稿データもすべて削除
    )

    category = models.ForeignKey(
        Category,
        verbose_name='カテゴリ',
        on_delete=models.PROTECT   # そのカテゴリを削除しないようにする
    )

    title = models.CharField(
        verbose_name='タイトル',
        max_length=200
    )

    comment = models.TextField(
        verbose_name='コメント'
    )

    image1 = models.ImageField(
        verbose_name='イメージ1',
        upload_to = 'photos'
    )

    image2 = models.ImageField(
        verbose_name='イメージ2',
        upload_to = 'photos',
        blank=True, 
        null=True
    )

    posted_at = models.DateTimeField(
        verbose_name='投稿日時',
        auto_now_add=True
    )

    def __str__(self):
        '''オブジェクトを文字列に変換して返す

        Return(str): 投稿記事のタイトル
        '''
        return self.title
