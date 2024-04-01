from .models import Board
from django import forms

class AddBoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ('title', 'category', 'description', 'image', 'price', 'is_related_price', 'author_name', 'author_number')
