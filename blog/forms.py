from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text') # 입력받을 변수를 지정 (폼에 보여질 양식)