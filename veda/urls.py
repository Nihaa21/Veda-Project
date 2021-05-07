
from django.urls import path,include
from .views import Blog,Blog_detail_view, Add_Post_view, Update_post_view, Delete_post_view,Add_Category_view,CategoryView,home,portrait_page,Add_Photo_view,landscape_page,food_page,email_list_signup
from . import views


urlpatterns = [
 path('',home.as_view(),name="home"),
 path('Blog/',Blog.as_view(),name="Blog"),
 path('post/<int:pk>',Blog_detail_view.as_view(),name="blog_details"),
 path('Add_Post/',Add_Post_view.as_view(),name="add_Post"),
 path('blog/edit/<int:pk>',Update_post_view.as_view(),name="update_Post"),
 path('blog/delete_post/<int:pk>',Delete_post_view.as_view(),name="delete_Post"),
 path('add_category/',Add_Category_view.as_view(),name="add_category"),
 path('category/<str:cats>/',CategoryView,name="category"),




 path('about',views.about,name="about"),
 path('films',views.films,name="films"),

 path('photography',views.photography,name="photography"),
 path('portraits/',portrait_page.as_view(),name="portrait_page"),
 path('landscape/',landscape_page.as_view(),name="landscape_page"),
 path('food/',food_page.as_view(),name="food_page"),
 path('add_Photo/',Add_Photo_view.as_view(),name="add_Photo"),


 path('contact',views.contact,name="contact"),
 path('subscribe/',views.email_list_signup,name="subscribe"),

]
