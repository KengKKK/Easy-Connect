from django import forms

# connect
class ConnectSwitch(forms.Form):
    
    Ip = forms.CharField(label='IP', max_length=25)
    user = forms.CharField(label='IP', max_length=25)
    passw = forms.CharField(label='IP', max_length=25)


