from django.conf.urls import patterns, include, url
from pool_app.views import *
from pool_app import views
urlpatterns = patterns('',
	url(r'^$', 'django.contrib.auth.views.login'),
	# url(r'^get_user_master_photo/(?P<user_id>([a-zA-Z0-9]*)$)$', get_user_master_photo),
	# url(r'^get_toilet_kiosk_photo/(?P<tk_id>([a-zA-Z0-9]*)$)', get_toilet_kiosk_photo),
	# url(r'^get_user_master_details/',get_user_master_details),
	# url(r'^get_tk_master_details/',get_tk_master_details),
	# url(r'^add_toilet_user/',add_toilet_user),
	# url(r'^test',test),
)