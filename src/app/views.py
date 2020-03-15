"""src views."""
from django.views.generic import TemplateView


class IDCardView(TemplateView):

    template_name = 'app/idcard.html'
