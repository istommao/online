"""src views."""
from django.views.generic import TemplateView


class IDCardView(TemplateView):

    template_name = 'app/idcard.html'


class CatBlogDemoView(TemplateView):

    template_name = 'app/catblog_demo.html'
