#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse

from .models import ResourceCard
from .forms import UserForm,UserProfileInfoForm, UserLoginForm

def index(request):
    return render(request, "index.html")

def learningResources(request):
    data = ResourceCard.objects.all()
    context = {"data": data}
    return render(request, "pages/learningResources.html",context)

def codeEditor(request):
    return render(request, "pages/code editor.html")

@login_required
def customRoom(request):
    return render(request, "pages/custom room.html")

@login_required
def challenges(request):
    return render(request, "pages/challenges.html")

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
