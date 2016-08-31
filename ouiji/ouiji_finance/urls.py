from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = {
	url(r'^quote/(?P<qn>[a-zA-Z]+)$', views.single_quote),
	url(r'^$', views.dash_view),
}
urlpatterns = format_suffix_patterns(urlpatterns)