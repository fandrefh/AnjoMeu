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

class Testimonials(models.Model):
	name = models.CharField(u'Nome', max_length=30)
	message = models.TextField(u'Mensagem')
	active = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.name

class Banks(models.Model):
	code_bank = models.PositiveIntegerField(u'Número do Banco', blank=True, null=True)
	bank_name = models.CharField(u'Nome do Banco', max_length=70)

	def __unicode__(self):
		return self.bank_name

	class Meta:
		verbose_name=u'Bank'
		verbose_name_plural=u'Banks'

class UserBank(models.Model):
	user = models.ForeignKey(User, blank=True, null=True, verbose_name=u'Usuário')
	bank = models.ForeignKey(Banks, verbose_name=u'Banco', unique=True)
	agency = models.CharField(u'Agência', max_length=20, unique=True)
	account_bank = models.CharField(u'Conta Bancária', max_length=50, unique=True)
	operation = models.CharField(u'Operação', max_length=10, blank=True, null=True, unique=True, help_text='Para correntista da CEF')

	def __unicode__(self):
		return "%s, %s, %s" % (self.bank, self.agency, self.account_bank)

	class Meta:
		verbose_name=u'User Bank'
		verbose_name_plural=u'User\'s Bank'