from django.contrib import admin
from models import AboutUs, HowItWork, UserProfile

class AboutAdmin(admin.ModelAdmin):
	pass

class HowItWorkAdmin(admin.ModelAdmin):
	pass

admin.site.register(UserProfile)
admin.site.register(AboutUs, AboutAdmin)
admin.site.register(HowItWork, HowItWorkAdmin)