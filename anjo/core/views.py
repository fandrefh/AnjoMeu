# coding: utf-8
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect

from models import AboutUs, HowItWork
from anjo.campaign.models import Campaign
from .forms import UserForm, UserProfileForm


def homepage(request):
	campaign = Campaign.objects.all()
	return render(request, 'index.html', {'campaign': campaign})

def about(request):
	about_us = AboutUs.objects.all()
	return render(request, 'core/about_us.html', {'about_us': about_us})

def howitwork(request):
	how_work = HowItWork.objects.all()
	return render(request, 'core/how_it_work.html', {'how_work': how_work})

def donor(request):
	return render(request, 'core/donors.html')

def register(request):

	registered = False

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():

			user = user_form.save()

			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user

			profile.save()

			registered = True

		else:
			print user_form.errors, profile_form.errors
	
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	return render(request, 'core/register_user.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

def user_login(request):

	if request.method == 'POST':

		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)

		if user is not None:

			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/usuario-logado/')
			else:
				return HttpResponse('Sua conta está desabilitada.')
		else:
			print('Login inválido, detalhes: {0}, {1}'.format(username, password))
			login_error = 'Ops! Alguma coisa que "não está certo" deu errado! Por favor, tente novamente. :)'
			return render(request, 'core/user_login.html', {'login_error': login_error})

	else:
		return render(request, 'core/user_login.html', {})

@login_required
def user_logged(request):
	return render(request, 'core/user_logged.html')

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/')