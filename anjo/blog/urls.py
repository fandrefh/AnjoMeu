from django.conf.urls import patterns, url

urlpatterns = patterns('anjo.blog.views',
	url(r'^posts/$', 'list_posts', name='listposts'),
	url(r'^ler-post-completo/(?P<id>\d+)/$', 'post_details', name='postdetails'),
)
