from django.db import models

class BlogPost(models.Model):
    '''モデルクラス
    '''
    # カテゴリに設定する項目を入れ子のタプルとして定義
    # 最初の要素は、モデルが使用する値、二番目の要素は、選択メニューに表示する文字列
    CATEGORY = (('science', '科学のこと'), ('deily', '日常のこと'), ('music', '音楽の事'))

    # タイトル用のフィールド
    title = models.CharField(
        verbose_name='タイトル',    # フィールドのタイトル
        max_length=200              #  最大文字数は２００
    )

    # 本文用のフィールド
    content = models.TextField(
        verbose_name='本文'         # フィールドのタイトル
    )

    # 投稿日時のフィールド
    posted_at = models.DateField(
        verbose_name='投稿日時',    # フィールドのタイトル  
        auto_now_add=True           # 日時を自動追加
    )

    # カテゴリのフィールド
    category = models.CharField(
        verbose_name='カテゴリ',    # フィールドのタイトル
        max_length=50,              # 最大文字数５０
        choices=CATEGORY
    )

    def __str__(self):
        '''オブジェクトの文字列に変換して返す
        
        Return(str):投稿記事のタイトル
        '''
        return self.title
