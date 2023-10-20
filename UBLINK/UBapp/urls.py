from django.urls import path 
from UBapp.views import calculate_api_view_incomes,calculate_api_view_spents,combined_data,generate_pdf,IncomeApiView,Login_Logout,PersonApiView,UserApiView,SpentApiView
from rest_framework.documentation import include_docs_urls
urlpatterns = [
    path('user/', UserApiView.UserAPIView.as_view(), name='UserView' ),
    path('user/<int:pk>/', UserApiView.UserAPIView.as_view(), name='UserViewDetail'),
    path('person/',PersonApiView.PersonAPIView.as_view(),name = 'PersonApiView'),
    path('person/<int:pk>',PersonApiView.PersonAPIView.as_view(), name='PersonApiViewDetail'),
    path('spent/',SpentApiView.SpentAPIView.as_view(),name = 'SpentView'),
    path('spent/<int:pk>',SpentApiView.SpentAPIView.as_view(),name = 'SpentViewDetail'),
    path('income/', IncomeApiView.IncomeAPIView.as_view(), name = 'IncomeView'),
    path('income/<int:pk>',IncomeApiView.IncomeAPIView.as_view(), name = 'IncomeViewDetail'),
    path('docs/',include_docs_urls(title ='documentation'),name='docs'),
    path('subtotal/', calculate_api_view_spents.calculate_api_view_spents, name='subtotal_spent'),
    path('subtotal/<int:pk>/<str:date>', calculate_api_view_spents.calculate_api_view_spents, name='detail_spent'),
    path('total/',calculate_api_view_incomes.calculate_api_view_income, name='total_income'),
    path('total/<int:pk>/<str:date>/',calculate_api_view_incomes.calculate_api_view_income, name='detail_income'),
    path('combined_data/<int:pk>/<str:date>/',combined_data.CombinedDataView.as_view(), name='generate_pdf'),
    path('login/',Login_Logout.LoginView.as_view(), name='login'),
    path('logout/', Login_Logout.LogoutView.as_view(), name='logout'),
]