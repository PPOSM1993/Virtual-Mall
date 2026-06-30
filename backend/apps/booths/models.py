from django.db import models
from django.utils.text import slugify


class Booth(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, blank=True)

    description = models.TextField(blank=True)

    company = models.ForeignKey(
        "companies.Company",
        on_delete=models.CASCADE,
        related_name="booths"
    )

    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="booths"
    )

    is_active = models.BooleanField(default=True)

    # ubicación dentro del mall (útil para frontend tipo mapa/grid)
    position_x = models.IntegerField(default=0)
    position_y = models.IntegerField(default=0)

    # visual / branding
    banner_url = models.URLField(blank=True, null=True)
    logo_url = models.URLField(blank=True, null=True)

    # metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["position_x", "position_y"]
        unique_together = ("company", "name")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.company.name}"