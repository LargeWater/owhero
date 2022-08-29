import django_filters

from main_app.models import Hero

class HeroFilter(django_filters.FilterSet):
    class Meta:
        model = Hero
        fields = ['role']