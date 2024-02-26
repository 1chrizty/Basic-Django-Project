from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import CreateView,ListView

# Create your views here.

from general.models import FeedbackModel
from general.forms import FeedbackForm
from general.models import SigninModel
from general.forms import SigninForm
from general.models import SignupModel
from general.forms import SignupForm
from general.models import BookingModel
from general.forms import BokingForm

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutUsView(TemplateView):
    template_name = 'about.html'

class GalleryView(TemplateView):
    template_name = 'gallery.html'

 
class CreateFeedbackView(CreateView):
    template_name='create_feedback.html'
    model= FeedbackModel
    form_class= FeedbackForm
    success_url= '/gen/home'

class CreateSigninView(CreateView):
    template_name='sign_in.html'
    model = SigninModel
    form_class = SigninForm
    success_url= '/gen/home'

class CreateSignupView(CreateView):
    template_name='sign_up.html'
    model = SignupModel
    form_class = SignupForm
    success_url = '/gen/home'

class RoomsPage(TemplateView):
    template_name='rooms.html'

class CreateBookingView(CreateView):
    template_name='book.html'
    model=BookingModel
    form_class=BokingForm
    success_url='/gen/home'
