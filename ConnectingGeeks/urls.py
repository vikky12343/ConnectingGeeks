"""ConnectingGeeks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""



from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static





from social.views import home,register,loginpage,signup,loginup,logout,HomeView,EntryView,post,CreateEntryView,CreateView,QuestionHomeView,QuestionView,question_post,PostEditView,PostDeleteView,profile
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home),
    path('web_sign',signup),
    path('web_login',loginup),
    path('register/',register),
    path('login/',loginpage),
    path('accounts/login/',loginpage),
    path('logout/',logout),
    path('entry/<int:pk>/edit/',PostEditView.as_view(success_url='/blog/'),name="post-edit"),
    path('entry/<int:pk>/remove/',PostDeleteView.as_view(success_url='/blog/'),name='post-delete'),
    path('blog/',HomeView.as_view(),name='blog_home'),
    path('entry/<int:pk>',EntryView.as_view(),name='entry_detail'),
    path('post/',CreateEntryView.as_view(success_url='/blog/'),name="create_entry"),
    path('ques/',QuestionHomeView.as_view(),name='question_detail'),
    path('question/<int:pk>',QuestionView.as_view(),name='question_detail'),
    path('question_submit/',question_post),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('profile/', profile),
    

    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
