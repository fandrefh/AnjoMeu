from django.conf.urls import patterns, url

urlpatterns = patterns('anjo.campaign.views',
	url(r'^criar-campanha/$', 'create_campaign', name='createcampaign'),
	url(r'^lista-de-campanhas/$', 'list_campaign', name='listcampaign'),
	url(r'^detalhes-da-campanha/(?P<id>\d+)/$', 'details', name='campaigndetails'),
)
