"""firstProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# リクエストされたら、下記からマッチするURLパターンを探す
# マッチしたURLで、レスポンスを作成し、ブラウザに返す
# pathのパラメータ path(route, view, kwargs=None, name=None)
'''
    route   ルートディレクトリ
    view    ビューまたは、as_view()で返されるビューを指定する
    kwargs  ビューで定義された関数やメソッドに、引数がある場合、
        指定した値を渡すことができる
    name    path()関数で、指定したＵＲＬパターンに名前を付けることができる
'''
urlpatterns = [
    # リクエストされたURLページへのフルパス部分が、admin/にマッチした場合
    # admin.site.urlsを呼び出して、Django管理サイトを表示する
    path('admin/', admin.site.urls),
    
    # http(s)://<ホスト名>/以下のURLパターンにblogアプリの
    # URLconf(urls.py)を含める
    path('', include('blog.urls')),
]
