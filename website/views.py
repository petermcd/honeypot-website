from django.views import generic

from .models import Setting


class SettingView(generic.ListView):
    template_name = 'website/main.html'

    def get_queryset(self):
        return Setting.objects.all().order_by('name')
