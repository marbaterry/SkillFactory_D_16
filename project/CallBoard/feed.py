from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import Post


class LatestEntriesFeed(Feed):
    title = "Police beat site news"
    link = "/sitenews/"
    description = "Updates on changes and additions to police beat central."

    def items(self):
        return Post.objects.order_by('-postDate')[:5]

    def item_title(self, item):
        return item.postTitle

    def item_description(self, item):
        return item.postCategory

    # # item_link is only needed if NewsItem has no get_absolute_url method.
    # def item_link(self, item):
    #     # return reverse('post', args=[item.pk])
    #     return reverse('post_detail', args=[item.pk])