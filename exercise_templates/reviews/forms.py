from django import forms

from reviews.models import Review


class ReviewFormBasic(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'book': forms.Select(attrs={'class': 'form-select'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class ReviewCreateForm(ReviewFormBasic):
    ...


class ReviewEditForm(ReviewFormBasic):
    ...


class ReviewDeleteForm(ReviewFormBasic):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name in self.fields:
            self.fields[name].disabled = True
