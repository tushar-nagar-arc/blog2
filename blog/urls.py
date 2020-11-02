from django.urls import path
from .views import BlogListView,BlogDetailView
urlpatterns=[
    # path('',BlogListView.as_view(),name='home'),
    path('',BlogListView,name='home'),
    path('post/<int:pk>/',BlogDetailView,name='detail'),
]
