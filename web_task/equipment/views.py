
from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Duration
from .forms import DurationFilterForm


def paginate(queryset, request):
    paginator = Paginator(queryset, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


def index(request):
    if request.method == 'POST':
        form = DurationFilterForm()
        query = Duration.objects.all().order_by('start')
        link_querystring = ''
    else:
        query = Duration.objects.all().order_by('start')
        form = DurationFilterForm(request.GET)
        if form.is_valid():
            # Filter query according to params
            if form.cleaned_data['client'] and form.cleaned_data['client'] != -100:
                query = query.filter(client_id__in=form.cleaned_data['client'])

            if form.cleaned_data['mode'] and form.cleaned_data['mode'] != -100:
                query = query.filter(mode_id__in=form.cleaned_data['mode'])

            if form.cleaned_data['equip'] and form.cleaned_data['equip'] != -100:
                query = query.filter(equipment_id__in=form.cleaned_data['equip'])

            # time management
            if form.cleaned_data['start_date']:
                query = query.filter(start=form.cleaned_data['start_date'])

            q = request.GET.copy()
            try:
                q.pop('page')
            except KeyError:
                pass
            link_querystring = q.urlencode()

    page_obj = paginate(query, request)
    context = {'form': form, 'page_obj': page_obj, 'link_querystring': link_querystring}
    return render(request, 'equipment/index.html', context)



