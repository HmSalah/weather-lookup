# Weather Lookup Program

### This program allows users to look up weather information by ZIP code or city, It utilizes the OpenWeatherMap API to retrieve geolocation and weather data.
-----------------------------------------------------------------------------------

**1.  Requirements:**
   *	Python 3.x
   *	requests library
   *	colorama library
   *	datatime module

**2. Usage:**
  1.  Run the program.
  2.  Follow the prompts to select the search method (ZIP code or city),
  3.  Enter the location information.
  4.  Choose the unit of measurement (Metric, Imperial, Kelvin),
  5.  The program will fetch the weather data and display it to the user.

**3. Functions:**
  *	search_zip: Searches for location information based on a ZIP code.
    *  Parameters:
       * zip_inp (str): The ZIP code to search for.

  *	search_city: Searches for location information based on a city name and state abbreviation.
     *	Parameters:
         *	city_inp (str): The name of the city.
         *	state_inp (str): The abbreviation of the state.

  *	get_geocodes: Extracts geolocation information from a parsed response.
     *	Parameters:
         *	parsed_response (dict or str): Parsed response from location
         *	search function.

  *	get_weather: Retrieves weather data based on geolocation information.
     *	Parameters:
        *	geo_response (tuple or str): Tuple containing city name, latitude, and longitude.

  *	weather_processing: Processes weather data to extract relevant information.
     *	Parameters:
        *	weather_response (dict or str): Weather data response.

  *	get_abbreviation: Retrieves abbreviation for units of measurement.
     *	Parameters:
         *	unit_inp (str): Unit of measurement.

  *	 print_weather: Prints formatted weather information.
      *	Parameters:
         *	process_response (tuple or str): Processed weather information.
         *	unit_response (tuple or str): Unit abbreviation and speed unit.
  -----------------------------------------------------------------------------------
  ##	<div align="center"> Weather Lookup in action! </div>
  ![image](https://github.com/HmSalah/weather-lookup/assets/74623220/325404f3-8b5a-479a-b67b-1aab5b24ea59)

