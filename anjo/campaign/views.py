# coding: utf-8
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.db.models import Sum

from .models import Campaign, GetPayment
from .forms import CampaignForm, GetPaymentForm

from anjo.core.models import DashUser

@login_required
def create_campaign(request):
	if request.method == 'POST':
		campaign_form = CampaignForm(request.POST, request.FILES)
		if campaign_form.is_valid():
			cf = campaign_form.save(commit=False)
			cf.user = request.user
			cf.save()
			model = cf
			return render(request, 'campaign/success.html', {'model': model})
		else:
			print(campaign_form.errors)
	else:
		campaign_form = CampaignForm()
	return render(request, 'campaign/create_campaign.html', {'campaign_form': campaign_form})

def list_campaign(request):
	list_camp = Campaign.objects.all().order_by('-created_at')
	paginator = Paginator(list_camp, 5)
	page = request.GET.get('page')
	try:
		list_campaign = paginator.page(page)
	except PageNotAnInteger:
		list_campaign = paginator.page(1)
	except EmptyPage:
		list_campaign = paginator.page(paginator.num_pages)
	return render(request, 'campaign/list_campaign.html', {'list_campaign': list_campaign})

def details(request, id):
	camp_destails = get_object_or_404(Campaign, id=id)
	return render(request, 'campaign/list_campaign_detais.html', {'camp_destails': camp_destails})

@login_required
def list_my_campaign(request, user_id):
	my_campaign = Campaign.objects.filter(user=user_id)
	paginator = Paginator(my_campaign, 5)
	page = request.GET.get('page')
	try:
		mycampaign = paginator.page(page)
	except PageNotAnInteger:
		mycampaign = paginator.page(1)
	except EmptyPage:
		mycampaign = paginator.page(paginator.num_pages)
	return render(request, 'campaign/list_my_campaign.html', {'mycampaign': mycampaign})

@login_required
def received(request, campaign_id):
	total_campaign = DashUser.objects.filter(campaign=campaign_id).aggregate(Sum('value'))
	rec_campaign = DashUser.objects.filter(campaign=campaign_id)
	return render(request, 'campaign/received_campaign.html', {'rec_campaign': rec_campaign, 'total_campaign': total_campaign})

@login_required
def get_payment(request):
	campaign_p = Campaign.objects.filter(user=request.user)
	# c_id = request.POST.get('optid')
	# camp = Campaign.objects.get(id=request.POST.get('optid'))
	# print(c_id)
	created = False
	if request.method == 'POST':
		camp = Campaign.objects.get(id=request.POST.get('optid'))
		pay_form = GetPaymentForm(request.POST)
		if pay_form.is_valid():
			pf = pay_form.save(commit=False)
			pf.campaign_c = camp
			pf.user_c = request.user
			pf.save()
			created = True
		else:
			print(pay_form.errors)
	else:
		pay_form = GetPaymentForm()
	return render(request, 'campaign/get_payment.html', {'pay_form': pay_form, 'created': created, 'campaign_p': campaign_p})