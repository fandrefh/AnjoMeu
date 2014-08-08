from django.conf.urls import patterns, url

urlpatterns = patterns('anjo.campaign.views',
	url(r'^criar-campanha/$', 'create_campaign', name='createcampaign'),
	url(r'^lista-de-campanhas/$', 'list_campaign', name='listcampaign'),
	url(r'^detalhes-da-campanha/(?P<id>\d+)/$', 'details', name='campaigndetails'),
	url(r'^minhas-campanhas/(?P<user_id>\d+)/$', 'list_my_campaign', name='mylistcampaign'),
	url(r'^recebido-campanha/(?P<campaign_id>\d+)/$', 'received', name='receivedcampaign'),
	url(r'^solicitar-saque/$', 'get_payment', name='getpayment'),
	url(r'^sucesso/$', 'create_campaign', name='succ'),
)
