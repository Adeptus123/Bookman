from . import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',views.home,name='home'),
    path('librarian',views.librarian,name='librarian'),
    path('reader',views.reader,name='reader'),
    path('yourbooks',views.yourbooks,name='yourbooks'),
    path('signin',views.signin,name='signin'),
    path('signup',views.signup,name='signup'),
    path('signout',views.signout,name='signout'),
    path('addbook',views.addbook,name='addbook'),
    path('lendbook/<int:pk>',views.lendbook,name='lendbook'),
    path('returnbook/<int:pk>',views.returnbook,name='returnbook'),
    path('deleteBook/<int:pk>',views.deleteBook,name='deleteBook')
]
