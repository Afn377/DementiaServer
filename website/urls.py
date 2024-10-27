"""website URL Configuration

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
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from main.views import SignupView
from main.views import RandomPictureView
from main.views import SentenceSimilarityView
from main.views import UserProfileView
from main.views import UpdateUserScoreView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('django.contrib.auth.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/signup/', SignupView.as_view(), name='signup'), 
    path('api/random-pictures/', RandomPictureView.as_view(), name='random-pictures'),
    path('api/similarity/', SentenceSimilarityView.as_view(), name='sentence_similarity'),
    path('api/user/<str:username>/', UserProfileView.as_view(), name='user-profile'),
    path('api/update-score/', UpdateUserScoreView.as_view(), name='update_user_score'),

]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:  # Only serve media files in debug mode
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
