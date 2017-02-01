from django.shortcuts import render
from django.views import View
# Create your views here.
class HomeView(View):
	def get(self ,request ,*arg ,**kwargs):
		context={};
		return render(request ,'index.html',context)
class IndexView(View):
	def get(self , request , *args , **kwwargs):
		context={}
		return render(request ,'home.html',context)		