from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.views import View
from .forms import UserForm,ProfileForm,LoginForm,UserRegisterForm
from django.contrib.auth import authenticate, login ,logout,get_user_model
from django.contrib.auth.models import User
from .models import Profile,Tests,Question,Choice,Correct
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
class HomeView(LoginRequiredMixin,View):
	login_url = '/login/'
	redirect_field_name = '/login/'
	def get(self ,request ,*arg ,**kwargs):
		test=Tests.objects.order_by('-times')[:5]
		context={
			"test":test,
		}
		return render(request ,'home.html',context)

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

class TestView(LoginRequiredMixin,View):
	login_url = '/login/'
	redirect_field_name = '/login/'
	template_name="test.html"
	def get(self,request,test_id):
		t=get_object_or_404(Tests,pk=test_id)
		context={
			"t":t,
		}
		return render(request,self.template_name,context)
	def post(self,request,test_id):
		t = get_object_or_404(Tests, pk=test_id)
		try:
			q = t.question_set.get(pk=request.POST['question'])
			selected_choice=q.choice_set.get(pk=request.POST['choice'])
		except(KeyError,Choice.DoesNotExist):
			return HttpResponse("Error")
		else:
			if q.correct_set.get(pk=request.POST['question']) == selected_choice.correct_set.get(pk=request.POST['choice']):
				return HttpResponse("Correct option")
			else:
				return HttpResponse("Incorrect Option")

@login_required(login_url='login/')
def profileview(request):
	template_name='profile.html'
	context={
		"profile":Profile,
	}
	return render(request,template_name,context)