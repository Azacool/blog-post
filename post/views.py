from django.shortcuts import render
from .models import Post

def main(request):
    content={'content': [{'id':'2','title':'Giving Help','date':'10/12/2019','image':'images/giving_help.jpg'}]}
    return render(request,template_name='index.html',context=content)


