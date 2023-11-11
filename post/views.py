from django.shortcuts import render
from .models import Post

def main(request):
    #content1={'content': [{'id':'2','title':'giving help','date':'10/12/2019'}]}
    content=Post.objects.all()
    return render(request,template_name='index.html',context=content)


