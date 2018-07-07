from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from pictures import views

urlpatterns = [
    url(r'^pictures/$', views.PicturesList.as_view()),
    url(r'^pictures/toApprove/$', views.PicturesToApprove.as_view()),
    url(r'^pictures/approved/$', views.PicturesApproved.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)