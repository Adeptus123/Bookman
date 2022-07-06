from email import message
from django.shortcuts import redirect, render
from datetime import datetime
from django.http import HttpResponse
from django.contrib.auth.models import User 
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth import get_user_model
from django.contrib import messages

from library.models import Book
User = get_user_model()

# Create your views here.
def home(request):
    return render(request,'home.html')

def librarian(request):
    allBooks = Book.objects.all()
    context = {'Books': allBooks}
    return render(request, 'librarian.html', context)

def reader(request):
    allBooks = Book.objects.all().filter(bowner='library')
    context = {'Books': allBooks}
    return render(request,'reader.html',context)

def yourbooks(request):
    user=request.user.username
    allBooks = Book.objects.all().filter(bowner=user)
    context = {'Books': allBooks}
    return render(request,'yourbooks.html',context)

def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        job=request.POST['job']
        # try some common errors
        if User.objects.filter(username=username).exists():
            messages.error(request,'Username already exists.Please enter another.')
            return redirect('home')
        myuser = User.objects.create_user(username=username, email=email,job=job)
        myuser.set_password(password)
        myuser.save()
        messages.success(request,'You have succesfully signed up')
        return redirect('home')
        
    else:
        return HttpResponse("this is signup else")   

def signin(request):
    if request.method=='POST':
       username=request.POST.get('username')
       password=request.POST.get('password')
       print(username,password)
       user=authenticate(username=username,password=password)
       if user is not None:
           login(request,user)
           ujob=request.user.job
           print(ujob)    
           if ujob=='librarian':
               return redirect('librarian')
           else:
               return redirect('reader')    
       else:
           messages.error(request,'Wrong username or password.Please Try again')
           return redirect('home')

def signout(request):
    logout(request)
    # messages.success(request,'You have successfully logged out')
    return redirect('home')

def addbook(request):
    if request.method=='POST':
        bname=request.POST.get('bname')
        bdesc=request.POST.get('bdesc')
        bdate=datetime.now()
        ins=Book(bname=bname,bdesc=bdesc,bdate=bdate,bowner='library')
        ins.save()
        messages.success(request,"The book is succesfully added")
        return redirect('librarian')
    else:
        return HttpResponse("Not working")    

def lendbook(request,pk):
    if request.method=='POST':
        books=Book.objects.get(id=pk)
        bname=books.bname
        bowner=request.user.username
        books.bowner=bowner
        books.save()
        messages.success(request,f"{bname} is successfully lended")
        return redirect('reader')
    else:
        return HttpResponse("Not working")        

def returnbook(request,pk):
    if request.method=='POST':
        books=Book.objects.get(id=pk)
        bname=books.bname
        books.bowner='library'
        books.save()
        messages.success(request,f"{bname} is successfully returned")
        return redirect('yourbooks')
    else:
        return HttpResponse("Not working")     

def search(request):
    return render(request,'search.html')

def deleteBook(request,pk):
    Books=Book.objects.get(id=pk)
    Books.delete()
    messages.success(request,f"The Book is successfully deleted")
    return redirect('librarian')