from django.conf.urls import url,include
from poems.views import *

urlpatterns = [
    url (r'^poems/$',PoemListView.as_view(),name='poem'),
    url(r'^poem/(?P<pk>[0-9]+)$',poem_detail,name='poem_detial')

]