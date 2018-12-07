from django.urls import path,re_path
from . import views # 导入views

app_name = 'learning_logs'
urlpatterns = [
    #主页
    path('',views.index,name='index'),   

    #显示所有的主题
    path('topics',views.topics,name='topics'),

    #特定主题的详细界面
    re_path(r'topics/(?P<topic_id>\d+)/$',views.topic,name='topic'),  

    #用于添加新主题的网页
    path('new_topics',views.new_topic,name='new_topic'),

    re_path(r'new_entry/(?P<topic_id>\d+)/$',views.new_entry,name='new_entry'),
]