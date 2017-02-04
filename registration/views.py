from django.shortcuts import render,redirect
from django.views import View
from .forms import UserForm,ProfileForm,LoginForm,UserRegisterForm
from django.contrib.auth import authenticate, login ,logout,get_user_model
from django.contrib.auth.models import User
from .models import Profile,Tests,Question,Choice
class HomeView(View):
	def get(self ,request ,*arg ,**kwargs):
		return render(request ,'home.html',{})
class RegisterView(View):
	template_name='register.html'
	def get(self ,request):
		form=UserRegisterForm()
		profile=ProfileForm()
		context={
			"form":form,
			"profile":profile,
		}
		return render(request,self.template_name,context)
	def post(self,request):
		form=UserRegisterForm(request.POST)
		profile=ProfileForm(request.POST)
		context = {
			"form": form,
			"profile": profile,
		}
		if form.is_valid() and profile.is_valid():
			user = form.save()
			profile = profile.save(commit=False)
			profile.user = user
			profile.save()
			if profile is not None:
				login(request,user)
				print("2")
				return redirect('/home/')
		return render(request,self.template_name,context)
			
class IndexView(View):
	def get(self , request , *args , **kwwargs):
		context={}
		return render(request ,'index.html',context)
class loginview(View):
	template_name='login.html'

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
class TestView(View):
	template_name="test.html"
	def get(self,request):
		Test=Tests.objects.all()
		context={
			"Test":Test,
		}
		return render(request,self.template_name,context)
