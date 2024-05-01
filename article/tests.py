import json
from django.test import TestCase, Client

from article.models import Article, Comment


# Create your tests here.


class TestCreateComment(TestCase):

    def test_create_comment(self) -> None:
        client = Client()
        # Given
        article = Article.create_one(
            "test_article_author",
            "test_article_title",
            "test_article_body",
        )

        response = client.post(
            "/v1/comments/",
            json.dumps(
                {
                    "author": (test_author := "test_comment_author"),
                    "body": (test_body := "test_comment_body"),
                    "article_id": article.id,
                }
            ),
            content_type="application/json",
        )

        # Then
        self.assertEqual(response.status_code, 200)
        comment_id = response.json()["comment_id"]
        result_comment = Comment.objects.get(id=comment_id)
        self.assertEqual(result_comment.author, test_author)
        self.assertEqual(result_comment.body, test_body)
