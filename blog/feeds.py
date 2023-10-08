from django.contrib.gis.feeds import Feed
from django.urls import reverse_lazy

from blog.models import Post


def trunkatewords(body, param):
    pass


class LatestPostFeed(Feed):
    title = "My Blog"
    link = reverse_lazy('blog:post_list')
    description = "New posts of my blog."

    def items(self):
        return Post.published.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return trunkatewords(item.body, 30)
