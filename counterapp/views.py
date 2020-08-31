from django.shortcuts import render,redirect
from .models import CounterModel

# Create your views here.
def helloworld(request):
	obj = CounterModel.objects.filter(id = 1)[0]
	ournumber = obj.number
	context = {'number': ournumber}
	return render(request,"helloworld/helloworld.html",context)

def hellostudent(request):
	return render(request,"hellostudent/hellostudent.html")

def increment(request):
	#here we need to write code for increments
	obj = CounterModel.objects.filter(id = 1)[0]
	obj.number = int(obj.number) + 1
	obj.save()
	return redirect(request.META['HTTP_REFERER'])

def decrement(request):
	#here we need to write code for decrements 
	obj = CounterModel.objects.filter(id = 1)[0]
	obj.number = int(obj.number) - 1
	obj.save()
	return redirect(request.META['HTTP_REFERER'])

def reset(request):
	#here we need to write code fro reset
	obj = CounterModel.objects.filter(id = 1)[0]
	obj.number = 0
	obj.save()
	return redirect(request.META['HTTP_REFERER'])