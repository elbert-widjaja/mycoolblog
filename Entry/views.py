from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .models import Posts, Categories, Comments
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

#signup library
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


#Signup
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('Entry:index')
    template_name = 'signup.html'

# Create your views here.

#Home page
def index(request):
    categories = Categories.objects.all()
    posts = Posts.objects.all()
    form = AuthenticationForm()
    like_id = -1
    for i in request.POST:
        if(request.POST[i] == 'Like'):
            like_id = i
    if(like_id != -1):
        post = Posts.objects.get(pk = like_id)
        post.post_like +=1
        post.save()
    
    context = {
        'categories': categories,
        'posts': posts,
        'form':form,
    }
    return render(request, 'Entry/index.html',context)

def categories(request):
    categories = Categories.objects.all()

    posts_count = [category.posts_set.count() for category in categories]
    print(posts_count)
    context = {
        'categories' : categories,
        'posts_count' : posts_count
    }
    return render(request, 'Entry/categories.html', context)

def category(request, category_id):
    categories = Categories.objects.all()
    category = Categories.objects.get(pk = category_id)
    posts = category.posts_set.all()
    context = {
        'categories' : categories,
        'posts' : posts
    }

    return render(request, 'Entry/category.html', context)

def new_category(request):
    try:
        #if not empty
        #create new category
        new = Categories(category = request.POST['category_name'],created_at = timezone.now())
        new.save()
        print(request.POST['category_name'])
        print("im here")
        return HttpResponseRedirect(reverse('Entry:categories'))
    except:
        return render(request,'Entry/new_category.html',{})
    
def posts(request):
    posts = Posts.objects.all()

    context = {
        'posts': posts,
    }
    return render(request, 'Entry/posts.html', context)

def post(request, post_id):

    post = Posts.objects.get(pk = post_id)
    comments = post.comments_set.all()

    context = {
        'post': post,
        'comments' : comments
    }
    return render(request, 'Entry/post.html', context)

def new_post(request):
    
    #if not empty
    #create new posts
    post_name = request.POST.get('post_name', False)
    post_description = request.POST.get('post_description', False)
    categories = Categories.objects.all()
    context = {}
    #edge case
    if(post_name == "" or post_description == ""):
        
        err_name = ""
        err_desc = ""
        if(post_name == ""):
            err_name = "please enter the post title"
        if(post_description == ""):
            err_desc = "please enter the post description"
        context = {
            'err_name':err_name,
            'err_desc':err_desc,
            'categories':categories
        }
        return render(request, 'Entry/new_post.html',context)
    #first time in
    elif(post_name == False and post_description == False):
        context = {
            'categories':categories
        }
        return render(request, 'Entry/new_post.html',context)
    #success
    else:
        category_id = request.POST.get('category_id',False)
        user_id = 1 ##todo
        print(category_id)
        new = Posts(post_name = post_name,post_description = post_description,created_at=timezone.now(),category_id = category_id,user_id = user_id)
        new.save()
        print(request.POST['post_name'])
        print("im here")
        return HttpResponseRedirect(reverse('Entry:posts'))

def users(request):
    users = User.objects.all()
    comment_count = [user.comments_set.count() for user in users]
    context = {
        'users': users,
        'comment_count': comment_count
    }
    return render(request, 'Entry/users.html', context)

def user(request,username):
    user = User.objects.get(username = username)
    comments = user.comments_set.all()
    
    context = {
        'user':user,
        'comments':comments,
    }
    return render(request, 'Entry/user.html',context)

# def new_comment(request, post_id):
#     comment_description = request.POST.get('comment_description', False)
#     category = Posts.objects.get(pk = post_id).category
#     user = Posts.objects.get(pk = post_id).user

#     context = {}
#     #edge case
#     if(comment_description == ""):
#         err_desc = ""
#         if(comment_description == ""):
#             err_desc = "please enter the comment description"
#         context = {

#             'err_desc':err_desc,
#         }
#         return render(request, 'Entry/new_comment.html',context)
#     #first time in
#     elif(comment_description == False):
#         context = {}
#         return render(request, 'Entry/new_comment.html',context)
#     #success
#     else:
#         print(category)
#         print(user)
#         category_id = request.POST.get('category_id',False)
#         user_id = 1 ##todo
#         print(category_id)
        
#         print("im here")
#         return HttpResponseRedirect(reverse('Entry:index'))
    