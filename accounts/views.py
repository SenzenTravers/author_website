from datetime import date, datetime

from django.http import JsonResponse
from django.shortcuts import render
from django.views import generic, View

from accounts.models import Member


# Create your views here.
class Birthday(View):
    def get(self, request, *args, **kwargs):
        # TODO: get either date or user_id
        # Todo: later on, change for class BirthdayHandler(generic.View):
        # Get date from request, default to today if not provided
        date_param = request.GET.get('date') or request.POST.get('date')

        if date_param:
            try:
                query_date = datetime.strptime(date_param, '%Y-%m-%d').date()
            except ValueError:
                query_date = date.today()
        else:
            query_date = date.today()

        profiles = Member.objects.filter(birthday__isnull=False)
        data = [
            {
                'member_id': member.id if member else None,
                'member_username': member.username if member else None,
                'birthday': member.birthday.isoformat() if member.birthday else None
            }
            for member in profiles if member.birthday and member.birthday == query_date
        ]
        return JsonResponse({'members_birthdays': data, 'query_date': query_date.isoformat()})

    def post(self, request, *args, **kwargs):
        pass
