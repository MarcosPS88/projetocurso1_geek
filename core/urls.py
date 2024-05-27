from django.urls import path
from .views import index, contato, produto

urlpatterns = [
    path('', view=index, name='index'),
    path('contato/', view=contato, name='contato'),
    path('produto/<int:produto_id>/', view=produto, name='produto')
]

