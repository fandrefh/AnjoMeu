from django.contrib import admin

from .models import AboutUs, HowItWork, UserProfile, Testimonials, Banks, UserBank

class UserBankAdmin(admin.ModelAdmin):
	pass

class BanksAdmin(admin.ModelAdmin):
	list_display = ('code_bank', 'bank_name')

class TestimonialsAdmin(admin.ModelAdmin):
	pass

class AboutAdmin(admin.ModelAdmin):
	pass

class HowItWorkAdmin(admin.ModelAdmin):
	pass

admin.site.register(UserBank, UserBankAdmin)
admin.site.register(Banks, BanksAdmin)
admin.site.register(Testimonials, TestimonialsAdmin)
admin.site.register(UserProfile)
admin.site.register(AboutUs, AboutAdmin)
admin.site.register(HowItWork, HowItWorkAdmin)