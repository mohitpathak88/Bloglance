from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin 
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post

def home(request):             #function based views
    context = {
        'posts': Post.objects.all()         #class based views- they have a lot of functionality that handles a lot of backend logic for us
    }
    return render(request, 'myblog/home.html', context)


class PostListView(ListView):
    model = Post                             #model is a variable which tells the listview what model to query in order to create the list. In this case, we wamt to list all our posts
    template_name = 'myblog/home.html'        #By creating the list view, the class by default look into this path -> <app>/<model>_<modeltype>.html <- Therefore we need to change the path
    context_object_name = 'posts'           #'posts' would be a variable that will loop over all the items in the template 
    ordering = ['-date_posted']             #Changes the order of the list, with recent post on the top


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):       #LoginRequiredMixin is used to confirm whether the user is logged in before creating a new post
    model = Post
    fields = ['title', 'content']                           
                                                            # template that it will use <model>_<modeltype>.html
    def form_valid(self, form):
        form.instance.author = self.request.user        #it will set the author of the post to the current logged in user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):           #Same template as create view
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def  test_func(self):               #To make sure only author gets to update a post
        post =  self.get_object()           #to get the post that we are currently updating
        if self.request.user == post.author:        #self.request.user gets the current logged in user and checks if the author is same
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):      #template used- post_confirm_delete.html        
    model = Post
    success_url = '/'   
    
    def  test_func(self):
        post =  self.get_object()
        if self.request.user == post.author:
            return True
        return False



def about(request):
    return render(request, 'myblog/about.html', {'title': 'About'})




