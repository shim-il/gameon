from django.urls import path

from . import views

urlpatterns = [
    path("", views.math_instructions_view, name = "math_instructions"),
    path("play_math/", views.play_math_view, name = "play_math")
    #path("<int:high_score>/update", views.update_score_view, name = "update_score")
]