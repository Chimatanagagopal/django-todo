
from django.urls import path
from .views import userRegisterview,userlogging,home,user_logout,studentget,studentpost,add_student_view,update_student_view,studentput,studeDelete
urlpatterns = [
    path('',userRegisterview,name='userRegisterview'),
    path('login/',userlogging,name='login'),
    path('home/',home,name='home'),
    path('studentget/',studentget,name='home'),
    path('add_student/', add_student_view, name='add_student'),
    path('updatestudent/<int:pk>/', update_student_view, name='updatestudent'),
    path('studentpost/',studentpost,name='studentpost'),
    path('studentput/<int:pk>/',studentput,name='studentput'),
    path('logout/',user_logout,name='logout'),
    path('delete/<int:pk>/',studeDelete,name="studeDelete")
]