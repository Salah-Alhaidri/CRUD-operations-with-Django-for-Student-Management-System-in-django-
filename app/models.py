from django.db import models

# Create your models here.
class StudentRecordModel(models.Model):
    student_name = models.CharField(max_length=50, blank=False, null=False)
    student_email = models.EmailField(unique=True, blank=False, null=False)
    student_age = models.PositiveIntegerField(blank=False, null=False)
    student_gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], blank=False, null=False)
    enrollment_date = models.DateField(auto_now_add=True)  # new field example

    def __str__(self):
        return self.student_name
