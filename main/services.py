
import requests
from urllib.parse import unquote

def getData(destinationName='', minTripStartDate='', maxTripStartDate='', lengthOfStay='',
                minStarRating='', maxStarRating='', minTotalRate='', maxTotalRate='', minGuestRating='', maxGuestRating=''):

    url = 'https://offersvc.expedia.com/offers/v2/getOffers'
    parameters = {
        'scenario': 'deal-finder',
        'page': 'foo',
        'uid': 'foo',
        'productType': 'Hotel',
    }

    if destinationName:
        if isinstance(destinationName, str):
            parameters['destinationCity'] = destinationName
        else:
            parameters['regionIds'] = destinationName
    if minTripStartDate:
        parameters['minTripStartDate'] = minTripStartDate
    if maxTripStartDate:
        parameters['maxTripStartDate'] = maxTripStartDate
    if lengthOfStay:
        parameters['lengthOfStay'] = lengthOfStay
    if minStarRating:
        parameters['minStarRating'] = minStarRating
    if maxStarRating:
        parameters['maxStarRating'] = maxStarRating
    if minTotalRate:
        parameters['minTotalRate'] = minTotalRate
    if maxTotalRate:
        parameters['maxTotalRate'] = maxTotalRate
    if minGuestRating:
        parameters['minGuestRating'] = minGuestRating
    if maxGuestRating:
        parameters['maxGuestRating'] = maxGuestRating

    r = requests.get(url, params=parameters)
    data = r.json()
    if 'offers' in data:
        offersData = data['offers']
        if 'Hotel' in offersData:
            hotelsData = offersData['Hotel']
            hotels = []
            for hotel in hotelsData:
                hotelObject = hotel
                sites = hotelObject['hotelUrls']
                hotelObject['hotelUrls'] = {'hotelInfositeUrl': unquote(unquote(sites['hotelInfositeUrl'])),
                                            'hotelSearchResultUrl': unquote(unquote(sites['hotelSearchResultUrl']))}
                hotels.append(hotelObject)
            return hotels
        else:
            return []
    else:
        return []


# def getData():
#     # url = 'https://offersvc.expedia.com/offers/v2/getOffers?scenario=deal-finder&page=foo&uid=foo&productType=Hotel'
#     # r = requests.get(url)
#
#     url = 'https://offersvc.expedia.com/offers/v2/getOffers'
#     params = {'scenario': 'deal-finder', 'page': 'foo', 'uid': 'foo', 'productType': 'Hotel'}
#     r = requests.get(url, params=params)
#
#     data = r.json()
#     offersData = data['offers']
#     hotelsData = offersData["Hotel"]
#
#     return hotelsData