"""
Python and django define package 
"""
from django.shortcuts import render,redirect
from datetime import datetime
import pytz
from rest_framework.views import APIView
from rest_framework.views import Response
import smtplib
"""
user define file
"""
from studentinfo.models import users,usersSerializer,student,studentSerializer,marks,marksSerializer

def login(request):
    if request.method == 'POST':
        try:
            input_json = request.POST.dict()
            email = input_json.get('email',None)
            password = input_json.get('password',None)
            if users.objects.filter(user_email= email,password=password,isactive=True).exists():
                request.session['is_logged'] = True
                return redirect('home')
            else:
                return redirect('login')
        except Exception as ex:
            pass
    return render(request,'login.html')


def home(request):
    if request.session.has_key('is_logged'):
        output_json = {}
        output_json['is_session_exists'] = request.session.has_key('is_logged')
        student_info_obj=student.objects.all()
        student_info=studentSerializer(student_info_obj,many = True).data
        current_list = []
        for item in student_info:
            current_status = {}
            current_status['profile_id'] = item.get('profile_id',None)
            current_status['name'] = item.get('name',None)
            current_status['department'] = item.get('department',None)
            current_status['age'] = item.get('age',None)
            current_status['address'] = item.get('address',None)
            current_status['gender'] = item.get('gender',None)
            current_status['status'] = item.get('isactive',None)
            mark_id = item.get('mark',None)
            mark_info=marks.objects.filter(marks_id=mark_id).values('mark','semester')[0]
            current_status['mark'] = mark_info['mark']
            current_status['semester'] = mark_info['semester']
            current_list.append(current_status)
        output_json['Status'] = 'Success'
        output_json['Payload'] = current_list
        return render(request,'home.html',output_json)
    return redirect('login')

class Addnewstudent(APIView):
    def post(self,request,format = 'Json'):
        input_json = request.data
        output_json = {}
        output_json = add_new_student(input_json)
        return Response(output_json)


def add_new_student(input_json):
    output_json = {}
    try:
        insert_marks = {}
        insert_param = {}
        insert_marks['mark'] = float(input_json['marks'])
        insert_marks['semester'] = input_json['semester']
        serialized_marks_params = marksSerializer(data = insert_marks)
        if serialized_marks_params.is_valid(raise_exception = True):
            serialized_marks_params.save()
        mark_info = marks.objects.filter(mark=input_json['marks'],semester=input_json['semester'],isactive=True).values('marks_id').order_by('-marks_id')[0]
        insert_param['name'] = input_json['name']
        insert_param['department'] = input_json['department']
        insert_param['age'] = input_json['age']
        insert_param['address'] = input_json['address']
        insert_param['gender'] = input_json['gender']
        insert_param['marks'] = mark_info['marks_id']
        serialized_user_params = studentSerializer(data = insert_param)
        if serialized_user_params.is_valid(raise_exception = True):
            serialized_user_params.save()
        output_json['Status'] = "Success"
        output_json['Message'] = "Data has been insert successfully"
    except Exception as ex:
        output_json['Status'] = "Failure"
        output_json['Message'] = "Data could not be inserted successfully" +str(ex)
        output_json['Payload'] = str(ex)
    return output_json

class DeleteStudent(APIView):
    def post(self,request,format = 'Json'):
        input_json = request.data
        output_json = {}
        output_json = delete_student(input_json)
        return Response(output_json)


def delete_student(input_json):
    output_json ={}
    output_json['Payload'] = {}
    try:
        if (input_json.get('status',None)) == '1':
            student.objects.filter(profile_id=input_json.get('profile_id',None)).update(isactive=False)
        else:
            student.objects.filter(profile_id=input_json.get('profile_id',None)).update(isactive=True)
        output_json['Status'] = "Success"
        output_json['Message'] = "Status have been update successfully"
        output_json['msg_Status'] = input_json.get('status',None)
        return output_json
    except Exception as ex:
        output_json['Status'] = "Failure"
        output_json['Message'] = "Status have not been successfully. Exception encountered is " + str(ex)
        output_json['Payload'] = None
        return output_json

class EditStudentName(APIView):
    def post(self,request,format = 'Json'):
        input_json = request.data
        output_json = {}
        output_json = edit_student_name(input_json)
        return Response(output_json)


def edit_student_name(input_json):
    output_json ={}
    output_json['Payload'] = {}
    try:
        student.objects.filter(profile_id=input_json.get('profile_id',None)).update(name=input_json.get('new_name',None))
        output_json['Status'] = "Success"
        output_json['Message'] = "Status have been edited successfully"
        return output_json
    except Exception as ex:
        output_json['Status'] = "Failure"
        output_json['Message'] = "Status have not been successfully. Exception encountered is " + str(ex)
        output_json['Payload'] = None
        return output_json


def logout(request):
    del request.session['is_logged']
    return redirect('login')