from django.shortcuts import render, redirect, get_object_or_404

from .forms import AddBoardForm
from .models import Category, Board
# Create your views here.

def home_page(request):
    categories = Category.objects.all()
    boards = Board.objects.all().order_by('-posted_date')[:8]
    context = {
        'categories': categories,
        'boards': boards
    }
    return render(request, './home_page.html', context)


def add_board_page(request):
    if request.method == 'POST':
        form = AddBoardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')  # После успешного добавления, перенаправляем на главную страницу
    else:
        form = AddBoardForm()

    context = {'form': form}
    return render(request, './add_board_page.html', context)
def board_detail_page(request, slug):
    board = get_object_or_404(Board, slug=slug)
    context = {
        'board': board
    }
    return render(request, './board_detail_page.html', context)

def edit_board_page(request, slug):
    board = get_object_or_404(Board, slug=slug)
    form = AddBoardForm(request.POST or None, request.FILES or None, instance=board)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('board_detail_page', slug=board.slug)

    context = {
        'board': board,
        'form': form
    }

    return render(request, './edit_board_page.html', context)

def delete_board_page(request, slug):
    board = get_object_or_404(Board, slug=slug)
    if request.method == 'POST':
        board.delete()
        return redirect('home_page')

    context = {
        'board': board
    }

    return render(request, './delete_board_page.html', context)


def all_board_page(request):
    boards = Board.objects.all().order_by('-posted_date')
    context = {'boards': boards}
    return render(request, './all_boards.html', context)