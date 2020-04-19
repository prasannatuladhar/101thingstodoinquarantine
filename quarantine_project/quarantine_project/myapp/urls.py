from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('next/<int:thing_id>',views.next,name='next'),

]
