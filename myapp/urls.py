from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('modelformcreate/', views.modelformcreate, name='modelformcreate'),
    path('detail/<int:post_id>', views.detail, name='detail'),
]