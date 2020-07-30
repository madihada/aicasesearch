# -*- coding: utf-8 -*-

from django import forms

from .models import Post, Keywords, Sentence

# 원래 것 임
# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = [
#             "title",
#             "subtitle",
#             "content",
#             "content2",
#             "content3",
#             # "image",
#         ]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "subtitle",
            "content",
            # "content2",
            # "content3",
            # "image",
        ]

###########################
class KeywordForm(forms.ModelForm):
    class Meta:
        model = Keywords
        fields = [
            # "keyword",
            # "키워드검색",
            "유사어검색",

        ]

##########################
class SentenceForm(forms.ModelForm):
    class Meta:
        model = Sentence
        fields = [
            "s_content"
        ]