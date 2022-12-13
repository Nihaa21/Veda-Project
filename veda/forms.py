from django import forms
from .models import Post,Category,PotographyPost,Signup

# choices=[('Travel','Travel'),('Food','Food'),('Fitness','Fitness')]
choices=Category.objects.all().values_list('name','name')

choice_list=[]
for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','category','body','Blog_cover_image','Blog_post_image_1','Blog_post_image_2','Blog_post_image_3','Blog_post_image_4','Blog_post_image_5','Blog_post_image_6')

        widgets={
        'title':forms.TextInput(attrs={'class':'form-control'}),
        'category':forms.TextInput(attrs={'class':'form-control'}),
        'body':forms.Textarea(attrs={'class':'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title' ,'category','body','Blog_cover_image','Blog_post_image_1','Blog_post_image_2','Blog_post_image_3','Blog_post_image_4','Blog_post_image_5','Blog_post_image_6')

        widgets={
        'title':forms.TextInput(attrs={'class':'form-control'}),
        # 'title_tag':forms.TextInput(attrs={'class':'form-control'}),
        'category':forms.TextInput(attrs={'class':'form-control'}),
        # 'author':forms.Select(attrs={'class':'form-control'}),
        'body':forms.Textarea(attrs={'class':'form-control'}),
        }

class PhotoForm(forms.ModelForm):
    class Meta:
        model=PotographyPost
        fields=('portrait_image','landscape_image','food_image')


class EmailSignupForm(forms.ModelForm):
    email=forms.EmailField(widget=forms.TextInput(attrs={
    "type":"email",
    "name":"email",
    "placeholder":"Type Your Email"
    }

    ),label="")
    class Meta:
        model=Signup
        fields = ('email',)
