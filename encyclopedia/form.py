from django import forms


class NameForm(forms.Form):
    title = forms.CharField(label="Title", max_length=20)
    body = forms.CharField(max_length=1000)



class layout(forms.Form):
    search = forms.CharField(max_length=30)

class EditEntryForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea, label='Content')