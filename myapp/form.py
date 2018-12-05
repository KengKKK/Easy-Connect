from django import forms


# function
class CallScript(forms.Form):
    # your_name = forms.CharField(label='Your name', max_length=100)
    inventory = forms.BooleanField(required=False)
    Version = forms.BooleanField(required=False)
    Environment = forms.BooleanField(required=False)
    CPU = forms.BooleanField(required=False)
    Memory = forms.BooleanField(required=False)
    Clock = forms.BooleanField(required=False)
    System = forms.BooleanField(required=False)
    Neighbors = forms.BooleanField(required=False)
    Vlan = forms.BooleanField(required=False)
    Interface = forms.BooleanField(required=False)
    # testCallScript = forms.BooleanField(required=False)

# connect
class ConnectSwitch(forms.Form):
    
    Ip = forms.CharField(label='IP', max_length=25)
    # Port = forms.CharField(label='Port', max_length=4)

    # ConnectSwitch = forms.BooleanField(required=False)
