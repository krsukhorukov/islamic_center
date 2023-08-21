from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

news = [
    path('', News.as_view(), name='news'),
    path('add/', AddNews.as_view(), name='add_news'),
    path('delete/', DeleteNews.as_view(), name='delete_news'),
]

timetable = [
    path('', TimeTable.as_view(), name='timetable'),
    path('add/', AddTimetable.as_view(), name='add_timetable'),
    path('edit/', EditTimetable.as_view(), name='edit_timetable'),
    path('delete/', DeleteTimetable.as_view(), name='delete_timetable'),
]

about = [
    path('', About.as_view(), name='about'),
    path('edit/', AboutUsEdit.as_view(), name='edit_about'),
]

urlpatterns = [
    path('news/', include(news)),
    path('timetable/', include(timetable)),
    path('setlang/', SetLanguage.as_view(), name='setlang'),
    path('getlang/', GetLanguage.as_view(), name='getlang'),
    path('login/', CustomLoginView.as_view(), name="login"),
    path('register/', RegisterPage.as_view(), name='register'),
    path('register_ajax/', RegisterAjax.as_view(), name='register_ajax'),
    path('charity/', Charity.as_view(), name='charity'),
    path('museum/', Museum.as_view(), name='museum'),
    path('contacts/', Contacts.as_view(), name='contacts'),
    path('about/', include(about)),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('', Main.as_view(), name='index'),
]
