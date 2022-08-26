from django.forms import ModelForm
from django import forms
from .models import Product, Review



class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields= '__all__'
        

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']

        labels = {
            'value': 'Place your vote',
            'body': 'Add a comment with your vote'
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})