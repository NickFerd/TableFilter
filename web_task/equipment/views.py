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
        # Drop all filters
        form = DurationFilterForm()
        query = Duration.objects.all().order_by('start')
        link_querystring = ''
    else:
        query = Duration.objects.all().order_by('start')
        form = DurationFilterForm(request.GET)
        if form.is_valid():
            # Apply filters
            if form.cleaned_data['client'] and '-100' not in form.cleaned_data['client']:
                query = query.filter(client_id__in=form.cleaned_data['client'])

            if form.cleaned_data['mode'] and '-100' not in form.cleaned_data['mode']:
                query = query.filter(mode_id__in=form.cleaned_data['mode'])

            if form.cleaned_data['equip'] and '-100' not in form.cleaned_data['equip']:
                query = query.filter(equipment_id__in=form.cleaned_data['equip'])

            if form.cleaned_data['duration']:
                query = query.filter(minutes=form.cleaned_data['duration'])

            if form.cleaned_data['start_date']:
                query = query.filter(start__date=form.cleaned_data['start_date'])

            if form.cleaned_data['stop_date']:
                query = query.filter(stop__date=form.cleaned_data['stop_date'])

            if form.cleaned_data['start_hour']:
                query = query.filter(start__time=form.cleaned_data['start_hour'])

            if form.cleaned_data['stop_hour']:
                query = query.filter(stop__time=form.cleaned_data['stop_hour'])


            #print(query)
            # Manage pagination with set filters
            q = request.GET.copy()
            try:
                q.pop('page')
            except KeyError:
                pass
            link_querystring = q.urlencode()

    page_obj = paginate(query, request)
    context = {'form': form, 'page_obj': page_obj, 'link_querystring': link_querystring}
    return render(request, 'equipment/index.html', context)
