from datetime import date
from django.test import TestCase
from django.urls import reverse
from accounts.models import Member


class AccountsBirthdaysTestCase(TestCase):
    def setUp(self):
        # Create 3 members
        # - One without birthdate
        self.member1 = Member.objects.create_user("user1", email="user1@test.com", password="pass", birthday=None)
        # - One with the requested birthdate (2024-12-25)
        self.member2 = Member.objects.create_user(
            "user2", email="user2@test.com", password="pass", birthday=date(2024, 12, 25)
        )
        # - One with a different birthdate
        self.member3 = Member.objects.create_user(
            "user3", email="user3@test.com", password="pass", birthday=date(2024, 6, 15)
        )

    def test_discord_profiles_birthdays_with_a_requesting_date(self):
        # Login as one of the members
        self.client.login(username="user1", password="pass")
        # Request with a specific date
        response = self.client.get(reverse('members:birthdays'), {'date': '2024-12-25'})
        
        self.assertEqual(response.status_code, 200)
        data = response.json()
        
        # Should only return the profile with the matching birthdate
        self.assertEqual(len(data['members_birthdays']), 1)
        self.assertEqual(data['members_birthdays'][0]['member_username'], 'user2')
        self.assertEqual(data['members_birthdays'][0]['birthday'], '2024-12-25')
        self.assertEqual(data['query_date'], '2024-12-25')

    def test_discord_profiles_birthdays_without_a_requesting_date(self):
        # Login as one of the members
        self.client.login(username="user1", password="pass")
        # Request without a specific date
        response = self.client.get(reverse('members:birthdays'), { })
        
        self.assertEqual(response.status_code, 200)
        data = response.json()
        
        # Should only return the profile with the matching birthdate
        self.assertEqual(len(data['members_birthdays']), 0) 
        self.assertEqual(data['query_date'], date.today().isoformat())