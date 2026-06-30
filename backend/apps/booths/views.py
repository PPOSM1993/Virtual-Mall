from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from drf_spectacular.utils import extend_schema_view, extend_schema

from .models import Booth
from .serializers import BoothSerializer

@extend_schema_view(
    list=extend_schema(
        tags=["Booths"],
        summary="Listar booths del mall",
        description="Devuelve todos los booths disponibles con filtros, búsqueda y ordenamiento.",
    ),
    retrieve=extend_schema(
        tags=["Booths"],
        summary="Obtener detalle de un booth",
        description="Devuelve información completa de un booth específico por ID.",
    ),
    create=extend_schema(
        tags=["Booths"],
        summary="Crear nuevo booth",
        description="Crea un booth asociado a una empresa y categoría.",
    ),
    update=extend_schema(
        tags=["Booths"],
        summary="Actualizar booth completo",
    ),
    partial_update=extend_schema(
        tags=["Booths"],
        summary="Actualizar booth parcialmente",
    ),
    destroy=extend_schema(
        tags=["Booths"],
        summary="Eliminar booth",
    ),
)
class BoothViewSet(viewsets.ModelViewSet):
    """
    ViewSet principal de Booths.

    Maneja CRUD completo + filtros para el mall virtual.
    """

    queryset = Booth.objects.select_related(
        "company",
        "category"
    ).all()

    serializer_class = BoothSerializer

    # 🔍 Filtros tipo producto real
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_fields = [
        "company",
        "category",
        "is_active",
    ]

    search_fields = [
        "name",
        "description",
    ]

    ordering_fields = [
        "created_at",
        "position_x",
        "position_y",
        "name",
    ]

    ordering = ["position_x", "position_y"]