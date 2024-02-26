from django.contrib import admin

from general.models import FeedbackModel

from general.models import SigninModel

from general.models import SignupModel

from general.models import BookingModel

# Register your models here.

admin.site.register(FeedbackModel)

admin.site.register(SigninModel)

admin.site.register(SignupModel)

admin.site.register(BookingModel)