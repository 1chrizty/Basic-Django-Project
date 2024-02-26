from django import forms

from general.models import FeedbackModel
from general.models import SigninModel 
from general.models import SignupModel
from general.models import BookingModel

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = FeedbackModel
        fields = ['name','email','contact','message','place']

class SigninForm(forms.ModelForm):
    class Meta:
        model = SigninModel
        fields = ['email','password']

class SignupForm(forms.ModelForm):
    class Meta:
        model = SignupModel
        fields = ['name','email','contact','password']

class BokingForm(forms.ModelForm):
    class Meta:
        model = BookingModel
        fields = ['name','age','contact','address','email','roomtype','paymentmethod']