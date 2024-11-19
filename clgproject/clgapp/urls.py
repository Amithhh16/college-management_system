from django.contrib import admin
from django.urls import path,include
from clgapp import views



urlpatterns = [



    path('dep_add',views.dep_add,name='dep_add'),
    path('',views.index,name='index'),
    path('admin',views.adminhome,name='adminhome'),
    path('reg_teacher',views.reg_teacher,name='reg_teacher'),
    path('reg_student',views.reg_student,name='reg_student'),
    path('registration',views.registration,name='registration'),
    path('teacherhome',views.teacherhome,name='teacherhome'),
    path('studenthome',views.studenthome,name='studenthome'),
    path('logins',views.logins,name='logins'),
    path('lgout',views.lgout,name='lgout'),


    path('viewstudents',views.viewstudents,name='viewstudents'),
    path('viewstu',views.viewstu,name='viewstu'),
    path('viewteacher',views.viewteacher,name='viewteacher'),
    path('approve/<int:aid>',views.approve,name='approve'),
    path('approved_stview',views.approved_stview,name='approved_stview'),
    path('updatest',views.updatest,name='updatest'),
    path('updatestudent/<int:uid>',views.updatestudent,name='updatestudent'),
    path('updatete',views.updatete,name='updatete'),
    path('updateteacher/<int:uid>',views.updateteacher,name='updateteacher'),
    path('deletest/<int:id>',views.deletest,name='deletest'),
    path('viewtea',views.viewtea,name='viewtea'),
    path('deletete/<int:id>',views.deletete,name='deletete'),
    path('depbystudent',views.depbystudent,name='depbystudent'),
    path('depbyteacher',views.depbyteacher,name='depbyteacher')
    

    
    


]
