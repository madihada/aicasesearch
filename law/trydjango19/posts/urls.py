from django.conf.urls import url
from django.contrib import admin
from . import views

from .views import (
	post_list,
	post_create,
	post_detail,
	post_update,
	post_delete,
	keyword_create,
	keyword_sentence,
	contact
	# sentences,
	# jp_search,
	)

urlpatterns = [
	url(r'^$', post_list, name= 'list'),
	url(r'^create/$', post_create),
	url(r'^(?P<id>\d+)/$', post_detail, name='detail'),
	url(r'^(?P<id>\d+)/edit/$', post_update, name='update'),
	url(r'^(?P<id>\d+)/delete/$', post_delete),
	#url(r'^posts/$', "<appname>.views.<function_name>"),
	url(r'^contact/', views.contact, name='contact'),
	url(r'^keywords/contact/', views.contact, name='contact'),

	url(r'^keywords/$', keyword_create),
	# url(r'^sentences/$', sentences),
	url(r'^/keywords/sentences/$', keyword_sentence),

	# url(r'^/search/$', jp_search),

	# url(r'^keywords/edit/$', keyword_update, name='kupdate'),

]