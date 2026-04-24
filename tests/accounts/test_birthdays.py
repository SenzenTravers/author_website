from datetime import date, timedelta
from django.test import TestCase
from django.urls import reverse
from accounts.models import Member


class AccountsBirthdaysTestCase(TestCase):
    def setUp(self):
        self.today = date.today()
        self.date_plus_ten = date.today() + timedelta(days=10)
        self.date_minus_ten = date.today() - timedelta(days=10)

        self.no_birthday = Member.objects.create_user(
            "no_birthday", email="no_birthday@test.com", password="pass", birthday=None,
            discord_id='17871183718936171'
        )
        self.has_requested_birthday = Member.objects.create_user(
            "has_requested_birthday", email="has_requested_birthday@test.com",
            password="pass", birthday=self.date_plus_ten,
            discord_id='17871183718936172'
        )
        self.has_requested_birthday_but_no_discord_ids = Member.objects.create_user(
            "has_requested_birthday_no_discord_id",
            email="has_requested_birthday_no_discord_id@test.com",
            password="pass", birthday=self.date_plus_ten
        )

        self.has_different_birthday = Member.objects.create_user(
            "has_different_birthday", email="has_different_birthday@test.com",
            password="pass", birthday=self.date_minus_ten,
            discord_id='17871183718936173'
        )
        self.has_today_birthday = Member.objects.create_user(
            "has_today_birthday", email="has_today_birthday@test.com",
            password="pass", birthday=date.today(),
            discord_id='17871183718936174'
        )

    ############################### GET
    def test_get_returns_users_matching_requesting_date_and_having_discord_ids(self):
        requested_date = self.date_plus_ten.isoformat()

        self.client.login(username="no_birthday", password="pass")
        response = self.client.get(reverse('members:birthdays'), {'date': requested_date})        
        data = response.json()
        
        # Should only return profile(s) with a matching birthday
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data['members_birthdays']), 1)
        self.assertEqual(data['query_date'], requested_date)

    def test_get_returns_empty_if_no_users_matches_requested_date(self):
        requested_date = date.today() - timedelta(days=20)
        requested_date = requested_date.isoformat()

        self.client.login(username="no_birthday", password="pass")
        response = self.client.get(reverse('members:birthdays'), {'date': requested_date})
        data = response.json()
        
        # Should only return profile(s) with a matching birthday
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data['members_birthdays']), 0) 
        self.assertEqual(data['query_date'], requested_date)

    def test_get_without_args_returns_members_born_today_date(self):
        self.client.login(username="no_birthday", password="pass")
        response = self.client.get(reverse('members:birthdays'), { })
        data = response.json()
        
        # Will return the member born on today's date
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data['members_birthdays']), 1) 
        self.assertEqual(data['query_date'], date.today().isoformat())

    ################################## POST
    def test_post_with_proper_birthday(self):
        birthday = date.today() - timedelta(days=20)
        birthday_iso = birthday.isoformat()


        self.client.login(username="no_birthday", password="pass")
        response = self.client.post(
            reverse('members:birthdays'),
            {'discord_id': '17871183718936171','birthday': birthday_iso}
        )
        members = Member.objects.filter(birthday__isnull=False).filter(discord_id__isnull=False)
        data = [
            {'discord_ids': member.discord_id} for member in members
            if member.birthday.day == birthday.day and member.birthday.month == birthday.month
        ]
        # Will return the member with a changed birthday
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 1) 
        self.assertEqual(data[0]['discord_ids'], '17871183718936171')

    def test_post_without_birthday(self):
        self.client.login(username="no_birthday", password="pass")
        response = self.client.post(
            reverse('members:birthdays'),
            {'discord_id': '17871183718936171'}
        )
        data = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            data['errorMsg'],
            "Expecting a 'birthday' field (YYYY-MM-DD) and a 'discord_id' field."
        )

    def test_post_with_birthday_no_matching_discord_id(self):
        birthday = date.today() - timedelta(days=20)
        birthday = birthday.isoformat()

        self.client.login(username="no_birthday", password="pass")
        response = self.client.post(
            reverse('members:birthdays'),
            {'discord_id': 'WRONG_DISCORD_ID','birthday': birthday}
        )
        data = response.json()

        self.assertEqual(response.status_code, 404)
        self.assertEqual(
            data['errorMsg'],
            "No member with that discord id."
        )
