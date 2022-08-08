import requests
import geopy.distance as ds

__api_url = 'https://sedeaplicaciones.minetur.gob.es/ServiciosRESTCarburantes/PreciosCarburantes/EstacionesTerrestres/'


def __get_data(url):
    """This method obtains the API data from an url"""
    return requests.get(url).json()


def get_stations_by_range(latitude, longitude, max_km):
    """This method gets latitude, longitude and max km and returns the gas stations that are in round range"""
    data = __get_data(__api_url)['ListaEESSPrecio']

    return_list = []

    for station in data:
        lat = station['Latitud'].replace(',', '.')
        long = station['Longitud (WGS84)'].replace(',', '.')

        if ds.geodesic((latitude, longitude), (lat, long)).km <= max_km:
            return_list.append(station)

    return return_list


def get_stations_by_range_filtered(latitude, longitude, max_km, **kwargs):
    """This method gets latitude, longitude, max km and the filter and returns the gas stations that are in round
    range filtered by price, gas type and gas station name"""

    # data = __get_data(__api_url)['ListaEESSPrecio']
    #
    # # if kwargs.keys() != ['station_name', 'gas']:
    # #     return 'Arguments not valid'
    #
    # filtered_name = []
    #
    # filter = []
    #
    # for station in data:
    #     name_list = kwargs['station_name'] if kwargs['station_name'] is not None else [station['Rótulo']]
    #
    #     for name in name_list:
    #         if name in station['Rótulo']:
    #             filtered_name.append(station)
    #             break
    #
    # for station in filtered_name:
    #
    #
    # for d in filtered_data:
    #     print(d['Rótulo'])
    #
    # for ads in data:
    #     print(ads['Rótulo'])

    return_list = []

    # for station in data:
    #     lat = station['Latitud'].replace(',', '.')
    #     long = station['Longitud (WGS84)'].replace(',', '.')
    #
    #     if ds.geodesic((latitude, longitude), (lat, long)).km <= max_km:
    #         return_list.append(station)
    #
    # return return_list


def get_stations():
    """This method returns all gas stations"""


def get_stations_filtered(**kwargs):
    """This method returns gas stations filtered by price, gas type, gas station name"""
