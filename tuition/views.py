
from django.template import loader
from django.shortcuts import redirect, render, HttpResponse
from tuition.forms import ContactForm, PostForm
from tuition.models import Post

# Create your views here.


def search(request):
    if request.method == "POST":
        query = request.POST['search']
        mydata = Post.objects.filter(title__icontains=query).values()
    return render(request, 'search.html', {'results': mydata})


def home(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


def details(request, id):
    details = Post.objects.get(id=id)
    return render(request, 'details.html', {'member': details})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/home/')
    else:
        form = ContactForm()
        return render(request, 'contact.html', {'form': form})


def postView(request):
    if request.method == 'POST':
        post = PostForm(data=request.POST, files=request.FILES)
        if post.is_valid():
            post.save()
        return redirect('/posts/')

    else:
        post = PostForm()
        return render(request, 'posts.html', {'post': post})
