from django import forms
from .models import ReviewModel

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewModel
        fields = ['review_text', 'rating']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].help_text = None
    review_text = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 40})
    )