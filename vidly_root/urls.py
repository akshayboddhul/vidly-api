from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),

    # For User Login
    path('api-auth/', include('rest_framework.urls')),

    # For JWT Token
    path('api/auth/', views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
