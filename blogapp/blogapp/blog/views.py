from django.shortcuts import render,get_object_or_404
from .models import Post,Comment
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailPostForm,CommentForm
from taggit.models import Tag
from django.db.models import Count

# Create your views here.

def post_list(request,tag_slug=None):
    object_list=Post.published.all()
    tag=None
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        object_list=object_list.filter(tags__in=[tag])
    paginator = Paginator(object_list, 5) # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)

    context={
        'posts':posts,
        'page': page,
        'tag': tag
    }
    
    return render(request,'blog/post/list.html',context)


# def post_detail(request, year, month, day, post):
#     #return HttpResponse(month)
#     #post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)
#     post = get_object_or_404(Post, slug=post, status='published',publish__year=year)
#     context={
#         'post':post
#     }
#     return render(request,'blog/post/detail.html',context)


# class PostListView(ListView):
#     queryset = Post.published.all()
#     context_object_name = 'posts'
#     paginate_by = 5
#     template_name = 'blog/post/list.html'


def post_share(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(Post, id=post_id, status='published')
    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            # ... send email
    else:
        form = EmailPostForm()

    return render(request, 'blog/post/share.html', {'post': post, 'form': form})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                             slug=post,
                             status='published',
                             publish__year=year,
                             #publish__month=month,
                             #publish__day=day
                            )
    # List of active comments for this post
    comments = post.comments.filter(active=True)
    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()

            comment_form=CommentForm() 
    else:
        comment_form = CommentForm()


    # List of similar posts
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:4]


    context={'post': post,'comments': comments,'comment_form': comment_form,'similar_posts': similar_posts}
    return render(request,'blog/post/detail.html',context)

