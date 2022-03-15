from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    '''
    UserCreationFormのサブクラス
    '''
    class Meta:
        '''
        UserCreationFormのインナークラス

        Attributes:
            model:連携するUserモデル
            fields:フォームで使用するフィールド
        '''
        model = CustomUser
        '''連携するUserモデルを設定'''
        fields = ('username', 'email', 'password1', 'password2')
        '''
        フォームで使用するフィールド
        ユーザー名、メールアドレス、パスワード、パスワード確認用
        '''