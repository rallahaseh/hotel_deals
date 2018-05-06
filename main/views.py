# Create your views here.

from django.shortcuts import render
from django.views.generic import TemplateView

from . import services
from .form import HomeForm
from django.http import HttpResponse

# Class based View
class HomeView(TemplateView):

    template_name = 'hotels_deals/index.html'

    def get(self, request):
        # <view logic>
        # return HttpResponse('get result')

        form = HomeForm()
        data = services.getData()

        args = {
            'form': form, 'searchData': data
        }
        return render(request, self.template_name, args)

    def post(self, request):
        # TEST Post
        # return HttpResponse(request.POST['destinationName'])

        form = HomeForm(request.POST)
        # if form.is_valid():
        #
        #
        destination_name = request.POST['destinationName']
        min_trip_start = request.POST['minTripStartDate']
        max_trip_start = request.POST['maxTripStartDate']
        length_of_stay = request.POST['lengthOfStay']
        min_star_rating = request.POST['minStarRating']
        max_star_rating = request.POST['maxStarRating']
        min_total_rate = request.POST['minTotalRate']
        max_total_rate = request.POST['maxTotalRate']
        min_guest_rating = request.POST['minGuestRating']
        max_guest_rating = request.POST['maxGuestRating']

        searchData = services.getData(destinationName=destination_name,
                                      minTripStartDate=min_trip_start,
                                      maxTripStartDate=max_trip_start,
                                      lengthOfStay=length_of_stay,
                                      minStarRating=min_star_rating,
                                      maxStarRating=max_star_rating,
                                      minTotalRate=min_total_rate,
                                      maxTotalRate=max_total_rate,
                                      minGuestRating=min_guest_rating,
                                      maxGuestRating=max_guest_rating)
        args = {
            'form': form, 'searchData': searchData
        }
        return render(request, self.template_name, args)

# Function based View
# def index(request):
#     data = services.getData()
#     data_list = {
#         'searchData': data
#     }
#
#     return render(request, 'hotels_deals/index.html', data_list)
