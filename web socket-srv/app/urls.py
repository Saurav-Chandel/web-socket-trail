
from django.urls import path, include
# from django.views.generic import TemplateView
# from django.contrib.auth.decorators import login_required
from rest_framework.routers import DefaultRouter
# from app.api import MessageModelViewSet, UserModelViewSet
from app import views
from .views import *


router = DefaultRouter()
router.register('message', MessageModelViewSet, basename='message-api')
router.register('user', ProfileModelViewSet, basename='profile-api')

urlpatterns = [
    path(r'api/v1/', include(router.urls)),


    path('<str:group_name>/', views.index,name='index'),

    # path('', login_required(
    #     TemplateView.as_view(template_name='core/chat.html')), name='home'),
]

