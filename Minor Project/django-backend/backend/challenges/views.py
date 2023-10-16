#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
import requests

from .models import Topic, Language, Problem
from .forms import UserForm,UserProfileInfoForm, UserLoginForm

def index(request):
    return render(request, "index.html")



##Learning Resources
def learningResources(request):
    data = Language.objects.all()
    context = {"languages": data}
    return render(request, "pages/learningResourcesHome.html",context)

def languageTopics(request, language):
    data = Topic.objects.filter(language__name=language)
    context = {"topics": data}
    return render(request, "pages/learningResourcesLanguage.html",context)

def topicContent(request, language, topicId):
	data = Topic.objects.get(pk=topicId)
	context = {"topic": data}
	return render(request, "pages/learningResourcesContent.html", context)


def codeEditor(request):
    return render(request, "pages/code editor.html")

@login_required
def customRoom(request):
    return render(request, "pages/custom room.html")


## challenges
@login_required
def challenges(request):
    return render(request, "pages/challenges.html")

def allProblems(request, difficulty):
	data = Problem.objects.filter(difficulty=difficulty)
	context = {"problems": data,"difficulty":difficulty}
	return render(request, "pages/problemList.html",context)

def problem(request, difficulty, problemId):
	data = Problem.objects.get(pk=problemId)
	context = {"problem": data}
	return render(request, "pages/problem.html",context)




def contact(request):
    return render(request, "pages/contact us.html")

def register(request):
     
	register_form = UserForm()
	login_form = UserLoginForm()

	if request.method == 'POST' and 'register' in request.POST:
		register_form = UserForm(request.POST)
		profile_form = UserProfileInfoForm()
	
		if register_form.is_valid():
			user = register_form.save()
			user.set_password(user.password)
			user.save()
            # Can't commit yet because we still need to manipulate
			profile = profile_form.save(commit=False)
            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
			profile.user = user
			profile.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("/")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	
	if request.method == 'POST' and 'login' in request.POST:
		# First get the username and password supplied
		login_form = UserLoginForm(request.POST)
		if login_form.is_valid():
			user = authenticate(username=login_form.cleaned_data["username"], password=login_form.cleaned_data["password"])

			# If we have a user
			if user:
				#Check it the account is active
				if user.is_active:
					# Log the user in.
					login(request,user)
					# Send the user back to some page.
					# In this case their homepage.
					return HttpResponseRedirect(reverse('index'))
				else:
					# If account is not active:
					return HttpResponse("Your account is not active.")
			else:
				return HttpResponse("Invalid login details supplied.")
		
	return render (request=request, template_name="pages/login signup.html", context={"register_form":register_form,"login_form":login_form})

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))

def compile_code(request):
	if request.method == 'POST':
		code = request.POST.get('code')
		language = request.POST.get('lang')
		print(code,language)
		# JDoodle API endpoint for code execution
		api_endpoint = "https://api.jdoodle.com/v1/execute"

		# JDoodle API credentials (replace with your own)
		client_id = "4be53239792086fc651032ad8dbb6b68"
		client_secret = "83c5c897ee8dd7b2ac3ac3d3d74701656ea0eabb079d761c4ee2e8e7a6113cde"

		# Prepare the request payload
		data = {
			"clientId": client_id,
			"clientSecret": client_secret,
			"script": code,
			"language": language,
			"versionIndex": "0",  # Use "0" for the latest version
		}

		# Make the API request to JDoodle
		response = requests.post(api_endpoint, json=data)
		print(response)
		if response.status_code == 200:
			result = response.json()
			output = result.get("output")
			return JsonResponse({'result': output})
		else:
			return JsonResponse({'result': f"Error: {response.status_code} - {response.text}"})    
		
	return render(request, "pages/problems.html")
