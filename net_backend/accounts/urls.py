

#TokenObtainPairView-- which is used to obtain the token used by a user to login 
#TokenRefreshView -- which is used to Refresh the token 


from django.urls import path

from rest_framework_simplejwt.views import ( # i love simple jwt token for authentication processes
    TokenObtainPairView,
    TokenRefreshView,
)

from . import api

urlpatterns = [
    
    path('me/',api.me, name='me'),
    path('signup/', api.signup, name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('friends/<uuid:pk>/', api.friends, name='friends'),
    path('friends/<uuid:pk>/request/', api.friendly_request, name='friendlyrequest'),
    path('friends/<uuid:pk>/<str:status>/', api.handle_request, name='handle_request'),
]
