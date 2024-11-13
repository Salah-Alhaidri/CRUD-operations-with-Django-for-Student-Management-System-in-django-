from django.urls import path
from app import views

urlpatterns = [
    path('', views.student_records_list, name="student_records_list"),
    path('insert', views.insert_student_record, name="insert_student_record"),
    path('update/<int:id>', views.update_student_record, name="update_student_record"),
    path('delete/<int:id>', views.delete_student_record, name="delete_student_record"),
]
