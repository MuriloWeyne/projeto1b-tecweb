from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete', views.delete, name='delete'),
    path('edit', views.edit, name='edit'),
    path('tag_list', views.tag_list, name='tag_list'),
    path('all_notes_with_tag', views.all_notes_with_tag, name='all_notes_with_tag'),
]
