from django.urls import reverse
from django.test import Client, TestCase
from voiture_noire.models import DiscordProfile
from accounts.models import Member  


class LibraryTestCase(TestCase):
    fixtures = ["accounts.json", "archives.json", "voiture_noire.json"]

    def setUp(self):
        Member.objects.create_user("Mr NoAccounts", email="jeanbobdupont@mail.fr", password="motdepasse")

    ############### INDEX
    def test_voiture_noire_index_unlogged(self):
        # Unlogged users only see stories available to everyone.
        response = self.client.get(reverse("voiture_noire:index"))
        nb_of_returned_stories = response.context_data['object_list']
        visible_status = {story.visible for story in response.context_data['fics']}
        visible_everyone_status = {story.visible_not_member_only for story in response.context_data['fics']}
        
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(False, visible_status) 
        self.assertNotIn(False, visible_everyone_status) 
        self.assertEqual(2, len(nb_of_returned_stories))

    def test_voiture_noire_index_logged(self):
        # Logged users that don't have a profile on the Discord Server
        # still can see all Visible stories.
        # visible_not_member_only doesn't matter.
        test_client = Client()
        test_client.login(username="Mr NoAccounts", password="motdepasse")
        response = test_client.get(reverse("voiture_noire:index"))
        nb_of_returned_stories = response.context_data['object_list']
        visible_status = {story.visible for story in response.context_data['fics']}
        visible_everyone_status = {story.visible_not_member_only for story in response.context_data['fics']}

        self.assertEqual(2, len(visible_everyone_status))
        self.assertNotIn(False, visible_status) 
        self.assertEqual(response.status_code, 200)
        self.assertEqual(5, len(nb_of_returned_stories))

    def test_voiture_noire_author_can_see_non_visible_fic(self):
        # Author can see their non-visible fic
        test_client = Client()
        test_client.login(username="MrsDiscordMemberAndAuthor", password="hypatia")
        response = test_client.get(reverse("voiture_noire:index"))
        nb_of_returned_stories = response.context_data['object_list']
        visible_status = {story.visible for story in response.context_data['fics']}
        visible_everyone_status = {story.visible_not_member_only for story in response.context_data['fics']}

        self.assertEqual(2, len(visible_everyone_status))
        self.assertIn(False, visible_status) 
        self.assertEqual(response.status_code, 200)
        self.assertEqual(6, len(nb_of_returned_stories))


    ############### ACCESS SPECIFIC FIC
    def test_voiture_noire_unlogged_user_can_only_see_fic_visible_for_everyone(self):
        # Non-visible, non-visible by outsider story
        response = self.client.get(reverse("archives:story_read_mode", kwargs={'fic_id':31, 'number': 1}))
        self.assertEqual(response.status_code, 302)
        # Visible, non-visible by outsider story
        response = self.client.get(reverse("archives:story_read_mode", kwargs={'fic_id':30, 'number': 1}))
        self.assertEqual(response.status_code, 302)
        # Visible by everyone story
        response = self.client.get(reverse("archives:story_read_mode", kwargs={'fic_id':2, 'number': 1}))
        self.assertEqual(response.status_code, 200)

    def test_voiture_noire_logged_user_behaviour(self):
        test_client = Client()
        test_client.login(username="Mr NoAccounts", password="motdepasse")
        # Non-visible, non-visible by outsider story
        response = test_client.get(reverse("archives:story_read_mode", kwargs={'fic_id':31, 'number': 1}))
        self.assertEqual(response.status_code, 302)
        # Visible, non-visible by outsider story
        response = test_client.get(reverse("archives:story_read_mode", kwargs={'fic_id':30, 'number': 1}))
        self.assertEqual(response.status_code, 200)
        # Visible by everyone story
        response = test_client.get(reverse("archives:story_read_mode", kwargs={'fic_id':2, 'number': 1}))
        self.assertEqual(response.status_code, 200)

    def test_voiture_noire_author_can_see_non_visible_fic(self):
        test_client = Client()
        test_client.login(username="MrsDiscordMemberAndAuthor", password="hypatia")
        # Non-visible, non-visible by outsider story
        response = test_client.get(reverse("archives:story_read_mode", kwargs={'fic_id':31, 'number': 1}))
        self.assertEqual(response.status_code, 200)
        # Visible, non-visible by outsider story
        response = test_client.get(reverse("archives:story_read_mode", kwargs={'fic_id':30, 'number': 1}))
        self.assertEqual(response.status_code, 200)
        # Visible by everyone story
        response = test_client.get(reverse("archives:story_read_mode", kwargs={'fic_id':2, 'number': 1}))
        self.assertEqual(response.status_code, 200)

