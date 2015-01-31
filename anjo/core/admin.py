from django.contrib import admin

from .models import AboutUs, HowItWork, UserProfile, Testimonials, Banks, UserBank, DashUser

class DashUserAdmin(admin.ModelAdmin):
	list_display = ('campaign', 'name_donator', 'email_donator', 'value')

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

admin.site.register(DashUser, DashUserAdmin)
admin.site.register(UserBank, UserBankAdmin)
admin.site.register(Banks, BanksAdmin)
admin.site.register(Testimonials, TestimonialsAdmin)
admin.site.register(UserProfile)
admin.site.register(AboutUs, AboutAdmin)
admin.site.register(HowItWork, HowItWorkAdmin)