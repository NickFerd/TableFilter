
from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Duration


def index(request):
    query = Duration.objects.all().order_by('start')
    paginator = Paginator(query, 40)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj}
    return render(request, 'equipment/index.html', context)



