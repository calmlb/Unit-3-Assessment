from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),    
    path('widgets/create/', views.WidgetCreate.as_view(), name = 'widget_create'),    
    path('widgets/delete/', views.WidgetDelete.as_view(), name= 'widget_delete')
]

