from django.shortcuts import render,redirect
from book.models import Book
from django.contrib.auth.models import User
from .forms import *
from django.http import *
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def create_book(request):
	if request.method=='GET':
		return render(request,"book/create_book.html",{})
	if request.method=='POST':
		name=request.POST.get('name','')
		author=request.POST.get('author','')
		book_ISBN=request.POST.get('book_ISBN','')
		pub_date=request.POST.get('pub_date')
		category=request.POST.get('category','')
		book=Book(name=name,author=author,book_ISBN=book_ISBN,pub_date=pub_date,category=category)

		book.save()
		return render(request,"book/create_book.html")

def list_of_book(request):
	if request.method=='GET':
		books=Book.objects.all()
		return render(request,"book/list_of_book.html",{'books':books})
	if request.method=='POST':
		name=request.POST.get('Search_Name')
	if name !="":
		books=Book.objects.filter(name=name)
	else:
		books=Book.objects.all()
	return render(request,"book/list_of_book.html",{'books':books})

def delete_book(request):
	if request.method=='POST':
		books=Book.objects.all()
		_id= request.POST.get('id')
		book= Book.objects.get(id=_id)
		book.delete()
		return render(request,"book/list_of_book.html",{'books':books})
def home_page(request):
	if request.method=='GET':
		return render(request,"book/home_page.html")
	if request.method=='POST':
		return render(request,"book/list_of_book.html",{'books':books})

def registration(request):
	if request.method=='POST':
		form1 = userform(request.POST)
		if form1.is_valid():
			username = form1.cleaned_data['username']
			first_name = form1.cleaned_data['first_name']
			last_name = form1.cleaned_data['last_name']
			email = form1.cleaned_data['email']
			password = form1.cleaned_data['password']
			User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
			return HttpResponseRedirect('/registration')

	else:
		form1 = userform()
	return render(request, 'book/registration.html', {'frm':form1})

def login(request):
	if request.method=='POST':
		username= request.POST['user']
		password= request.POST['pas']
		try:
			user = auth.authenticate(username=username, password=password)
			if user is not None:
				auth.login(request, user)
				return render(request,'book/list_of_book.html')
			else:
				messages.error(request, 'Username and password did not matched')

		except auth.ObjectNotExist:
			print("invalid user")

	return render(request,"book/login.html")

def logout(request):
	auth.logout(request)
	return render(request, 'book/login.html')