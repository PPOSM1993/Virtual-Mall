from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from drf_spectacular.utils import extend_schema_view, extend_schema

from .models import Category
from .serializers import CategorySerializer

@extend_schema_view(
    list=extend_schema(
        tags=["Categories"],
        summary="Listar categorías",
        description="Obtiene todas las categorías del mall para organizar booths y empresas.",
    ),
    retrieve=extend_schema(
        tags=["Categories"],
        summary="Detalle de categoría",
        description="Devuelve información de una categoría específica.",
    ),
    create=extend_schema(
        tags=["Categories"],
        summary="Crear categoría",
        description="Permite crear nuevas categorías para el mall.",
    ),
    update=extend_schema(
        tags=["Categories"],
        summary="Actualizar categoría completa",
    ),
    partial_update=extend_schema(
        tags=["Categories"],
        summary="Actualizar categoría parcialmente",
    ),
    destroy=extend_schema(
        tags=["Categories"],
        summary="Eliminar categoría",
    ),
)
class CategoryViewSet(viewsets.ModelViewSet):
    """
    ViewSet de Categories.

    Maneja la clasificación de booths y empresas dentro del mall virtual.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # 🔍 Filtros pro para frontend
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_fields = []  # por ahora simple, pero listo para crecer
    search_fields = [
        "name",
        "description",
    ]

    ordering_fields = [
        "name",
        "created_at",
    ]

    ordering = ["name"]