from article.models import Comment


def create_comment_service(
    article_id: int,
    author: str,
    body: str,
) -> Comment:
    return Comment.create_one(author, body, article_id)
