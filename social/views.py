from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User,auth
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Entry,Question
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy 
from django.core.exceptions  import  PermissionDenied





def home(request):

	return render(request,'index.html')
def post(request):
    return render(request,'post.html')



def signup(request):
    if request.method == 'POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        try:
            if password1==password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request,'Username already exits')
                    return redirect('sign')
                elif User.objects.filter(email=email).exists():
                    messages.info(request,'Email already exists')
                    return redirect('sign')
                else:
                    obj=User.objects.create_user(username=username,email=email,password=password1,first_name=first_name,last_name=last_name)
                    obj.save()
                    messages.info(request,'Account Successfully Created')
                    
                    return HttpResponseRedirect('/register/')
            else:
                return HttpResponseRedirect('/register/')

        except Exception as e:
        	return HttpResponseRedirect('/register/')

@csrf_exempt
def loginup(request):

    if request.method == 'POST':
    	username=request.POST['username']
    	password=request.POST['password']
    	obj=auth.authenticate(username=username,password=password)   
    	if obj is not None:
            auth.login(request,obj)
            return redirect('/blog')	
    	else:
            messages.info(request,'Username or password invalid')

            return redirect('/login/')
# Create your views here.

def register(request):

	return render(request,'signup.html')

def loginpage(request):

	return render(request,'login.html')

def profile(request):
    return render(request,'profile.html')


    
   

#def post(request):

   # return render(request,'blogpost.html')

def logout(request):
    auth.logout(request)
    return redirect('/home')

class HomeView(ListView):
    model=  Entry
    template_name='blogpost.html'
    context_object_name="entry"
    ordering =['-entry_date']
    
     

class EntryView(DetailView):
    model=Entry
    template_name='entry_detail.html'
    

    


class CreateEntryView(CreateView):


    model=Entry
    template_name='post.html'
    

    
    fields=['entry_title','entry_text']
    def form_valid(self,form):


        form.instance.entry_author=self.request.user
        return super().form_valid(form)


class QuestionHomeView(ListView):
    model= Question
    template_name='question.html'
    context_object_name="question"
    ordering =['-q_date']

class QuestionView(DetailView):
    model=Question
    template_name='detail_viewquestion.html'


def question_post(request):
    if request.method=="POST":
        post=request.POST['post']
        if post=="":
            return redirect('/ques/')
        else:
            instance=request.user
            obj=Question(q_text=post,q_auther=instance)
            obj.save()
            return redirect('/ques/')

class PostEditView(UpdateView):
    model = Entry
    template_name = 'edit_post.html'
    fields = ['entry_title','entry_text']


    def form_valid(self,form):


        form.instance.entry_author=self.request.user
        return super().form_valid(form)


class PostDeleteView(DeleteView):
    model = Entry
    template_name = 'delete_post.html'
    raise_exception=True

    








