from django.urls import path

from .views import index, curriculo_gley, curriculo_nat, curriculo_helo, curriculo_eliel, curriculo_glyc, formulario, listar_curriculos

urlpatterns = [
    path('',index),
    path('curriculo_gley',curriculo_gley),
    path('curriculo_nat',curriculo_nat),
    path('curriculo_helo',curriculo_helo),
    path('curriculo_eliel',curriculo_eliel),
    path('curriculo_glyc',curriculo_glyc),
    path('formulario', formulario, name='formulario'),
    path('listar_curriculos', listar_curriculos, name='listar_curriculos'),

]
