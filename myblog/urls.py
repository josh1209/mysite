from django.urls import path
from .views import stub_view, list_view, detail_view, add_model

urlpatterns = [
    path('', list_view, name='blog_index'),
    path('posts/<int:post_id>/', detail_view, name='blog_detail'),
    path('template/', add_model, name='template_test')
]
