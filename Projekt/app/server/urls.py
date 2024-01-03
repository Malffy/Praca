from rest_framework import routers
from django.urls import path, include
from .views import ServerViewSet, StatsViewSet, VoteViewSet, PostViewSet, SectionViewSet, ActiveUserList

router = routers.DefaultRouter()
router.register(r'server', ServerViewSet)
router.register(r'stats', StatsViewSet)
router.register(r'vote', VoteViewSet)
router.register(r'post', PostViewSet)
router.register(r'section', SectionViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('active-users/', ActiveUserList.as_view(), name='active-users'),
]
