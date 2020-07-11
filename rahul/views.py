from django.shortcuts import render,redirect
from . models import Create


# Create your views here.

def index(request):

	return render(request, 'rahul/index.html')

def create(request):
	return render(request, 'rahul/create.html')

def read(request):
	create = Create.objects.all()  
	return render(request, 'rahul/read.html',{'create':create})

def save(request):
	if request.method == "POST":
		first_name = request.POST.get('first_name','')
		last_name = request.POST.get('last_name','')
		company = request.POST.get('company','')
		phone = request.POST.get('phone','')
		email = request.POST.get('email','')
		website = request.POST.get('website','')
		store = Create(first_name = first_name,last_name=last_name,company=company,phone=phone,email=email,
			website=website)
		# print(store)
		store.save()
	return redirect('/read')

def edit(request,id):

	create = Create.objects.get(id=id)

	return render(request,'rahul/edit.html',{'create':create})

def update(request,id):

	user = Create.objects.get(id=id) 
	first_name = request.POST.get('first_name','')
	last_name = request.POST.get('last_name','')
	company = request.POST.get('company','')
	phone = request.POST.get('phone','')
	email = request.POST.get('email','')
	website = request.POST.get('website','')

	user.first_name = first_name	
	user.last_name = last_name	
	user.company = company	
	user.phone = phone	
	user.email = email	
	user.website = website
	user.save()	
	return redirect('/read')

def delete(request,id):
	user = Create.objects.get(id=id)
	user.delete()
	return redirect('/read')


