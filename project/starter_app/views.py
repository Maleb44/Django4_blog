from django.shortcuts import render
# from .models import Message
from .models import Post

from django.utils import timezone
from operator import itemgetter
from django.utils.text import slugify

import datetime
import os 
import sqlite3
from forms import PostForm
db_titel = []

def db_read():
    all_entries = Post.objects.order_by('-date').all()
    db_titel_1 =  []
    print 'Post reading'
    for row in all_entries:
        db_titel_1.append({'title':row.title,'slug':row.slug,'content':row.content,'date':row.date})
    return db_titel_1
# db_titel = db_read()

def look(slug):
    
    db_titel = db_read()
    item={}

    for item in db_titel:
        print item
        if item["slug"] == slug:
            return item

def home(request):
    db_titel = db_read()
    context_dict  = {'messages' : db_titel}
    return render(request, 'starter_app/blog.html',context_dict)


def post_detail(request,slug):
    post_detail = {}
    post_detail = Post.objects.get(slug=slug)
    #post_detail = look(slug)
   #print post_detail

    #dat_str = post_detail['date'][0:10]
    #post_detail.update({'date': dat_str}) 
    #if not post_detail:
    #    return render (request,'starter_app/blog.html',{})
      
    context_dict  = {'pos' : post_detail}
    return render (request,'starter_app/post_detail.html',
        context_dict)    
    
def post_new(request): 
        
    post = PostForm
    sent = False
    if request.method == 'POST':        # Form was submitted   
        form = PostForm(request.POST)      
        if form.is_valid():
        ###           # Form fields passed validation 
            cd = form.cleaned_data 
            post.date = datetime.datetime.now().isoformat()  
           # post.date = datetime.datetime.utcnow().isoformat()               
            elem = {'title': cd['title'],'slug':slugify(cd['title']),
         
            'content':cd['content'],'date':post.date }
            t1 = elem['title']
            t2 = elem ['slug']
            t3 = elem ['content']
            t4 = elem ['date']
            b = Post(title=t1, slug=t2, content=t3, date=t4)
            b.save()
          
            sent =True
    else:
        form = PostForm()
    return render(request, 'starter_app/post_new.html', 
            {'post': post,'form': form,'sent': sent})   
    


def post_list(request):
    db_titel = db_read()
    context_dict  = {'messages' : db_titel}
    return render(request,'starter_app/post_list.html',context_dict)
def post_menu_d(request,slug):
    db_titel = db_read()
    post_detail = {}
    post_detail = look(slug)

    right = {'post_t': post_detail}
    context_dict  = {'messages' : db_titel}
    context_dict.update(right)
    return render(request,'starter_app/total.html',context_dict)
def post_menu(request):
    db_titel = db_read()
    right = {'post_t': db_titel[0]}
    context_dict  = {'messages' : db_titel}
    context_dict.update(right)
    return render(request,'starter_app/total.html',context_dict)