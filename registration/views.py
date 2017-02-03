from django.shortcuts import render,redirect
from django.views import View
from .forms import UserForm,ProfileForm,LoginForm
from django.contrib.auth import authenticate, login ,logout,get_user_model

class HomeView(View):
	def get(self ,request ,*arg ,**kwargs):
		return render(request ,'home.html',{})
def RegisterView(request):
	form=UserForm()
	profile=ProfileForm()
	context={
		"form":form,
		"profile":profile,
	}
	return render(request,'register.html',context)
class IndexView(View):
	def get(self , request , *args , **kwwargs):
		context={}
		return render(request ,'index.html',context)
class loginview(View):
	template_name='login.html'
	form_class=LoginForm
	def get(self,request):
		form=LoginForm()
		context={
			"form":form,
		}
		return render(request,self.template_name,context)
	def post(self,request):
		form=LoginForm(request.POST)
		if form.is_valid():
			username=form.cleaned_data['username']
			password=form.cleaned_data['password']
			user = authenticate(username=username, password=password)

			if user is not None:

				login(request,user)
				return  redirect('/home/')
		return render(request,self.template_name,{"form":form})
def logoutview(request):
	logout(request)
	return redirect('/')