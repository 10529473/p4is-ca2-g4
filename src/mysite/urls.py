"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings

from account.views import (
	registration_view,
	login_view,
	logout_view,
	account_view,
)

from product.views import print_product_list

urlpatterns = [
	# HACK: Redirect to product page
	path('', print_product_list, name='home'),

	path('admin/', admin.site.urls),
	
	# account views
	path('register/', registration_view, name='register'),
    path('account/', account_view, name='account'),
	path('login/', login_view, name='login'),
	path('logout/', logout_view, name='logout'),
	
	# product views
	path('product/', include('product.urls')),
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
