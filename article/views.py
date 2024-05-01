import json
from http.client import BAD_REQUEST

from django.http import HttpRequest, JsonResponse
from django.views.generic import View

from services import create_comment_service

# Create your views here.


# noinspection PyMethodMayBeStatic
class CommentView(View):
    def post(self, request: HttpRequest) -> JsonResponse:
        errors = []

        try:
            body = json.loads(request.body)
        except json.JSONDecodeError:
            errors.append("Invalid JSON")

        if "article_id" not in body:
            errors.append("Missing article id")
        elif not isinstance(body["article_id"], int):
            errors.append(f"article_id is not an integer. received: {body['article_id']}")
        if "author" not in body:
            errors.append("Missing author")
        elif not isinstance(body["author"], str):
            errors.append(f"author is not a string. received: {body['author']}")
        if 'body' not in body:
            errors.append("Missing body")
        elif not isinstance(body["body"], str):
            errors.append(f"body is not a string. received: {body['body']}")

        if errors:
            return JsonResponse({"errors": errors}, status=BAD_REQUEST)

        comment = create_comment_service(
            body["article_id"],
            body["author"],
            body["body"],
        )
        return JsonResponse({"comment_id": comment.id})
