from django.conf.urls import url
from .views import views,errors

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^details/(?P<id>\d+)/$',views.details,name='details')
]

handler404 = errors.http_response_404
handler500 = errors.http_response_500