from anjo.blog.models import Post
from anjo.core.models import Testimonials


def display_allposts(request):
	try:
		posts = Post.objects.all().order_by('-post_date')[:5]
	except Exception, e:
		raise e

	return {'posts': posts}

def display_alltestimonial(request):
	try:
		testimonial = Testimonials.objects.all().order_by('-id')
	except Exception, e:
		raise e

	return {'testimonial': testimonial}