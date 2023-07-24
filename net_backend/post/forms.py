from django.forms import ModelForm
from.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('body',)
        



# we only want the field body only        