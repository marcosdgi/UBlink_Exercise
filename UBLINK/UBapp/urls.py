from django.urls import path 
from .views import UserAPIView, PersonAPIView, SpentAPIView, IncomeAPIView
from rest_framework.documentation import include_docs_urls
urlpatterns = [
    path('user/', UserAPIView.as_view(), name='UserView' ),
    path('user/<int:pk>/', UserAPIView.as_view(), name='UserViewDetail'),
    path('person/',PersonAPIView.as_view(),name = 'PersonApiView'),
    path('person/<int:pk>',PersonAPIView.as_view(), name='PersonApiViewDetail'),
    path('spent/',SpentAPIView.as_view(),name = 'SpentView'),
    path('spent/<int:pk>',SpentAPIView.as_view(),name = 'SpentViewDetail'),
    path('income/', IncomeAPIView.as_view(), name = 'IncomeView'),
    path('income/<int:pk>',IncomeAPIView.as_view(), name = 'IncomeViewDetail'),
    path('docs/',include_docs_urls(title ='documentation'),name='docs'),
]