from django.contrib import admin
from models import Campaign, GetPayment


class GetPaymentAdmin(admin.ModelAdmin):
	list_display = ('campaign_c', 'user_c', 'value', 'request_date')

class CampaignAdmin(admin.ModelAdmin):
	list_display = ('title', 'goal', 'donations', 'message', 'user')

admin.site.register(GetPayment, GetPaymentAdmin)
admin.site.register(Campaign, CampaignAdmin)