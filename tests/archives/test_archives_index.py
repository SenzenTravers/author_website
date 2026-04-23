from datetime import date, timedelta


from django.db.models import Q
from django.test import Client, TestCase
from django.urls import reverse
from voiture_noire.models import ExchangeParticipant
from accounts.models import Member
from archives.models import Author, PairingType, Story


class ArchivesIndexTestCase(TestCase):
    fixtures = ["accounts.json", "archives.json"]

    def setUp(self):
        Member.objects.create_user("LurkerOnly", email="luciedupont@mail.fr", password="motdepasse")
        tomorrow = date.today() + timedelta(days=1)
        Story.objects.create(
            author=Author.objects.get(nickname="Author2_Nickname"), story_date=tomorrow,
            story_title="Future Title", summary="Future Summary",
            rating="g", visibility="Everyone"
        )

    def test_voiture_noire_index_unlogged(self):
        # Unlogged users only see stories available to everyone.
        # Future stories are not displayed.
        response = self.client.get(reverse("voiture_noire:index"))
        fetched_stories = response.context_data['stories']
        visibility_status = {story.visibility for story in fetched_stories}
        count_relevant_stories = Story.objects.filter(
            Q(visibility='Everyone') & (Q(story_date__lte=date.today()))
        ).count()
        future_story = Story.objects.get(story_title="Future Title")
        
        self.assertEqual(response.status_code, 200)
        self.assertNotIn("Private", visibility_status) 
        self.assertNotIn("Members only", visibility_status) 
        self.assertIn("Everyone", visibility_status)
        self.assertEqual(len(fetched_stories), count_relevant_stories)
        self.assertNotIn(future_story, fetched_stories)

    def test_voiture_noire_index_logged(self):
        # Members see all available stories except the other's Private ones.
        # Future stories are not displayed.
        test_client = Client()
        test_client.login(username="LurkerOnly", password="motdepasse")

        response = test_client.get(reverse("voiture_noire:index"))
        fetched_stories = response.context_data['stories']
        visibility_status = {story.visibility for story in fetched_stories}
        user_id = Member.objects.get(username="LurkerOnly").id
        count_relevant_stories = Story.objects.filter(
            Q(author__member_id=user_id) | ((~Q(visibility='Private') & Q(story_date__lte=date.today())))
        ).count()
        future_story = Story.objects.get(story_title="Future Title")

        self.assertEqual(len(fetched_stories), count_relevant_stories)
        self.assertNotIn("Private", visibility_status) 
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(future_story, fetched_stories)

    def test_voiture_noire_author_can_see_their_private_fic(self):
        # Author can see their own private fic.
        # Their own future stories are displayed
        test_client = Client()
        test_client.login(username="Author2", password="hypatia7")

        response = test_client.get(reverse("voiture_noire:index"))
        fetched_stories = response.context_data['stories']
        visibility_status = {story.visibility for story in fetched_stories}

        user_id = Member.objects.get(username="Author2").id
        count_relevant_stories = Story.objects.filter(
            Q(author__member_id=user_id) | (~Q(visibility='Private') & Q(story_date__lte=date.today()))
        ).count()
        future_story = Story.objects.get(story_title="Future Title")

        self.assertEqual(len(fetched_stories), count_relevant_stories)
        self.assertIn("Private", visibility_status) 
        self.assertEqual(response.status_code, 200)
        self.assertIn(future_story, fetched_stories)
