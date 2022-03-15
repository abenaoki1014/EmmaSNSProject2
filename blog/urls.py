# pathをインポートする
from django.urls import path
# blogアプリのviewsモジュールを丸ごとインポート
from . import views

# URLパターンを逆引  きできるように名前を付ける
app_name = 'blog'

# URLパターンを登録するための変数
urlpatterns = [
    # リクエストされたURLのページへのフルパス部分が''(無し)にマッチングした場合
    # viewsモジュールのIndexViewクラスをインスタンス化する
    path('', views.IndexView.as_view(), name='index'),

    # リクエストされたURLが「blog-detail/レコードのid」の場合は
    # BlogDetailを実行
    path(
        # 詳細ページのURLは、「blog-detail/レコードのid」
        'blog-detail/<int:pk>/',
        # viewsモジュールのBlogDetailを実行
        views.BlogDetail.as_view(),
        # ＵＲＬパターンの名前を'blog_detail'にする
        name='blog_detail'
    ),
    path(
        'science-list/',
        views.ScienceView.as_view(),
        name='science_list'
    ),
    path(
        'dailylife-list/',
        views.DailyLifeView.as_view(),
        name='dailylife_list'
    ),
    path(
        'music-list/',
        views.MusicView.as_view(),
        name='music_list'
    ),
    path(
        'contact/',
        views.ContactView.as_view(),
        name='contact'
    ),
]