from django import forms
from .models import PostModel, Comment

class PostModelForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 8}))
    class Meta:
        model = PostModel
        fields = ('title', 'content')

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ('title', 'content')

class CommentForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Add Comment Here'}))
    class Meta:
        model = Comment
        fields =('content',)