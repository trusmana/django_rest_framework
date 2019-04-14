from django.conf.urls import url,include
from django.contrib import admin
from django.views import generic
from rest_framework import routers
from api.views import SongView

router = routers.DefaultRouter()
router.register('song',SongView)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',generic.TemplateView.as_view(template_name='inti.html')),
    url(r'^api/', include(router.urls)),
]
