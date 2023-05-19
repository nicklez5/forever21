from django.urls import path,include
from . import views
urlpatterns=[
    path('men_shirts',views.MenShirtAPIView.as_view()),
    path('men_shirts/<int:id>/',views.MenShirtDetailAPIView.as_view()),
    path('men_jackets',views.MenJacketAPIView.as_view()),
    path('men_jackets/<int:id>/',views.MenJacketAPIView.as_view()),
    path('men_pants',views.MenPantsAPIView.as_view()),
    path('men_pants/<int:id>/',views.MenPantsDetailAPIView.as_view()),
    path('men_joggers',views.MenJoggersAPIView.as_view()),
    path('men_joggers/<int:id>',views.MenJoggersDetailAPIView.as_view()),
    path('glasses',views.GlassesAPIView.as_view()),
    path('glasses/<int:id>/',views.GlassesDetailAPIView.as_view()),
    path('earring',views.EarringAPIView.as_view()),
    path('earring/<int:id>',views.EarringDetailAPIView.as_view()),
    path('necklace',views.NecklaceAPIView.as_view()),
    path('necklace/<int:id>', views.NecklaceDetailAPIView.as_view()),
    path('women_shirts',views.Women_ShirtAPIView.as_view()),
    path('women_shirts/<int:id>',views.Women_ShirtDetailAPIView.as_view()),
    path('women_jackets',views.Women_JacketAPIView.as_view()),
    path('women_jackets/<int:id>',views.Women_JacketDetailAPIView.as_view()),
    path('women_pants',views.Women_PantsAPIView.as_view()),
    path('women_pants/<int:id>',views.Women_PantsDetailAPIView.as_view()),
    path('women_joggers',views.Women_JoggersAPIView.as_view()),
    path('women_joggers/<int:id>',views.Women_JoggersDetailAPIView.as_view()),
    path('cart',views.CartAPIView.as_view())
]