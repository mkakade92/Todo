from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.CreateTask,name='index'),
    path('task_detail/<str:pk>/',views.TaskDetail,name="task_detail"),
    path('updatetask/<str:pk>/',views.UpdateTask,name="update_task"),
    path('deletetask/<str:pk>/',views.DeleteTask,name="delete_task"),

]