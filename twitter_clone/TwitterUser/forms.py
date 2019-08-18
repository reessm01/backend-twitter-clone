from django import forms

class EditHeadlineForm(forms.Form):
    headline = forms.CharField(max_length=140, widget=forms.Textarea(attrs={"rows":2, "cols":20, 'style':'resize:none;'}))