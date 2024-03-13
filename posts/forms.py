from django import forms

from posts.models import Group, Post


class AddPostForm(forms.Form):
    title = forms.CharField(label='Заголовок', max_length=100)
    text = forms.CharField(widget=forms.Textarea, label='Текст поста')
    group = forms.ModelChoiceField(
        queryset=Group.objects.all(), required=False,
        label='Название сообщества',
        empty_label='Не выбрана')

    def save(self, author):
        title = self.cleaned_data['title']
        text = self.cleaned_data['text']
        group = self.cleaned_data['group']
        # Create a new Post object and save it
        new_post = Post(title=title, text=text, group=group, author=author)
        new_post.save()

    # class Meta:
    #     model = Post
    #     fields = ('title', 'text', 'group')
