from django.shortcuts import render
from django.views  import View
# Create your views here.
from .models import Question, Answers
class HomeView(View):
	def get(self ,request ,*args , **kwargs):
		latest_question_list = Question.objects.all()
		answer_list=Answers.objects.all()
		context={
		'latest_question_list':latest_question_list,
		'answer_list':answer_list
		}
		return render(request,'index.html',context)
		