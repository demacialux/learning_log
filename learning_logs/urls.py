from django.urls import path
from . import views # 导入views

app_name = 'learning_logs'
urlpatterns = [
    #主页
    path('',views.index,name='index'),   

    #显示所有的主题
    path('topics',views.topics,name='topics'),

    #特定主题的详细界面
    path('topics/(?P<topic_id>\d+)',views.topic,name='topic'),  #使用正则表达式匹配URL

    path('new_topics',views.new_topic,name='new_topic'),
]