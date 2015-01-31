# coding:utf-8
from django.db import models
from django.contrib.auth.models import User
from locale import setlocale, currency as coin, LC_ALL
import uuid, os

# Create your models here.

class Campaign(models.Model):

	def generate_new_filename(instance, filename):
		ext = filename.split('.')[-1]
		filename = '%s.%s' % (uuid.uuid4(), ext)
		return os.path.join('images', filename)


	user = models.ForeignKey(User, blank=True, null=True)
	title = models.CharField(u'Título da sua Campanha', max_length=50)
	goal = models.DecimalField(u'Meta R$', max_digits=15, decimal_places=2, help_text='De quanto você precisa?')
	donations = models.DecimalField(u'Doação de R$', max_digits=5, decimal_places=2, help_text='A partir de quanto gostaria de receber.');
	image = models.ImageField(u'Envie uma imagem', upload_to=generate_new_filename, help_text='Envie uma bela imagem para sua campanha.')
	message = models.TextField(u'Fale sobre sua campanha', help_text='Faça uma boa descrição da sua campanha')
	created_at = models.DateTimeField(auto_now_add=True)

	def real_coin(self):
		setlocale(LC_ALL, 'pt_BR.UTF-8')
		return coin(self.goal, grouping=True)
	real_coin.short_description = 'Meta: '

	def __unicode__(self):
		return self.title

class GetPayment(models.Model):
	campaign_c = models.ForeignKey(Campaign, verbose_name=u'Campanha', blank=True, null=True)
	user_c = models.ForeignKey(User, verbose_name=u'Usuário', blank=True, null=True)
	value = models.DecimalField(u'Valor R$', max_digits=15, decimal_places=2, help_text='Quanto quer sacar?')
	request_date = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.campaign