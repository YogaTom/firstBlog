from django.urls import path, include
# 引入views.py
from . import views

# 正在部署的应用的名称
app_name = 'DevOps'

urlpatterns = [
    # path函数将url映射到视图
    path('article-list/', views.article_list, name='article_list'),
    path('article-detail/<int:id>/', views.article_detail, name='article_detail'),
    path('article-create/', views.article_create, name='article_create'),
    path('article-update/<int:id>/', views.article_update, name='article_update'),
    # 安全删除文章
    path('article-safe-delete/<int:id>/', views.article_safe_delete, name='article_safe_delete'),
    path('password-reset/', include('password_reset.urls')),
]
