from django.conf.urls import patterns, url

urlpatterns = patterns('anjo.core.views',
	url(r'^$', 'homepage', name='homepage'),
	url(r'^enviar-depoimento/$', 'create_testimonial', name='createtestimonial'),
	url(r'^depoimentos/$', 'testimonial', name='testimonials'),
	url(r'^quem-somos/$', 'about', name='aboutus'),
	url(r'^como-funciona/$', 'howitwork', name='howwork'),
	url(r'^anjos/$', 'donor', name='donors'),
	url(r'^novo-usuario/$', 'register', name='newuser'),
	url(r'^login/$', 'user_login', name='userlogin'),
	url(r'^usuario-logado/$', 'user_logged', name='userlogged'),
	url(r'^logout/$', 'user_logout', name='userlogout'),
)