from django.urls import path
from .views import blglst, blgdl, mblg, crtblg, delblg, updblg

urlpatterns = [
    path('blog/list', blglst ),
    path('blog/det<int:id>', blgdl),
    path('create', crtblg),
    path('delete/int:id>', delblg),
    path('update/<int:id>', updblg),
    path('my/blog/', mblg)
]
