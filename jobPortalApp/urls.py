from jobPortalApp import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    # path('load_order',views.load_order,name='load_order'),
]