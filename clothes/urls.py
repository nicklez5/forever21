from django.urls import path,include
from . import views
urlpatterns=[
    path('men_shirts/',views.menshirts,name="MenShirt"),
    path('men_shirts/<int:id>/',views.menshirt,name="MenShirt"),
    path('men_jackets/',views.menjackets,name="MenJackets"),
    path('men_jackets/<int:id>/',views.menjacket,name="MenJacket"),
    path('men_pants/',views.menpants,name="MenPants"),
    path('men_pants/<int:id>/',views.menpant,name="MenPant"),
    path('men_joggers/',views.menjoggers,name="MenJoggers"),
    path('men_joggers/<int:id>',views.menjogger,name="MenJogger"),
    path('glasses/',views.glasses,name="Glasses"),
    path('glasses/<int:id>/',views.glass,name="Glass"),
    path('earring/',views.earrings,name="Earrings"),
    path('earring/<int:id>',views.earring,name="Earring"),
    path('necklace/',views.necklaces,name="Necklaces"),
    path('necklace/<int:id>', views.necklace,name="Necklace"),
    path('women_shirts/',views.womenshirts,name="WomenShirts"),
    path('women_shirts/<int:id>',views.womenshirt,name="WomenShirt"),
    path('women_jackets/',views.womenjackets,name="WomenJackets"),
    path('women_jackets/<int:id>',views.womenjacket,name="WomenJacket"),
    path('women_pants/',views.womenpants,name="WomenPants"),
    path('women_pants/<int:id>',views.womenpant,name="WomenPant"),
    path('women_joggers/',views.womenjoggers,name="WomenJoggers"),
    path('women_joggers/<int:id>',views.womenjogger,name="WomenJogger"),
    path('carts/',views.carts,name="Carts"),
    path('cart/',views.cart,name="Cart")
]