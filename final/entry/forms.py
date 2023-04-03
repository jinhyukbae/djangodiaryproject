from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AddForm(forms.Form):

    productivity = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'type': 'range',
                'min': '0',
                'max': '10',
                'value': '5',
                'step': '1',
                'class': 'mb-3 form-control'
            }
        ),
        label='오늘의 감정 지수',
        required=True
    )

    note = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': '제목',
                'class': " form-control mb-3",
            }
        ),
        label='',
        required=True
    )

    content = forms.CharField(
        widget=forms.Textarea(
            {
                'placeholder': '영어로 일기 쓰기 ',
                'class': " form-control quilljs-textarea",
                'row': "15"
            }
        ),
        label='',
        required=True
    )
    
class UserForm(UserCreationForm):
    username = forms.CharField(label="아이디")
    password1 = forms.CharField(label="비밀번호")
    password2 = forms.CharField(label="비밀번호 확인")
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")