from rest_framework import serializers
from .models import Booth


class BoothSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source="company.name", read_only=True)
    category_name = serializers.CharField(source="category.name", read_only=True)

    class Meta:
        model = Booth
        fields = [
            "id",
            "name",
            "slug",
            "description",
            "company",
            "company_name",
            "category",
            "category_name",
            "is_active",
            "position_x",
            "position_y",
            "banner_url",
            "logo_url",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["slug", "created_at", "updated_at"]