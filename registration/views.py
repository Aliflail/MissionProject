from django.shortcuts import render,redirect,get_object_or_404,HttpResponse,HttpResponseRedirect
from django.views import View
from .forms import UserForm,ProfileForm,LoginForm,UserRegisterForm
from django.contrib.auth import authenticate, login ,logout,get_user_model
from django.contrib.auth.models import User
from .models import Profile,Tests,Question,Choice,Correct,Testscore
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse
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
		error=''
		context={
			"t":t,
			"error_message":error
		}
		return render(request,self.template_name,context)
	def post(self,request,test_id):
		t = get_object_or_404(Tests, pk=test_id)
		if Testscore.objects.get(user=request.user):
			score=Testscore.objects.get(user=request.user,test=t)
		else:
			score=Testscore.objects.create(user=request.user,test=t)
		try:
			q = t.question_set.get(pk=request.POST['question'])
			selected_choice=q.choice_set.get(pk=request.POST['choice'])
		except(KeyError,Choice.DoesNotExist):
			context = {
				"t": t,
				"error":"you didnt select a choice"
			}
			return render(request,self.template_name,context)
		else:
			s = selected_choice.correct_set.filter(pk=request.POST['choice']).count()
			if s is not 0 :
				print(q.correct_set.get(pk=request.POST['question']))
				print(selected_choice.correct_set.filter(pk=request.POST['choice']).count())
				if q.correct_set.get(pk=request.POST['question']) == selected_choice.correct_set.get(pk=request.POST['choice']):
					score.score+=1
					score.save()
					return HttpResponseRedirect(reverse('test', args=(test_id)))
			else:
				return HttpResponseRedirect(reverse('test', args=(test_id)))








class TestQuestionView(LoginRequiredMixin,View):
	login_url = '/login/'
	redirect_field_name = '/login/'
	template_name="question.html"
	ii = 1

	def get(self,request,test_id):
		t=get_object_or_404(Tests,pk=test_id)
		error=''
		j=1

		for q in Question.objects.filter(testno=t.id):
			if j < self.ii:
				j+=1
			else:
				break
		context={
			"q":q,
			"t":t,
			"error_message":error
		}
		return render(request,self.template_name,context)
	def post(self,request,test_id):
		t = get_object_or_404(Tests, pk=test_id)
		j=1
		if Testscore.objects.get(user=request.user):
			score=Testscore.objects.get(user=request.user,test=t)
		else:
			score=Testscore.objects.create(user=request.user,test=t)
		try:
			for q in Question.objects.filter(testno=t.id):
				if j < self.ii:
					j += 1
				else:
					break
			selected_choice=q.choice_set.get(pk=request.POST['choice'])
		except(KeyError,Choice.DoesNotExist):
			context = {
				"t": t,
				"error":"you didnt select a choice"
			}
			return render(request,self.template_name,context)
		else:
			error = ''
			s = selected_choice.correct_set.filter(pk=request.POST['choice']).count()
			if s is not 0 :
				if q.correct_set.get(pk=self.ii) == selected_choice.correct_set.get(pk=request.POST['choice']):
					score.score+=1
					score.save()
					print(Question.objects.filter(pk=self.ii).count())
					if Question.objects.filter(pk=self.ii).count() is not 0:
						self.ii += 1
						q = Question.objects.get(pk=self.ii)
					else:
						return HttpResponse("your score is "+score.score)
					context = {
						"q": q,
						"t": t,
						"error_message": error
					}
					return render(request,self.template_name,context)
			else:
				print(Question.objects.filter(pk=self.ii).count())
				if Question.objects.filter(pk=self.ii).count() is not 0:
					self.ii += 1
					q = Question.objects.get(pk=self.ii)

				else:
					return HttpResponse("your score is " + score.score)
				context = {
					"q": q,
					"t": t,
					"error_message": error
				}
				return render(request, self.template_name, context)



@login_required(login_url='login/')
def profileview(request):
	template_name='profile.html'
	context={
		"profile":Profile,
	}
	return render(request,template_name,context)