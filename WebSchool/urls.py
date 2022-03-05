"""WebSchool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

ar_models = [
  {
    "title": "Mars",
    "href": "https://console.echoar.xyz/webar?key=shiny-sky-7689&entry=92bdf20f-3655-4f7e-9780-2f01cc59d32f",
    "image": "Mars.png"
  },
  {
    "title": "Lungs",
    "href": "https://console.echoar.xyz/webar?key=shiny-sky-7689&entry=fc55f64c-7da1-46d9-8985-cd170f3f9b3b",
    "image": "Lungs.png"
  },
  {
    "title": "Sun",
    "href": "https://console.echoar.xyz/webar?key=shiny-sky-7689&entry=76dda169-a597-486a-aac4-65c5d8e1e682",
    "image": "Sun.png"
  },
  {
    "title": "Earth",
    "href": "https://console.echoar.xyz/webar?key=shiny-sky-7689&entry=04822cbd-84fe-4ab0-afe1-032b90df7d1f",
    "image": "Earth.png"
  },
  {
    "title": "Pyramid",
    "href": "https://console.echoar.xyz/webar?key=snowy-firefly-0544&entry=41c23aa9-9b5e-4fff-90d6-e0539198579c",
    "image": "Pyramid.png"
  },
  {
    "title": "Solar System",
    "href": "https://go.echoar.xyz/KeLN",
    "image": "SolarSystem.png"
  },
  {
    "title": "Space Needle",
    "href": "https://console.echoar.xyz/webar?key=snowy-firefly-0544&entry=25de17ce-56ea-40db-aa88-68371a257827",
    "image": "Space Needle.png"
  },
  {
    "title": "Eiffel Tower",
    "href": "https://console.echoar.xyz/webar?key=shiny-sky-7689&entry=92b7cf4a-ee63-49b3-852f-186dec0bdb89",
    "image": "Eiffel.png"
  },
  {
    "title": "Colosseum",
    "href": "https://console.echoar.xyz/webar?key=shiny-sky-7689&entry=e96e9c40-0c90-4929-8186-b24af025e0e8",
    "image": "Colosseum.png"
  },
  {
    "title": "T-Rex",
    "href": "https://console.echoar.xyz/webar?key=shiny-sky-7689&entry=2d402140-4cfa-4cd6-a930-c12eb4a84f81",
    "image": "TREX.png"
  },
  {
    "title": "Bohr's model of atom",
    "href": "https://console.echoar.xyz/webar?key=shiny-sky-7689&entry=e3b8a12e-c31a-4d43-9a48-8c9136522808",
    "image": "Bohr.png"
  },
  {
    "title": "Rutherford's model of atom",
    "href": "https://console.echoar.xyz/webar?key=shiny-sky-7689&entry=7f407769-47e1-41c1-9f30-0b89c76e5c33",
    "image": "Rutherford.png"
  },
  {
    "title": "DNA",
    "href": "https://console.echoar.xyz/webar?key=shiny-sky-7689&entry=4bb99a57-7f96-4598-b68d-ab254b992c2e",
    "image": "DNA.png"
  },
  {
    "title": "Heart",
    "href": "https://console.echoar.xyz/webar?key=shiny-sky-7689&entry=7d3bef97-14c8-462c-aec6-de6532262611",
    "image": "Heart.png"
  },
  {
    "title": "HIV",
    "href": "https://console.echoar.xyz/webar?key=shiny-sky-7689&entry=41ca98cd-2f51-4523-8439-02ffe6661446",
    "image": "HIV.png"
  },
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/',include('posts.urls')),
    path('homework/',include('homework.urls')),
    path('notes/',include('notes.urls')),
    path('classes/',include('classes.urls')),
    path('formsuccess/',TemplateView.as_view(template_name='backend/form_success.html'), name="formsuccess"),
    path('',include('user.urls')),
    path('',RedirectView.as_view(url='/posts/'), name='index'),
    path('ar/', TemplateView.as_view(template_name='backend/arpage.html', extra_context={"models": ar_models}), name='ar'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
