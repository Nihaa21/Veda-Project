from django.shortcuts import render,redirect
from django.views.generic import DetailView,ListView,CreateView,UpdateView,DeleteView,View
from .models import Post,Category,PotographyPost,Signup
from .forms import PostForm,EditForm,PhotoForm,EmailSignupForm
from django.urls import reverse_lazy

from django.core.mail import send_mail
from django.conf import settings

from django.http import HttpResponseRedirect
from django.contrib import messages
import json
import requests

# Create your views here.
# def home(request):
#
#
#     return render(request,'veda/home.html', {})
class home(ListView):


    ordering=['-post_date'][:3]
    posts = Post.objects.all().order_by('-post_date')
    model = Post
    cats= Category.objects.all()
    template_name='veda/home.html'

    def get_context_data(self, *args, **kwargs):

        cat_menu = Category.objects.all()
        context = super(home, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        form = EmailSignupForm()
        return context




def about(request):
    cat_menu = Category.objects.all()
    return render(request,'veda/about.html',{'cat_menu':cat_menu})


def films(request):
    cat_menu = Category.objects.all()
    return render(request,'veda/films.html',{'cat_menu':cat_menu})



def contact(request):
    cat_menu = Category.objects.all()


    if request.method =="POST":

        name=request.POST['name']
        from_email=request.POST['from_email']
        message=request.POST['message']

        msg_mail = str(message) + "\n \nFrom - \n" + str(name.title()) + "\n" + "Email Id - " +str(from_email)
        send_mail(
            'Message from ' + name, #subject
             msg_mail, #msg
            from_email, #from
            ['nihaghali554@gmail.com'], #to
        )
        return render(request,'veda/contact.html',{'cat_menu':cat_menu,'name':name})
        # send_mail(subject= name,
        # message= message,
        # from_email=settings.DEFAULT_FROM_EMAIL,
        # recipient_list = [settings.EMAIL_HOST_USER],
        # fail_silently  = True,)

    else:
        return render(request,'veda/contact.html',{'cat_menu':cat_menu})

# def blog(request):
#     return render(request,'veda/blog.html')

class Blog(ListView):
    model = Post
    template_name='veda/blog.html'

    # to oder according to lastest at first
    ordering=['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(Blog, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class Blog_detail_view(DetailView):
    model = Post
    template_name='veda/blog_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(Blog_detail_view, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class Add_Post_view(CreateView):
    model = Post
    # bootstrap class to style form
    form_class=PostForm
    template_name='veda/add_post.html'
    # fields = ('title','title_tag','author','body')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(Add_Post_view, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class Add_Category_view(CreateView):
    model = Category
    # bootstrap class to style form
    # form_class=PostForm
    template_name='veda/add_category.html'
    fields ='__all__'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(Add_Category_view, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


def CategoryView(request,cats):
    category_post= Post.objects.filter(category=cats).order_by('-post_date')
    cat_menu = Category.objects.all()
    # model = Post
    # ordering=['-post_date']
    return render(request,'veda/categories.html',{'cats':cats.title(), 'category_post':category_post,'cat_menu':cat_menu})

    # def get_context_data(self, *args, **kwargs):
    #     cat_menu = Category.objects.all()
    #     context = super(Add_Category_view, self).get_context_data(*args, **kwargs)
    #     context["cat_menu"] = cat_menu
    #     return context

# class CategoryView(View):
#     model = Category
#     template_name='veda/categories.html'
#
#
#     def get(self,request,cats,*args, **kwargs):
#         # cats= Category.objects.all()
#         category_post= Post.objects.filter(category=cats)
#         return render(request,self.template_name,{'cats':cats, 'category_post':category_post})
#
#
#     def get_context_data(self,request, *args, **kwargs):
#         cat_menu = Category.objects.all()
#         context = super(CategoryView, self).get_context_data(*args, **kwargs)
#         context["cat_menu"] = cat_menu
#         return context



class Update_post_view(UpdateView):
    model = Post
    # bootstrap class to style form
    form_class=EditForm
    template_name='veda/update_post.html'
    # fields = ('title','title_tag','body')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(Update_post_view, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class Delete_post_view(DeleteView):
    model = Post
    template_name='veda/delete_post.html'
    success_url=reverse_lazy('Blog')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(Delete_post_view, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


def photography(request):
    cat_menu = Category.objects.all()
    return render(request,'veda/photography.html',{'cat_menu':cat_menu})

class portrait_page(ListView):
    model = PotographyPost
    template_name='veda/film_photography.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(portrait_page, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class landscape_page(ListView):
    model = PotographyPost
    template_name='veda/digital.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(landscape_page, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class food_page(ListView):
    model = PotographyPost
    template_name='veda/commissioned.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(food_page, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class Add_Photo_view(CreateView):
    model = PotographyPost
    # bootstrap class to style form
    form_class=PhotoForm
    template_name='veda/add_photo.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(Add_Photo_view, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

MAILCHIMP_API_KEY= settings.MAILCHIMP_API_KEY
MAILCHIMP_DATA_CENTER= settings.MAILCHIMP_DATA_CENTER
MAILCHIMP_EMAIL_LIST_ID= settings.MAILCHIMP_EMAIL_LIST_ID

api_url = f'https://{MAILCHIMP_DATA_CENTER}.api.mailchimp.com/3.0'
members_endpoint= f'{api_url}/lsits/{MAILCHIMP_EMAIL_LIST_ID}/members'


def subscribe(email):
    data={
    "email_address":email,
    "status":"subscribed"
    }
    r=request.post(
    members_endpoint,
    auth=("", MAILCHIMP_API_KEY),
    data=json.dumps(data)

    )
    return r.status_code , r.json()


def email_list_signup(request):
    form=EmailSignupForm(request.Post or None)
    if request.method == 'POST':
        if form.is_valid():
            email_signup_qs = Signup.objects.filter(email=form.instance.email)
            if email_signup_qs.exists():
                message.info(request,"You are already Subscribed!")
            else:
                subscribe(form.instance.email)
                form.save()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
