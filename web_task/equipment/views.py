
from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Duration
from .forms import DurationFilterForm


def index(request):
    query = Duration.objects.all().order_by('start')
    form = DurationFilterForm(request.GET)
    if form.is_valid():
        if form.cleaned_data['start_date']:
            query = query.filter(start=form.cleaned_data['start_date'])

    paginator = Paginator(query, 40)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj, 'form': form}
    return render(request, 'equipment/index.html', context)



