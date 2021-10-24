from django import forms
from .models import Trivia

class NameForm(forms.ModelForm):
    class Meta:
        model= Trivia
        fields = ['name']


FIRST_ANSWER= [ 
    ("Sachin Tendulkar", "Sachin Tendulkar"),
    ("Virat Kolli", "Virat Kolli"),
    ("Adam Gilchirst", "Adam Gilchirst"),
    ("Jacques Kallis", "Jacques Kallis"),
    ]

class FirstAnsForm(forms.ModelForm):
    first_answer = forms.ChoiceField(label = '',
                                     choices = FIRST_ANSWER,
                                     widget= forms.RadioSelect())
    class Meta:
        model = Trivia
        fields = ['first_answer']


SECOND_ANSWER = [
    ('White', 'White'),
    ('Yellow', 'Yellow'),
    ('Orange', 'Orange'),
    ('Green', 'Green')
    ]

class SecondAnsForm(forms.ModelForm):
    second_answer = forms.MultipleChoiceField(label = 'Select your answer', 
                                              choices=SECOND_ANSWER,
                                              widget = forms.CheckboxSelectMultiple)
    class Meta:
        model = Trivia
        fields = ['second_answer']

