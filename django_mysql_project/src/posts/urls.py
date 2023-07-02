from django.conf.urls import url
from .views import views


urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^details/(?P<id>\d+)/$',views.details,name='details')
]

handler404=views.handle_404_error
handler500=views.handle_500_error