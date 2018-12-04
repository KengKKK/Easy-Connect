from django import forms

class CallScript(forms.Form):
    # your_name = forms.CharField(label='Your name', max_length=100)
    testCallScript = forms.BooleanField(required=False)

class ConnectSwitch(forms.Form):
    # Ip = forms.CharField(label='IP Address', max_length=25)
    # Port = forms.CharField(label='Port', max_length=4)
        testCallScript = forms.BooleanField(required=False)
