from django.shortcuts import render
from myapp.models import User

# Create your views here.
def user(request):
	return render(request,'htmlpage/user.html',{})

def insertuser(request):
	vuid = request.POST['tuid'],
	vname = request.POST['tuname'],
	vemail = request.POST['tuemail'],
	vcontact = request.POST['tucontact']
	us = User(tuid=vuid,tuname=vname,tuemail=vemail,tucontact=vcontact);
	us.save();
	return render(request,'htmlpage/index.html',{})