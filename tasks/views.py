from django.shortcuts import render,redirect
from .models import userRegister,studentData
from .forms import formRegister
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .serilazer import studentSerilazation
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
# Create your views here.
def userRegisterview(request):
    form=formRegister()
    if request.method=='POST':
        form=formRegister(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request,'tasks/register.html',{"form":form})
def userlogging(request):
    if request.method=='POST':
        username=request.POST['Name']
        password=request.POST['password']
        print(f"Username: {username}, Password: {password}")
        user=authenticate(request,username=username,password=password)
        print(f"Authenticated user: {user}")
        if user is not None:
            login(request,user)
            return redirect('home')
        messages.error(request, "Invalid username or password.")
        return redirect('login')
    return render(request,'tasks/login.html')
def home(request):
    return render(request,'tasks/home.html')
def user_logout(request):
    logout(request)
    return redirect('login')
#----------------------------------------------------------------
@api_view(['GET'])
def studentget(request):
    query_set=studentData.objects.all()
    serializer=studentSerilazation(query_set,many=True)
    return render(request, 'tasks/home.html', {'students': serializer.data})

def add_student_view(request):
    return render(request, 'tasks/ADDstudent.html')


@api_view(['POST'])
def studentpost(request):
    serializer = studentSerilazation(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return redirect('home')
    return Response(serializer.errors, status=400)

 

def update_student_view(request,pk):
    student = get_object_or_404(studentData, pk=pk)
    return render(request, 'tasks/updatestudent.html', {'student': student})

@api_view(['POST'])
def studentput(request,pk):
    query_set=studentData.objects.get(pk=pk)
    serializer = studentSerilazation(query_set,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return redirect('home')
    return Response(serializer.errors, status=400)
@api_view(['GET', 'DELETE'])
def studeDelete(request,pk):
    student = get_object_or_404(studentData, pk=pk) #model_name.objects.get(pk=pk)
    student.delete()
    return redirect('home')
 


