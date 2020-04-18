import calendar
import re
from datetime import date, datetime

from django.db.models import Q
from django_filters import rest_framework as filters

from .models import Timeline


class TimelineFilter(filters.FilterSet):
    date_range = filters.CharFilter(
        method='filter_month_range',
        label='date_range',
    )
    start_date = filters.DateFilter(field_name='start__date')
    stop_date = filters.DateFilter(field_name='stop__date')

    def filter_month_range(self, queryset, name, value):
        try:
            match = re.match(
                r'(?P<initial_year>\d{4})(-(?P<initial_month>\d{2}))?(-(?P<initial_day>\d{2}))?(_(?P<final_year>\d{4})(-(?P<final_month>\d{2}))?(-(?P<final_day>\d{2}))?)?',
                value,
            )
            if match is None:
                return queryset
            match = match.groupdict()
            range_values = {
                'initial_year': match['initial_year'],
                'initial_month': match['initial_month'] or '01',
                'initial_day': match['initial_month'] or '01',
            }
            range_values['final_year'] = match['final_year'] or range_values['initial_year']
            range_values['final_month'] =  match['final_month'] or '12'
            last_day_of_month = str(calendar.monthrange(
                int(range_values['final_year']),
                int(range_values['final_month']),
            )[1]).zfill(2)
            range_values['final_day'] =  match['final_day'] or last_day_of_month

            try:
                initial_date = datetime.strptime(
                    "{initial_year}-{initial_month}-{initial_day}".format(**range_values),
                    '%Y-%m-%d'
                ).date()
                final_date = datetime.strptime(
                    "{final_year}-{final_month}-{final_day}".format(**range_values),
                    '%Y-%m-%d'
                ).date()
            except:
                return queryset

            return queryset.filter(
                stop__date__lte=final_date,
                start__date__gte=initial_date,
            )
        except Exception as e:
            print(e)
            return queryset

    class Meta:
        model = Timeline
        fields = [
            'date_range',
            'user',
            'start_date',
            'stop_date',
        ]
