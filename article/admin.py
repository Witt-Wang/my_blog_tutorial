from django.contrib import admin
from .models import Article
from pagedown.widgets import AdminPagedownWidget
from django import forms

class ArticleForm(forms.ModelForm):
    content = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = Article
        fields = '__all__'

class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm

admin.site.register(Article,ArticleAdmin)
