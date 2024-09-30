from django.shortcuts import render
from django.views.generic import TemplateView
from dashboard.utils.constants import DASHBOARD_TEMPLATE


class DashboardView(TemplateView):
    template_name = DASHBOARD_TEMPLATE
