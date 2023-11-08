import requests  # importing the requests library to work with API
import time

favorite_cities = []    # Sample data storage for favorite cities

# function for retrieve the weather data from the API server
def weather_checking(api_key, location):
    response = requests.get(f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}")    # requesting to the web server to get the data
    code = response.status_code     # response code for the request
    data = response.json()
    if code == 200:
        weather_status = data['current']['condition']['text']   # Weather description of the given city
        temp = data['current']['temp_f']                        # temperature of the city or location
        return f"Weather:{weather_status}, Temperature:{temp} f"
    else:
        return "Error retrieving weather data."

# to add the city into the favorite cities list
def add_city(city):
    favorite_cities.append(city)
    print(f"Added {city} to your favorite list.")

# to remove the city from the favorite cities list
def remove_city(city):
    if city in favorite_cities:
        favorite_cities.remove(city)
        print(f"Removed {city} from your favorite list.")
    else:
        print(f"{city} is not in your favorite list.")

# to display the city from the favorite cities list
def display_favorites():
    if len(favorite_cities) > 0:
        print("Your favorite cities:")
        for city in favorite_cities:
            print(city)
    else:
        print("No items in favorite cities")

# to update the city from the favorite cities list
def update(city, api_key):
    print(f"Updated {weather_checking(api_key, city)}")

# CRUD operation on favorite cities list
def crud_operation(location, api_key):
    flag = True
    while flag:
        choice = input("Choose the option\n1.Add     2.Read      3.Update    4.Delete\n")
        if choice == '1':
            add_city(location)
        elif choice == '2':
            display_favorites()
        elif choice == '3':
            city = input("Which city you want to update from the favorites:")
            update(city, api_key)
        elif choice == '4':
            removing = input("Which city you want to remove from the favorites:")
            remove_city(removing)
        else:
            flag = False

def main():
    print("---------WEATHER CHECKING APPLICATION---------")
    api_key = input("Enter your API key:")
    end = False
    while not end:
        location = input("Enter the city you want to know the weather:")
        print(weather_checking(api_key, location))
        wish = input("Do you want to know about favorite cities(y/n):").lower()
        if wish == 'y':
            crud_operation(location, api_key)
            choice2 = input("Do you want to continue(y/n):")
            if choice2 == 'n':
                end = True
        else:
            end = True
    print("Thank you for visiting :) ....")

if __name__ == '__main__':
    main()
    time.sleep(15)