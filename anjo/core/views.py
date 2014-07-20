# coding: utf-8
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect

from .models import UserProfile, UserBank

from .models import AboutUs, HowItWork, Testimonials
from anjo.campaign.models import Campaign
from .forms import UserForm, UserProfileForm, TestimonialsForm, UserBankForm, BanksForm

def homepage(request):
	campaign = Campaign.objects.all().order_by('-created_at')[:5]
	camp_created = Campaign.objects.all().order_by('-created_at')[:4]
	testimonial = Testimonials.objects.all().order_by('-created_at')[:5]
	return render(request, 'index.html', {'campaign': campaign, 'camp_created': camp_created, 'testimonial': testimonial})

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

def create_testimonial(request):
	created = False
	
	if request.method == 'POST':
		test_form = TestimonialsForm(data=request.POST)
		if test_form.is_valid():
			test_form.save()
			created = True
	else:
		test_form = TestimonialsForm()
	return render(request, 'core/create_testimonial.html', {'test_form': test_form, 'created': created})



def testimonial(request):
	testimonial = Testimonials.objects.all().order_by('-created_at')
	return render(request, 'core/testimonials.html', {'testimonial': testimonial})


@login_required
def add_bank(request):
	created = False
	if request.method == 'POST':
		bank_form = UserBankForm(request.POST)
		if bank_form.is_valid():
			bf = bank_form.save(commit=False)
			bf.user = request.user
			bf.save()
			created = True
		else:
			print(bank_form.errors)
	else:
		bank_form = UserBankForm()
	return render(request, 'core/user_bank.html', {'bank_form': bank_form, 'created': created})

@login_required
def user_information(request, user_id):
	user_infor = get_object_or_404(UserProfile, user=user_id)
	user_bank = get_object_or_404(UserBank, user=user_id)
	return render(request, 'core/user_information.html', {'user_infor': user_infor, 'user_bank': user_bank})