from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'tags', views.TagViewSet)

urlpatterns = [	
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework',),),
    url(r'^', include(router.urls),),
]
