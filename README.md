# Broskies_hubtasks.day12
Task 10: Weather App Using API

OverviewFor Task 10, we were required to build a Python program that displays the weather using a public API. The objective was to create a simple yet functional application that retrieves and displays weather data for a given city.

What We BuiltWe built a basic weather app that includes the following features:

1. API Integration: We integrated the OpenWeatherMap API to fetch weather data.
2. User Input: The app asks the user to input the city name.
3. Weather Data Display: The app displays the current temperature, humidity, and weather description for the given city.
4. Error Handling: The app handles cases where the city is not found.

Why We Built ItThe weather app was built to:

1. Demonstrate API Integration: By integrating a public API, we demonstrated our understanding of working with external data sources.
2. Practice Python Programming: We used Python to build the app, practicing our programming skills.
3. Develop Real-World Applications: The weather app is a real-world application that can be used to retrieve and display weather data.

How We Built ItHere's a step-by-step breakdown of how we built the weather app:

Step 1: Choosing the APIWe chose the OpenWeatherMap API because it provides a free tier and is well-documented.

Step 2: Installing Required LibrariesWe installed the requests library using pip to make HTTP requests to the API.

Step 3: Writing the Python CodeWe wrote a Python script that:

1. Fetches Weather Data: Uses the requests library to make a GET request to the OpenWeatherMap API.
2. Parses JSON Response: Parses the JSON response from the API to extract relevant weather data.
3. Displays Weather Data: Displays the current temperature, humidity, and weather description for the given city.

Step 4: Implementing Error HandlingWe implemented error handling to handle cases where the city is not found.

Step 5: Testing the AppWe tested the app to ensure that it works as expected.

Technical Details- We used Python 3.x (the latest version available) for building the application.
- We used the requests library to make HTTP requests to the OpenWeatherMap API.
- We used the OpenWeatherMap API to fetch weather data.

Challenges and Solutions- Challenge: Handling API errors and exceptions.
- Solution: We implemented error handling to handle cases where the city is not found or the API returns an error.
- Challenge: Parsing JSON response from the API.
- Solution: We used the json() method to parse the JSON response from the API.

ConclusionIn conclusion, we built a basic weather app using Python and the OpenWeatherMap API. The app retrieves and displays weather data for a given city, demonstrating our understanding of API integration and Python programming. The app can be enhanced by adding more features, such as displaying forecasts or handling different units.
