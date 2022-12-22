from django.shortcuts import render, redirect
from .models import QuesModel
from django.urls import reverse
from .forms import AddQuesForm, CreateUserForm
from django.contrib.auth import login,logout,authenticate
# Create your views here.

def home(request):
   if request.method == 'POST':
      print(request.POST)
      questions= QuesModel.objects.all()
      print(questions)
      score=0
      wrong=0
      correct=0
      total=0
      for q in questions:
         total +=1
         print(request.POST.get(q.question))
         print(q.ans)
         print()
         if q.ans == request.POST.get(q.question):
            score += 10
            correct +=1
         else:
            wrong += 1
      percent = score/(total*10) * 100
      context = {
         'score': score,
         'time': request.POST.get('timer'),
         'wrong': wrong,
         'correct': correct,
         'percent': percent,
         'total': total
   }
      return render(request, 'quiz_app/result.html', context)
   else:
      questions=QuesModel.objects.all()
      context = {
         'questions': questions
      }
      return render(request, 'quiz_app/home.html', context)

def addQuestion(request):
   if request.user.is_staff:
      form=AddQuesForm()
      if(request.method == 'POST'):
         form=AddQuesForm(request.POST)
         if(form.is_valid()):
            form.save()
            return redirect('/')
      context={'form': form}
      return render(request, 'quiz_app/addQuestion.html', context)
   else:
      return redirect('home')

def registerPage(request):
   if request.user.is_authenticated:
      return redirect('home')
   else:
      form =CreateUserForm()
      if request.method == 'POST':
         form =CreateUserForm(request.POST)
         if form.is_valid:
            user= form.save()
            return redirect('login')

      context={
         'form':form,
      }
   return render(request, 'quiz_app/register.html', context)

def loginPage(request):
   if request.user.is_authenticated:
      return redirect('home')
   else:
      if request.method == 'POST':
         username= request.POST.get('username')
         password= request.POST.get('password')
         user= authenticate(request, username=username, password=password)
         if user is not None:
            login(request, user)
            return redirect('/')
         context={}
         return render(request, 'quiz_app/login.html', context)

def logoutPage(request):
   logout(request)
   return redirect('/')
