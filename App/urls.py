from App.views import index,createTask,DeleteTask,UpdateTask
from django.urls import path

urlpatterns=[

        path('',index,name='index'),
        path('create/',createTask,name='createtask'),
        path('delete/<str:pkk>',DeleteTask,name='deletetask'),
        path('update/<str:pkk>',UpdateTask,name='updatetask')
]