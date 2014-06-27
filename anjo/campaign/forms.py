from django import forms
from .models import Campaign

class CampaignForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(CampaignForm, self).__init__(*args, **kwargs)
		self.fields['goal'].localize = True
		self.fields['goal'].widget.is_localized = True
		self.fields['donations'].localize = True
		self.fields['donations'].widget.is_localized = True

	class Meta:
		model = Campaign
		# excludes = ('user')