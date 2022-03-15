from django.shortcuts import render
from django.urls import reverse_lazy
# django.views.genericからTemplateView DetailView FormViewをインポート
from django.views.generic import ListView, DetailView
# モデルBlogPostをインポート
from .models import BlogPost

from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import ContactForm
from django.contrib import messages

class IndexView(ListView):
    '''トップページのビュー
    
    投稿記事を一覧表示するため、ListViewを継承する

    Attributes:
        template_name: レンダリングするテンプレート
        context_object_name: object_listキーの別名を設定
        queryset: データベースのクエリ
    '''
    # index.htmlをレンダリングする
    template_name = 'index.html'
    # object_listキーの別名を設定
    context_object_name = 'orderby_records'
    # モデルBlogPostのオブジェクトにorder_by()を適用して
    # BlogPostのレコードを投稿日時の降順で並べ替える
    queryset = BlogPost.objects.order_by('-posted_at')
    # １ページに表示するレコードの件数
    paginate_by = 2

class BlogDetail(DetailView):
    '''詳細ページのビュー

    投稿記事の詳細を表示するので、DetailViewを継承する
    
    Attributes:
        template_name = レンダリングするテンプレート
        Model: モデルのクラス
    '''
    # post.htmlをレンダリングする
    template_name = 'post.html'
    # クラス変数modelにモデルBlogPostを設定
    model = BlogPost

class ScienceView(ListView):
    '''科学(science)カテゴリの記事を一覧表示するビュー
    '''
    template_name = 'science_list.html'
    model = BlogPost
    context_object_name = 'science_records'
    queryset = BlogPost.objects.filter(category='science').order_by('-posted_at')
    paginate_by = 2

class MusicView(ListView):
    '''音楽(music)カテゴリの記事を一覧表示するビュー
    '''

    template_name = 'music_list.html'
    model = BlogPost
    context_object_name = 'music_records'
    queryset = BlogPost.objects.filter(category='music').order_by('-posted_at')
    paginate_by = 2

class DailyLifeView(ListView):
    '''日常(dailylife)カテゴリの一覧表示するビュー
    '''

    template_name = 'dailylife_list.html'
    model = BlogPost
    context_object_name = 'dailylife_records'
    queryset = BlogPost.objects.filter(category='deily').order_by('-posted_at')
    paginate_by = 2

class ContactView(FormView):
    '''問い合わせページを一覧表示するビュー
    '''

    # contact.htmlをレンダリングする
    template_name = 'contact.html'
    # クラス変数form_classにforms.pyで定義したContactFormを設定
    form_class = ContactForm
    # 送信完了後にリダイレクトするページ
    success_url = reverse_lazy('blog:contact')

    def form_valid(self, form):
        '''FormViewクラスのform_valid()をオーバーライド

        フォームのバリデーションを通過したデータがPOSTされたときに呼ばれるメール送信を行う

        Parameters:
            form(django.forms.Form): 
                form_classに格納されているフォームのオブジェクト
        Return:
            HttpResponseRedirectのオブジェクト
            オブジェクトをインスタンス化するとsuccess_urlで設定されているURLにリダイレクトさせる
        '''
        form.send_email()
        return super().form_valid(form)
