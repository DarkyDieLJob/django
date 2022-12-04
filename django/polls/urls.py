from django.urls import path

urlpatterns = [
    path('polls/',include('polls.urls')),
    path('abaut/',views.abaut),
]