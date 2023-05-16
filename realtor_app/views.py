from django.shortcuts import render
from django.views import generic
from .models import Item, PROPERTY_TYPE

# Create your views here.

class PropertyList(generic.ListView):
    queryset = Item.objects.order_by("date_created")  # "-date_created" inverse order
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["properties"] = PROPERTY_TYPE
        return context


class PropertyDetails(generic.DetailView):
    model = Item
    template_name = "property_detail.html"

class AboutView(generic.TemplateView):
    template_name = "about.html"