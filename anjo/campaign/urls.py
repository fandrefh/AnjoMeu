from django.conf.urls import patterns, url

urlpatterns = patterns('anjo.campaign.views',
	url(r'^criar-campanha/$', 'create_campaign', name='createcampaign'),
)
