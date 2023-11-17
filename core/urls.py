from django.urls import path
from .views import index, formulario, listar_curriculos, detalhes_curriculo, CurriculoListView
urlpatterns = [
    path('',index),
    path('formulario', formulario, name='formulario'),
    path('listar_curriculos', listar_curriculos, name='listar_curriculos'),
    path('curriculo/<int:pk>/', detalhes_curriculo, name='detalhes_curriculo'),
    path('curriculos/', CurriculoListView.as_view(), name='listar_curriculos'),
]
