from django.http import JsonResponse
from django.shortcuts import render
from .models import FormTemplate
from .utils import validate_field, detect_field_type

def validate_form(request):
    if request.method == "POST":
        data = request.POST.dict()
        templates = FormTemplate.objects.all()

        for template in templates:
            valid = True
            for field_name, field_type in template.fields.items():
                if field_name not in data or not validate_field(data[field_name], field_type):
                    valid = False
                    break
            if valid:
                return JsonResponse({"template_name": template.name})

        # Если ни один шаблон не подошёл
        field_types = [
            (key, detect_field_type(value))
            for key, value in data.items()
        ]
        field_types_dict = dict(field_types)
        return JsonResponse(field_types_dict)
    return render(request, 'base.html')
