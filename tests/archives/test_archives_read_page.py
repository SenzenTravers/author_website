from datetime import date, timedelta


from django.db.models import Q
from django.test import Client, TestCase
from django.urls import reverse
from voiture_noire.models import DiscordProfile
from accounts.models import Member
from archives.models import Author, PairingType, Story


class ArchivesReadPageTestCase(TestCase):
    fixtures = ["accounts.json", "archives.json"]

    def setUp(self):
        pass

    def test_voiture_noire_unlogged_user_can_only_see_fic_visible_for_everyone(self):
        # Non-visible, non-visible by outsider story
        response = self.client.get(reverse("archives:read_story", kwargs={'story_id':31, 'chapter_number': 1}))
        self.assertEqual(response.status_code, 302)
        # Visible, non-visible by outsider story
        response = self.client.get(reverse("archives:read_story", kwargs={'story_id':30, 'chapter_number': 1}))
        self.assertEqual(response.status_code, 302)
        # Visible by everyone story
        response = self.client.get(reverse("archives:read_story", kwargs={'story_id':2, 'chapter_number': 1}))
        self.assertEqual(response.status_code, 200)

    def test_voiture_noire_logged_user_behaviour(self):
        test_client = Client()
        test_client.login(username="Mr NoAccounts", password="motdepasse")
        # Non-visible, non-visible by outsider story
        response = test_client.get(reverse("archives:read_story", kwargs={'story_id':31, 'chapter_number': 1}))
        self.assertEqual(response.status_code, 302)
        # Visible, non-visible by outsider story
        response = test_client.get(reverse("archives:read_story", kwargs={'story_id':30, 'chapter_number': 1}))
        self.assertEqual(response.status_code, 200)
        # Visible by everyone story
        response = test_client.get(reverse("archives:read_story", kwargs={'story_id':2, 'chapter_number': 1}))
        self.assertEqual(response.status_code, 200)

    def test_voiture_noire_author_can_see_non_visible_fic(self):
        test_client = Client()
        test_client.login(username="MrsDiscordMemberAndAuthor", password="hypatia")
        # Non-visible, non-visible by outsider story
        response = test_client.get(reverse("archives:read_story", kwargs={'story_id':31, 'chapter_number': 1}))
        self.assertEqual(response.status_code, 200)
        # Visible, non-visible by outsider story
        response = test_client.get(reverse("archives:read_story", kwargs={'story_id':30, 'chapter_number': 1}))
        self.assertEqual(response.status_code, 200)
        # Visible by everyone story
        response = test_client.get(reverse("archives:read_story", kwargs={'story_id':2, 'chapter_number': 1}))
        self.assertEqual(response.status_code, 200)

