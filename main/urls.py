from django.urls import path
from .views import *


urlpatterns = [
    path('', Home),
    path('blog/', Blogs),
    path('product/<int:pk>/', ProductDetail.as_view()),
    path('addtocart/<int:id>/', AddToCart, name='addtocart'),
    path('about/', About),
    path('cart/', Cart),
    path('buyurtmaberish/<int:id>/', BuyurtmaBerish),
    path('count-savatcha/', CountSavatcha),
    
    path('deletecart/<int:id>/', DeleteCart),
]