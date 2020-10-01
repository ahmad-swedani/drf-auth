from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Post
# Create your tests here.

class BlogTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='testuser', password='password')
        test_user.save()


        test_Post = Post.objects.create(
            author = test_user,
            title = 'ahmad swedani',
            short_content = 'Nokia & 5G',
            full_content = 'Nokia clinches 5G deal with BT to phase out Huawei\'s kit in EE network'
        )
        test_Post.save() 

        

    def test_Post_content(self):

        movie = Post.objects.get(id=1)
        actual_author = str(movie.author)
        actual_title = str(movie.title)
        actual_short_content = str(movie.short_content)
        actual_full_content = str(movie.full_content)

        self.assertEqual(actual_author, 'testuser')
        self.assertEqual(actual_title, 'ahmad swedani')
        self.assertEqual(actual_short_content, "Nokia & 5G")
        self.assertEqual(actual_full_content, 'Nokia clinches 5G deal with BT to phase out Huawei\'s kit in EE network')