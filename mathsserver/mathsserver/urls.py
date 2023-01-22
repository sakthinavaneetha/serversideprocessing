from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns=[
    path('admin/',admin.site.urls),
    path('volofrectangulartank/',views.volumecalculation,name="volofrectangulartank"),
    path('',views.volumecalculation,name="volofrectangulartankroot")
]