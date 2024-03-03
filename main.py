"""
This program allows users to look up weather information by ZIP code or city.

It utilizes the OpenWeatherMap API to retrieve geolocation and weather data.

Requirements:
    - Python 3.x
    - requests library
    - colorama library
    - datatime module

Usage:
    1. Run the program.
    2. Follow the prompts to select the search method (ZIP code or city),
    3. Enter the location information.
    4. Choose the unit of measurement (Metric, Imperial, Kelvin),
    5. The program will fetch the weather data and display it to the user.

Functions:
    - search_zip: Searches for location information based on a ZIP code.
       Parameters:
           - zip_inp (str): The ZIP code to search for.

    - search_city: Searches for location information based on a city name and
       state abbreviation.
       Parameters:
           - city_inp (str): The name of the city.
           - state_inp (str): The abbreviation of the state.

    - get_geocodes: Extracts geolocation information from a parsed response.
       Parameters:
           - parsed_response (dict or str): Parsed response from location
           search function.

    - get_weather: Retrieves weather data based on geolocation information.
       Parameters:
           - geo_response (tuple or str): Tuple containing city name, latitude,
           and longitude.

    - weather_processing: Processes weather data to extract relevant
    information.
       Parameters:
           - weather_response (dict or str): Weather data response.

    - get_abbreviation: Retrieves abbreviation for units of measurement.
       Parameters:
           - unit_inp (str): Unit of measurement.

    - print_weather: Prints formatted weather information.
       Parameters:
           - process_response (tuple or str): Processed weather information.
           - unit_response (tuple or str): Unit abbreviation and speed unit.
"""
import requests
from colorama import Fore, Style
from datetime import datetime


def search_zip(zip_inp):
    """
    Search for location by ZIP code.

    Args:
        zip_inp (str): The ZIP code to search for.

    Returns:
        dict or str: Dictionary containing location information if successful,
                     otherwise error message.
    """
    try:
        url = (f"http://api.openweathermap.org/geo/1.0/zip?zip={zip_inp},US"
               f"&appid=01d9a6107a99b19399c956dfb1e15d30")
        response = requests.request("GET", url)
    except (requests.HTTPError, requests.ConnectionError):
        zip_response = "connect error"
        return zip_response
    except (TypeError, KeyError):
        zip_response = "error"
        return zip_response
    else:
        try:
            zip_response = response.json()
            zip_response['lat']
            zip_response['lon']
        except KeyError:
            zip_response = "error"
            return zip_response
        else:
            print(f"\n{Fore.GREEN}Geo Code Request was Successful!\n{url}")
            return zip_response


def search_city(city_inp, state_inp):
    """
        Search for location by city name and state abbreviation.

        Args:
            city_inp (str): The name of the city.
            state_inp (str): The abbreviation of the state.

        Returns:
            dict or str: Dictionary containing location information if
            successful, otherwise error message.
        """
    try:
        url = (f"http://api.openweathermap.org/geo/1.0/direct?q={city_inp},"
               f"{state_inp},US&appid=01d9a6107a99b19399c956dfb1e15d30")
        response = requests.request("GET", url)
        response_json = response.json()
        response_json[0]
    except (requests.HTTPError, requests.ConnectionError):
        city_response = "connect error"
        return city_response
    except (TypeError, KeyError, IndexError):
        city_response = "error"
        return city_response
    else:
        if not response_json:
            city_response = "error"
            return city_response
        else:
            for dictionary in range(len(response_json)):
                city_response = (response_json[dictionary])
                print(f"\n{Fore.GREEN}Geo Code Request was Successful!\n{url}")
                return city_response


def get_geocodes(parsed_response):
    """
       Extract geocodes from parsed response.

       Args:
           parsed_response (dict or str): Parsed response from location
           search function.

       Returns:
           tuple or str: Tuple containing city name, latitude, and longitude
           if successful, otherwise error message.
       """
    if parsed_response in ("connect error", "error"):
        if parsed_response == 'error':
            geo_response = "error"
            return geo_response
        else:
            geo_response = "connect error"
            return geo_response
    else:
        city = parsed_response["name"]
        lat = parsed_response["lat"]
        lon = parsed_response["lon"]
        geo_response = city, lat, lon
        return geo_response


def get_weather(geo_response):
    """
    Get weather data based on geocodes.

    Args:
        geo_response (tuple or str): Tuple containing city name, latitude,
        and longitude.

    Returns:
        dict or str: Dictionary containing weather information if successful,
                     otherwise error message.
    """
    if geo_response in ("connect error", "error"):
        if geo_response == 'error':
            weather_response = 'error'
            return weather_response
        else:
            weather_response = 'connect error'
            return weather_response
    else:
        name, latitude, longitude = geo_response
        try:
            url = (f"https://api.openweathermap.org/data/2.5/weather?lat="
                   f"{latitude}&lon={longitude}&appid=01d9a6107a99b19399c956"
                   f"dfb1e15d30&units=Metric")
            response = requests.request("GET", url)
            weather_response = response.json()
            weather_response['name']
        except (requests.HTTPError, requests.ConnectionError):
            weather_response = "connect error"
            return weather_response
        except KeyError:
            weather_response = "error"
            return weather_response
        else:
            print(f"\n{Fore.GREEN}Weather Request was Successful!\n{url}")
            return weather_response


def weather_processing(weather_response):
    """
    Process weather JSON weather data and extract relevant information.

    Args:
        weather_response (dict or str): Weather data response.

    Returns:
        tuple or str: Tuple containing weather information if successful,
                      otherwise error message.
    """
    if weather_response in ("connect error", "error"):
        if weather_response == 'error':
            process_response = "error"
            return process_response
        else:
            process_response = "connect error"
            return process_response
    else:
        temperature = weather_response['main']
        information = weather_response['weather']
        wind = weather_response['wind']
        temp_info = information[0]
        temp = round(temperature['temp'])
        feels_like = round(temperature['feels_like'])
        temp_high = round(temperature['temp_max'])
        temp_low = round(temperature['temp_min'])
        humidity = temperature['humidity']
        pressure = temperature['pressure']
        description = temp_info['description'].title()
        wind_speed = wind['speed']
        process_response = (temp, feels_like, temp_high, temp_low, humidity,
                            pressure, description, wind_speed)
        return process_response


def get_abbreviation(unit_inp):
    """
        Get abbreviation for units.

        Args:
            unit_inp (str): Unit of measurement.

        Returns:
            tuple or str: Tuple containing unit abbreviation and speed unit if
            successful, otherwise error message.
        """
    if unit_inp.lower() == 'metric':
        unit_abbv = 'C'
        unit_speed = 'km/h'

    elif unit_inp.lower() == 'imperial':
        unit_abbv = 'F'
        unit_speed = 'mp/h'

    elif unit_inp.lower() == 'kelvin':
        unit_abbv = 'K'
        unit_speed = 'km/h'
    else:
        unit_response = "error"
        return unit_response
    unit_response = unit_abbv, unit_speed
    return unit_response


def print_weather(process_response, unit_response):
    """
        Print weather information in a beautiful format using colorama.

        Args:
            process_response (tuple or str): Processed weather information.
            unit_response (tuple or str): Unit abbreviation and speed unit.

        Returns:
            str: Formatted weather information string.
        """
    if process_response in ("connect error", "error"):
        if process_response == 'error':
            print_response = 'error'
            return print_response
        else:
            print_response = 'connect error'
            return print_response
    elif unit_response == 'error':
        print_response = 'error'
        return print_response
    else:
        unit, unit_speed = unit_response
        (temp, feels_like, temp_high, temp_low, humidity, pressure,
         description, wind_speed) = process_response
        print_response = (f"{Fore.CYAN}Sky Condition:{Fore.CYAN} {description}"
                          f"\n{Fore.CYAN}Temperature:{Fore.CYAN} {temp}{unit}"
                          f"\n{Fore.CYAN}Feels Like: {Fore.CYAN}{feels_like}"
                          f"{unit}\n{Fore.CYAN}"
                          f"High Temp: {Fore.CYAN}{temp_high}{unit}\n"
                          f"{Fore.CYAN}Low Temp:{Fore.CYAN} {temp_low}{unit}\n"
                          f"{Fore.CYAN}Humidity: {Fore.CYAN}{humidity}%\n"
                          f"{Fore.CYAN}Pressure: {Fore.CYAN}{pressure} "
                          f"hpa\n{Fore.CYAN}Wind Speed:{Fore.CYAN} "
                          f"{wind_speed} {unit_speed}")
        return print_response


def main():
    """Prompt user for information and call the print weather function."""
    print(f"{Style.BRIGHT}\n{Fore.YELLOW}Welcome to my weather program.")
    looping = 'True'
    choice = input(f"\n{Fore.YELLOW}Would you like to perform a weather "
                   f"lookup? {Fore.BLACK}({Fore.BLUE}Y{Fore.BLACK}/"
                   f"{Fore.LIGHTRED_EX}N{Fore.BLACK}): ").strip()
    while looping == 'True':
        if choice.lower() == 'y':
            search_inp = input(f"\n{Fore.BLUE}> Would you like to search by "
                               f"{Fore.GREEN}'ZIP' {Fore.BLUE}or {Fore.GREEN}"
                               f"'CITY'{Fore.BLUE}?: ").strip()
            while search_inp.lower() not in ['zip', 'city']:
                search_inp = input(f"\n{Fore.LIGHTRED_EX}** Select lookup by "
                                   f"'ZIP' or 'CITY': ").strip()
            else:
                unit_inp = input(f"\n{Fore.BLUE}> "
                                 f"How would you like the temperature "
                                 f"displayed? {Fore.GREEN}"
                                 f"(Metric, Imperial, Kelvin){Fore.BLUE}"
                                 f": ").strip()
                while unit_inp.lower() not in ['metric', 'imperial', 'kelvin']:
                    unit_inp = input(f"\n{Fore.LIGHTRED_EX}"
                                     f"** Select a Unit of Measurement "
                                     f"(Metric, Imperial, Kelvin): ").strip()
                else:
                    try:
                        if search_inp.lower() == "zip":
                            zip_inp = input(f"\n{Fore.BLUE}> Enter the "
                                            f"{Fore.GREEN}Zip Code{Fore.BLUE} "
                                            f"you would like "
                                            f"to lookup: ").strip()
                            search_type = search_zip(zip_inp)
                            return search_type
                        elif search_inp.lower() == "city":
                            city_inp = input(f"\n{Fore.BLUE}> Enter the "
                                             f"{Fore.GREEN}City{Fore.BLUE} "
                                             f"you would like "
                                             f"to lookup: ").strip()
                            while True:
                                if city_inp == "":
                                    city_inp = input(f"\n{Fore.LIGHTRED_EX}"
                                                     f"> Please Enter "
                                                     f"a City: ").strip()
                                else:
                                    state_inp = input(f"\n{Fore.BLUE}> "
                                                      f"Enter a{Fore.GREEN} "
                                                      f"State{Fore.BLUE}"
                                                      f": ").strip()
                                    if state_inp == "":
                                        continue
                                    else:
                                        search_type = search_city(city_inp,
                                                                  state_inp)
                                        return search_type
                    finally:
                        get_geo = get_geocodes(search_type)
                        if get_geo == 'error':
                            print(f"\n{Fore.LIGHTRED_EX}> You have entered an "
                                  f"invalid location. Please use a correct "
                                  f"ZIP code or CITY name.")
                            continue
                        elif get_geo == "connect error":
                            print(f"\n{Fore.RED}> Could not establish a "
                                  f"connection to the server, There was a "
                                  f"connection error.")
                            continue
                        weather = get_weather(get_geo)
                        weather_fix = weather_processing(weather)
                        units = get_abbreviation(unit_inp)
                        time = datetime.now()
                        current_time = time.strftime("%H:%M")
                        day = time.strftime('%A')
                        if get_geo == 'error':
                            print('error')
                        else:
                            city, x, y = get_geo
                            print(f"{Fore.BLACK}{"":_^50}")
                            print(f"\n{Fore.MAGENTA}The Current Weather "
                                  f"Forecast in {city}\n{day} {current_time}")
                        weather_table = print_weather(weather_fix, units)
                        print(f"{Fore.BLACK}{"":_^50}")
                        print(weather_table)
                        print(f"{Fore.BLACK}{"":_^50}")
                        choice = input(f"\n{Fore.YELLOW}Would you like to "
                                       f"perform another weather lookup? "
                                       f"{Fore.BLACK}({Fore.BLUE}Y{Fore.BLACK}"
                                       f"/{Fore.LIGHTRED_EX}N{Fore.BLACK})"
                                       f": ").strip()
                        continue
        elif choice.lower() == 'n':
            print(f"\n{Fore.YELLOW}~~ Thank you, have a good day, Good Bye")
            break
        else:
            choice = input(f"\n{Fore.LIGHTRED_EX}** Enter 'Y' to perform a "
                           f"lookup or 'N' to exit: ").strip()


if __name__ == "__main__":
    main()
else:
    print(f"\n** Thank you for running my module, below is the docstring:"
          f"\n{"":^50}\n{__doc__}{"":^50}")
