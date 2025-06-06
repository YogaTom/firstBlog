"""
Django settings for tom_blog project.

Generated by 'django-admin startproject' using Django 5.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import os
from pathlib import Path
import logging
from logging.handlers import TimedRotatingFileHandler

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2p@qfe_n&7)r!=k$eh=b@1*2r85a)xip7ghi^b@4_ia=g%)xcf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ['*']

# 静态文件收集目录
STATIC_ROOT = os.path.join(BASE_DIR, 'collected_static')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'password_reset',
    'DevOps',
    'userprofile',
    'taggit',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tom_blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [],
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'tom_blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        "ENGINE": "django.db.backends.mysql",
        "NAME": "",   
        "USER": "",
        "PASSWORD": "", 
        "HOST": "",
        "PORT": "",
    } 
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# SMTP服务器，改为你的邮箱的smtp!
EMAIL_HOST = 'smtp.163.com'
# 改为你自己的邮箱名！
EMAIL_HOST_USER = ''
# 你的邮箱密码
EMAIL_HOST_PASSWORD = ''
# 发送邮件的端口
EMAIL_PORT = 25
# 是否使用 TLS
EMAIL_USE_TLS = True
# 默认的发件人
DEFAULT_FROM_EMAIL = 'TOM的博客 <yogatom@163.com>'

# 媒体文件地址
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# 自动创建日志目录
LOG_DIR = os.path.join(BASE_DIR, 'logs')
os.makedirs(LOG_DIR, exist_ok=True)
'''
TimedRotatingFileHandler: 每天生成一个日志文件，保留30天。
encoding: 'utf-8': 避免中文乱码。
verbose 格式带有时间、级别、模块名、行号等，方便排查问题。
django.request 专门处理 HTTP 错误（如 500 错误）。
添加了 console 处理器，便于开发调试。
'''
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    
    # 格式定义
    'formatters': {
        'verbose': {
            'format': '[{asctime}] {levelname} [{name}:{lineno}] {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    
    # 处理器
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'simple',
        },
        'info_file': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'info.log'),
            'when': 'midnight',
            'backupCount': 30,
            'level': 'INFO',
            'formatter': 'verbose',
            'encoding': 'utf-8',
        },
        'error_file': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'error.log'),
            'when': 'midnight',
            'backupCount': 30,
            'level': 'ERROR',
            'formatter': 'verbose',
            'encoding': 'utf-8',
        },
    },
    
    # 日志记录器
    'loggers': {
        'django': {
            'handlers': ['console', 'info_file', 'error_file'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console', 'error_file'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
}
