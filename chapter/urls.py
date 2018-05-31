from django.urls import path
from . import views

urlpatterns = [
    # chapter/
    path('', views.chapter, name='chapter'),
    # chapter/3
    path('<int:chapter_id>/', views.chapter_detail, name='chapter_detail'),
    # chapter/3/contact
    path('<int:chapter_id>/contact/',
         views.chapter_contact, name='chapter_contact'),
    # chapter/<id>/member
    path('<int:chapter_id>/member/', views.chapter_members, name='chapter_members'),
    # chapter/member/
    path('member/', views.member, name='member'),
    # chapter/member/2
    path('member/<int:member_id>/', views.member_detail, name='member_detail'),
    # chapter/member/2/contact
    path('member/<int:member_id>/contact/',
         views.member_contact, name='member_contact'),
]
