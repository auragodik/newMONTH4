from django import forms

class BookSearchForm(forms.Form):
    query = forms.CharField(
        label='Поиск книги',
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Введите название или автора'})
    )