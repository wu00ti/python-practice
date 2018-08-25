from django.urls import path
from . import views

app_name = 'lib'
urlpatterns = [
    path('addBook/',views.addBook,name='addBook'),
    path('detail/',views.detail,name='detail'),
    path('delBook/<int:book_id>',views.deleteBook,name='delBook'),
]
