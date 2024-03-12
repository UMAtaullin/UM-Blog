from django import forms

from posts.models import Group


class AddPostForm(forms.Form):

    text = forms.CharField(widget=forms.Textarea)
    group = forms.ModelChoiceField(
        queryset=Group.objects.all(), required=False)

    # class Meta:
    #     model = Post
    #     fields = ('text', 'group')
