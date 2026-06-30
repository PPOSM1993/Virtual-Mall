from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from drf_spectacular.utils import extend_schema_view, extend_schema

from .models import Company
from .serializers import CompanySerializer


@extend_schema_view(
    list=extend_schema(
        tags=["Companies"],
        summary="Listar empresas del mall",
        description="Obtiene todas las empresas registradas en el sistema del mall virtual.",
    ),
    retrieve=extend_schema(
        tags=["Companies"],
        summary="Detalle de empresa",
        description="Devuelve información completa de una empresa específica.",
    ),
    create=extend_schema(
        tags=["Companies"],
        summary="Crear empresa",
        description="Registra una nueva empresa en el mall.",
    ),
    update=extend_schema(
        tags=["Companies"],
        summary="Actualizar empresa completa",
    ),
    partial_update=extend_schema(
        tags=["Companies"],
        summary="Actualizar empresa parcialmente",
    ),
    destroy=extend_schema(
        tags=["Companies"],
        summary="Eliminar empresa",
    ),
)
class CompanyViewSet(viewsets.ModelViewSet):
    """
    ViewSet de Companies.

    Representa las empresas que tienen presencia dentro del mall virtual
    y pueden tener uno o varios booths asociados.
    """

    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    # 🔍 Filtros tipo producto real
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_fields = [
        # si luego agregas campos como is_active, subscription, etc
    ]

    search_fields = [
        "name",
        "description",
    ]

    ordering_fields = [
        "name",
        "created_at",
    ]

    ordering = ["name"]