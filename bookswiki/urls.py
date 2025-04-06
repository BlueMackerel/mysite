from django.urls import path

from . import views
app_name='bookswiki'
urlpatterns = [
    path('',views.index,name='index'),
    path('<str:subject>/',views.showdocs,name='detail'),
    path('modify_list/<str:subject>/', views.showdocsmodify, name='modify_list'),
    path('document/create/',views.docscreate,name='document_create'),
    path('document/modify/<str:subject>/', views.docsmodify, name='document_modify'),
    path('document/delete/<str:subject>/', views.docsdelete, name='document_delete'),
    path('document/search/', views.list, name='search'),


]