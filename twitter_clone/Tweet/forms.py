from django import forms

class NewTweetForm(forms.Form):
    text = forms.CharField(max_length=140, widget=forms.Textarea(attrs={"rows":3, "cols":20, 'style':'resize:none;'}))