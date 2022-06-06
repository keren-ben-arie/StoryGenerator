"""StoryTeller URL Configuration

The `urlpatterns` list routes URLs to templates. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function templates
    1. Add an import:  from my_app import templates
    2. Add a URL to urlpatterns:  path('', templates.home, name='home')
Class-based templates
    1. Add an import:  from other_app.templates import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from StoryTeller.views.online_image_parser import OnlineSamplerView
from django.urls import path

urlpatterns = [
    path("", OnlineSamplerView.as_view(), name="index"),
    path("upload", OnlineSamplerView.post, name="upload"),

]

