from datetime import date
from random import choices

from django.db.models import Q
from archives.models import Author, Story

def return_a_rec(user):
    if user.is_authenticated:
        author_profile = Author.objects.filter(member=user).first() 
        eligible_stories = Story.objects.filter(
            ~Q(author=author_profile) & (~Q(visibility='Private') & Q(story_date__lte=date.today()))
        )
    else:
        eligible_stories = Story.objects.filter(
            (Q(visibility='Everyone') & Q(story_date__lte=date.today()))
        )
    
    return eligible_stories.order_by('?').first()
    

def get_all_visible_stories(user):
    if user.is_authenticated:
        return Story.objects.filter(
            Q(author__member_id=user.id) | (~Q(visibility='Private') & Q(story_date__lte=date.today()))
        ).order_by('-story_date')
    else:
        return Story.objects.filter(
            Q(visibility='Everyone') & (Q(story_date__lte=date.today()))
        ).order_by('-story_date')

def get_all_visible_stories_of_author(user, author_id):
    if user.is_authenticated:
        return Story.objects.filter(
            Q(author__member_id=author_id) &
            (
                (~Q(visibility='Private') & Q(story_date__lte=date.today()) | Q(author__member_id=user.id))
            )
        ).order_by('-story_date')
    else:
        return Story.objects.filter(
            Q(visibility='Everyone') & (Q(story_date__lte=date.today()))
        ).order_by('-story_date')