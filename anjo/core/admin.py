from django.contrib import admin

from .models import AboutUs, HowItWork, UserProfile, Testimonials

class TestimonialsAdmin(admin.ModelAdmin):
	pass

class AboutAdmin(admin.ModelAdmin):
	pass

class HowItWorkAdmin(admin.ModelAdmin):
	pass

admin.site.register(Testimonials, TestimonialsAdmin)
admin.site.register(UserProfile)
admin.site.register(AboutUs, AboutAdmin)
admin.site.register(HowItWork, HowItWorkAdmin)