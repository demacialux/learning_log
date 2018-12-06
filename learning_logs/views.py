from django.shortcuts import render
from .models import Topic
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import TopicForm

# Create your views here.
def index(request):
    """学习笔记的主页"""
    return render(request,'learning_logs/index.html')

def topics(request):
    """显示所有主题"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request,'learning_logs/topics.html',context)

def topic(request,topic_id):  #该函数接受正则表达式(?P<topic_id>\d+)捕捉的值，并存储到topic_id
    """显示单个主题及其所有的条目"""
    topic = Topic.objects.get(id=topic_id)  #获取指定的主题
    entries = topic.entry_set.order_by('-date_added')  #获取与该主题相关联的条目并按降序排列
    context = {'topic':topic,'entries':entries}  #将主题和条目存储于字典context
    return render(request,'learning_logs/topic.html',context)  #将字典发送给接下来的模板topic.html

def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        #未能提交数据：创建一个新表单
        form = TopicForm()
    
    else:
        #POST提交的数据，对数据进行处理
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    context = {'form':form}
    return render(request,'learning_logs/new_topic.html',context)