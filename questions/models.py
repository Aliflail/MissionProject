from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models


class Question(models.Model):
	question_text = models.CharField(max_length=220)
	def __str__(self):
		return self.question_text
class Answers(models.Model):
	Answer = models.CharField(max_length=220)
	Question =models.ForeignKey(Question , on_delete=models.CASCADE)
	def __str__(self):
		return self.Answer
class Correct(models.Model):
	Ans  =  models.ForeignKey(Answers, on_delete=models.CASCADE)
	Ques =  models.ForeignKey(Question, on_delete=models.CASCADE)		