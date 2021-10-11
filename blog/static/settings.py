"""
Django settings for whereabouts project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
print(Path(__file__).resolve().parent.parent)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-w%4w%z+qltqre4c$=1v#hf(fe@#bs_yk(4l&u-4km5zs8h(5w$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'django_summernote',
    'blog.apps.BlogConfig',
    'simpleui',
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

ROOT_URLCONF = 'whereabouts.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # 可供添加自定义HTML文件,
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

WSGI_APPLICATION = 'whereabouts.wsgi.application'

# summernote富文本编辑器相关配置
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
X_FRAME_OPTIONS = 'SAMEORIGIN'

SUMMERNOTE_CONFIG = {
    # Or, you can set it to `False` to use SummernoteInplaceWidget by default - no iframe mode
    # In this case, you have to load Bootstrap/jQuery sources and dependencies manually.
    # Use this when you're already using Bootstrap/jQuery based themes.
    'iframe': False,

    # You can put custom Summernote settings
    'summernote': {
        # As an example, using Summernote Air-mode
        'airMode': False,

        # Change editor size
        'width': '100%',
        'height': '480',

        # Use proper language setting automatically (default)
        'lang': None,

        # Toolbar customization
        # https://summernote.org/deep-dive/#custom-toolbar-popover
        'toolbar': [
            ['style', ['style']],
            ['font', ['bold', 'underline', 'clear']],
            ['fontname', ['fontname']],
            ['color', ['color']],
            ['para', ['ul', 'ol', 'paragraph']],
            ['table', ['table']],
            ['insert', ['link', 'picture', 'video']],
            ['view', ['fullscreen', 'codeview', 'help']],
        ],

        # You can also add custom settings for external plugins
        'print': {
            'stylesheetUrl': '/some_static_folder/printable.css',
        },
        'codemirror': {
            'mode': 'htmlmixed',
            'lineNumbers': 'true',
            # You have to include theme file in 'css' or 'css_for_inplace' before using it.
            'theme': 'monokai',
        },
    },
}

# 富文本编辑器ckeditor的配置
CKEDITOR_CONFIGS = {
    # django-ckeditor默认使用default配置
    'default': {
        # 编辑器宽度自适应
        'width': 'auto',
        'height': '250px',
        # tab键转换空格数
        'tabSpaces': 4,
        # 工具栏风格
        'toolbar': 'Custom',
        # 工具栏按钮
        'toolbar_Custom': [
            # 表情 代码块
            ['Smiley', 'CodeSnippet'],
            # 字体风格
            ['Bold', 'Italic', 'Underline', 'RemoveFormat', 'Blockquote'],
            # 字体颜色
            ['TextColor', 'BGColor'],
            # 链接
            ['Link', 'Unlink'],
            # 列表
            ['NumberedList', 'BulletedList'],
            # 最大化
            ['Maximize']
        ],
        # 加入代码块插件
        'extraPlugins': ','.join(['codesnippet', 'widget', 'lineutils']),
    }
}

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 数据库引擎
        'NAME': 'test',  # 数据库名称
        'USER': 'tester',  # 链接数据库的用户名
        'PASSWORD': 'tester123',  # 链接数据库的密码
        'HOST': '127.0.0.1',  # mysql服务器的域名和ip地址
        'PORT': '3306',  # mysql的一个端口号,默认是3306
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

# Model指定用户定义UserInfo, 替换外键关键字配置
AUTH_USER_MODEL = "blog.UserInfo"
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# 文件系统默认配置
# https://docs.djangoproject.com/zh-hans/3.2/ref/settings/#staticfiles-finders
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]
# 静态文件的存放路径
# https://docs.djangoproject.com/zh-hans/3.2/ref/settings/#std:setting-STATICFILES_DIRS
# file path style : "C:/Users/user/mysite/extra_static_content"
STATICFILES_DIRS = [
    "whereabouts/",
]

# 日志配置文件
# LOG_ROOT = os.path.join(BASE_DIR, 'logs')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    # 消息处理引擎，可以定义多个以便处理不同级别信息
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'C:/Users/41999/Documents/projectmanagement/Test/Scripts/whereabouts/logs/debug.log',  # 注意，你的文件应该有读写权限。
            # 'maxBytes': '100 * 1024 * 1024',
            'encoding': 'utf-8',
        },
    },
    # 日志系统入口
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}


