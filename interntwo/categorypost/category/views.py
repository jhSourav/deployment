from django.db.models import Q
from django.shortcuts import render
from .models import PostType,Posts
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def postType (request):
    type=PostType.objects.all()
    contex ={'type': type}
    return render(request, 'postcategory.html',contex)

def posts(request, name):
    post = Posts.objects.filter(type__name=name)
    query = request.GET.get("q")

    if query:
        post = post.filter(
            Q(Location__contains=query) |
            Q(Posting_title__contains=query) |
            Q(job_type__contains=query)

        )
    page = request.GET.get('page')

    paginator = Paginator(post, 3)
    post=paginator.get_page(page)

    context = {'post': post }
    return render(request, 'posts.html', context)