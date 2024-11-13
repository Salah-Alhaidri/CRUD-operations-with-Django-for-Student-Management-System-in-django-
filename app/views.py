from django.shortcuts import render, redirect,get_object_or_404
from .models import StudentRecordModel
from django.contrib import messages

# View to list all student records
def student_records_list(request):
    data = StudentRecordModel.objects.all()
    context = {"data": data}
    return render(request, "index.html", context)

# View to insert a new student record
def insert_student_record(request):
    if request.method == "POST":
        student_name = request.POST.get('student_name')
        student_email = request.POST.get('student_email')
        student_age = request.POST.get('student_age')
        student_gender = request.POST.get('student_gender')

        # Create and save new student record
        new_student = StudentRecordModel(
            student_name=student_name,
            student_email=student_email,
            student_age=student_age,
            student_gender=student_gender
        )
        new_student.save()
        messages.success(request, "Student record inserted successfully.")
        return redirect("student_records_list")

    return render(request, "insert.html")

# View to update an existing student record
def update_student_record(request, id):
    student = StudentRecordModel.objects.get(id=id)
    
    if request.method == "POST":
        student.student_name = request.POST['student_name']
        student.student_email = request.POST['student_email']
        student.student_age = request.POST['student_age']
        student.student_gender = request.POST['student_gender']
        student.save()
        messages.success(request, "Student record updated successfully.")
        return redirect("student_records_list")

    context = {"student": student}
    return render(request, "edit.html", context)

# View to delete a student record
def delete_student_record(request, id):
    d=StudentRecordModel.objects.get(id=id) 
    d.delete()
    messages.error(request,"Data deleted Successfully")
    return redirect("/")