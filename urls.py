from django.urls import path
from . import views

# ...existing code...

urlpatterns = [
    # ...existing code...
    path('ai-analysis/', views.ai_analysis, name='ai_analysis'),
    path('health-education/', views.health_education, name='health_education'),
    path('nutrition/', views.nutrition, name='nutrition'),
    path('exercise/', views.exercise, name='exercise'),
    path('mental-health/', views.mental_health, name='mental_health'),
    path('general-health-issues/', views.general_health_issues, name='general_health_issues'),
    path('common-cold/', views.common_cold, name='common_cold'),
    path('flu/', views.flu, name='flu'),
    path('burns/', views.burns, name='burns'),
    # ...existing code...
]

# ...existing code...
