from datetime import date, datetime

from django.http import JsonResponse
from django.shortcuts import render
from django.views import generic, View

from accounts.models import Member


class Birthday(View):
    def get(self, request, *args, **kwargs):
        date_param = request.GET.get('date')

        if date_param:
            try:
                query_date = datetime.strptime(date_param, '%Y-%m-%d').date()
            except ValueError:
                query_date = date.today()
        else:
            query_date = date.today()

        profiles = Member.objects.filter(birthday__isnull=False).exclude(discord_id="")
        data = [
            {'discord_ids': member.discord_id} for member in profiles
            if member.birthday.day == query_date.day and member.birthday.month == query_date.month
        ]
        return JsonResponse({'members_birthdays': data, 'query_date': query_date.isoformat()})

    def post(self, request, *args, **kwargs):
        date_param = request.POST.get('birthday')
        discord_id_param = request.POST.get('discord_id')

        if discord_id_param == '' or date_param == '':
            return JsonResponse(
            {'errorMsg': "Expecting a 'birthday' field (YYYY-MM-DD) and a 'discord_id' field."},
            status=400
        )

        try:
            query_date = datetime.strptime(date_param, '%Y-%m-%d').date()
        except:
            return JsonResponse(
            {'errorMsg': "Expecting a 'birthday' field (YYYY-MM-DD) and a 'discord_id' field."},
            status=400
        )

        try:
            member = Member.objects.get(discord_id=discord_id_param)
        except:
            return JsonResponse(
            {'errorMsg': "No member with that discord id."},
            status=404
        )

        birthday_person = Member.objects.get(discord_id=discord_id_param)
        birthday_person.birthday = datetime.strptime(date_param, '%Y-%m-%d').date()
        birthday_person.save()

        return JsonResponse({'errorMsg':""})