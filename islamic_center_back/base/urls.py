from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

news = [
    path('', News.as_view(), name='news'),
    path('add/', AddNews.as_view(), name='add_news'),
    path('delete/', DeleteNews.as_view(), name='delete_news'),
]

urlpatterns = [
    path('news/', include(news)),
    path('setlang/', SetLanguage.as_view(), name='setlang'),
    path('getlang/', GetLanguage.as_view(), name='getlang'),
    path('login/', CustomLoginView.as_view(), name="login"),
    path('register/', RegisterPage.as_view(), name='register'),
    path('register_ajax/', RegisterAjax.as_view(), name='register_ajax'),
    path('contacts/', Contacts.as_view(), name='contacts'),
    path('museum/', Museum.as_view(), name='museum'),
    path('charity/', Charity.as_view(), name='charity'),
    path('timetable/', TimeTable.as_view(), name='timetable'),
    path('about/', About.as_view(), name='about'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('', Main.as_view(), name='index'),
]
