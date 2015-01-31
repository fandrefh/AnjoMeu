# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post


def list_posts(request):
	posts_list = Post.objects.all()
	paginator = Paginator(posts_list, 5)
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	return render(request, 'blog/list_post.html', {'posts': posts})

def post_details(request, id):
	post_id = get_object_or_404(Post, id=id)
	return render(request, 'blog/post_details.html', {'post_id': post_id})