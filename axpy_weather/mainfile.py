# -*- coding: utf-8 -*-

import argparse
import sys
import pyowm

#
# DEFINE YOUR FUNCTIONS HERE...
#

def getweather(args):
    owm = pyowm.OWM(API_key='17eedc3734df4de3f39231276ce06112')  # You MUST provide a valid API key

    # Have a pro subscription? Then use:
    # owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')

    # Will it be sunny tomorrow at this time in Milan (Italy) ?
    forecast = owm.daily_forecast("Santiago,cl")
    tomorrow = pyowm.timeutils.tomorrow()
    print('Will is be sunny in Santiago tomorrow? ' + str(forecast.will_be_sunny_at(tomorrow)))  # Always True in Italy, right? ;-)

    # Search for current weather in London (UK)
    observation = owm.weather_at_place('Stockholm,se')
    w = observation.get_weather()

    # Weather details
    w.get_wind()                  # {'speed': 4.6, 'deg': 330}
    w.get_humidity()              # 87
    w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

    print('\nStockholm weather ')
    print('Wind: ' + str(w.get_wind()))
    print('Humidity: ' + str(w.get_humidity()))
    print('Temperature: ' + str(w.get_temperature('celsius')['temp']) + ' Degree Celsius')


def main():

    '''Console script'''
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    parser_getweather = subparsers.add_parser('getweather')
    parser_getweather.set_defaults(func=getweather)

    if len(sys.argv) <=1:
        sys.argv.append('--help')

    # Show help if no arguments are given
    args = parser.parse_args()
    args.func(args)
    
    
if __name__ == "__main__":
    main()
