from django.http import HttpResponse

from .models import Board


def home(request):
    boards = Board.objects.all()

    board_names = [
      board.name for board in boards
    ]

    response_html = '<br>'.join(board_names)

    return HttpResponse(response_html)
