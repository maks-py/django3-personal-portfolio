from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name' : forms.TextInput(attrs={'class':'input',
                                            'placeholder' : 'who is comment',
                                            'id' : 'name'}),
            'body' : forms.Textarea(attrs={'class':'textarea',
                                           'rows' : 5,
                                           'placeholder' : 'comment body',
                                           'id' : 'body'}),
        }
