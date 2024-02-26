from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


from general.views import HomePageView
from general.views import CreateFeedbackView
from general.views import AboutUsView
from general.views import CreateSigninView
from general.views import CreateSignupView
from general.views import GalleryView
from general.views import RoomsPage
from general.views import CreateBookingView

urlpatterns = [
    path('home/',HomePageView.as_view(),name='index_page'),
    path('about/',AboutUsView.as_view(),name='about_page'),
    path('feedback/',CreateFeedbackView.as_view(),name='new_feedback'),
    path('signin/',CreateSigninView.as_view(),name='signin_page'),
    path('signup/',CreateSignupView.as_view(),name='signup_page'),
    path('gallery/',GalleryView.as_view(),name='gallery_page'),
    path('rooms/', RoomsPage.as_view(),name='rooms_page'),
    path('booking/',CreateBookingView.as_view(),name='book_page')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)