#coding: utf-8
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AboutUs(models.Model):
	title = models.CharField(max_length=70)
	about_us = models.TextField()

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name=u'About Us'
		verbose_name_plural=u'About Us'

class HowItWork(models.Model):
	title = models.CharField(max_length=70)
	how_work = models.TextField()

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name=u'How it Work'
		verbose_name_plural=u'How it Work'

class UserProfile(models.Model):
	GENDER_CHOICES = (
		('M', 'Masculino'),
		('F', 'Feminino')
	)
	user = models.OneToOneField(User)
	cpf = models.CharField(u'CPF', max_length=14, help_text='Formato: 000.000.000-00')
	birthday = models.DateField(u'Data de Nascimento', help_text='Formato: 00/00/0000')
	gender = models.CharField(u'Sexo', max_length=1, choices=GENDER_CHOICES)
	address = models.CharField(u'Endereço', max_length=100, help_text='Informe seu endereço completo')
	code_postal = models.CharField(u'CEP', max_length=10, help_text='Formato: 00.000-000')
	neighborhood = models.CharField(u'Bairro', max_length=50)
	state = models.CharField(u'Estado', max_length=2)
	city = models.CharField(u'Cidade', max_length=50)
	phone_number = models.CharField(u'Telefone/Celular', max_length=14, help_text='Formato: (00)00000-0000')
	created_at = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.user.username