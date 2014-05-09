#coding: utf-8
from django import forms
from localflavor.br.br_states import STATE_CHOICES
from django.contrib.auth.models import User
from .models import UserProfile, Testimonials


class TestimonialsForm(forms.ModelForm):
	class Meta:
		model = Testimonials
		exclude = ('active',)

class UserForm(forms.ModelForm):
	first_name = forms.CharField(label='Nome')
	last_name = forms.CharField(label='Sobrenome')
	username = forms.CharField(label='Nome de usuário')
	email = forms.EmailField(label='E-mail')
	password = forms.CharField(label='Senha', widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
	state = forms.ChoiceField(label='Estado', choices=STATE_CHOICES)

	class Meta:
		model = UserProfile
		fields = ('cpf', 'birthday', 'gender', 'address', 'code_postal', 'neighborhood', 'state', 'city', 'phone_number')