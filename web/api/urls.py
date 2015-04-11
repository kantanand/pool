from django.conf.urls import patterns, include, url
from api.views import *
from pool_app import views
from api import views

urlpatterns = patterns('',
	url(r'^$', 'django.contrib.auth.views.login'),
	url(r'^add_user/', add_user),
	url(r'^find_hashtag/',find_hashtag),
	url(r'^search_question/',search_question),
	url(r'^create_question/',create_question),
	url(r'^answer_this_question/',answer_this_question),
	url(r'^get_answers/',get_answers),
	
	# url(r'^get_user_master_details/',get_user_master_details),
	# url(r'^get_tk_master_details/',get_tk_master_details),
	# url(r'^add_toilet_user/',add_toilet_user),
	# url(r'^test',test),
)