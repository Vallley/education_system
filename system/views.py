from django.db.models import Count
from . import models
from django.views.generic import ListView


class ProductsList(ListView):
    model = models.Product
    template_name = "product.html"
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = models.Product.objects.annotate(lesson_count=Count("lesson"))

        context["products"] = products
        return context
    
class LessonsList(ListView):
    context_object_name = "lessons"

    def get_queryset(self):
        print(self.kwargs.get('id'))
        return models.Lesson.objects.filter(product_id=self.kwargs.get('id'))

    template_name = "lessons.html"
    
                

