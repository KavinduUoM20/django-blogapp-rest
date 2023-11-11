from django.urls import path,include
from .views import ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('',ArticleViewSet,basename='article')

urlpatterns = [
    path('', include(router.urls)),
    #path('', views.ArticleList.as_view(), name='article-list'),
    #path('<int:pk>/', views.ArticleDetails.as_view(), name='article-details'),

]