from geopy.geocoders import Nominatim

def get_current_location():
    # Initialize geolocator
    geolocator = Nominatim(user_agent="my_geocoder")

    # Get current location coordinates
    location = geolocator.geocode("")

    if location:
        # Retrieve current location details
        current_location_name = location.address
        current_latitude = location.latitude
        current_longitude = location.longitude

        # Print current location details
        print("Current Location: ", current_location_name)
        print("Coordinates: Latitude - {}, Longitude - {}".format(current_latitude, current_longitude))
    else:
        print("Failed to get current location. Please ensure location services are enabled in your browser.")
        print("Instructions to enable location services:")
        print("1. Open your browser's settings or preferences.")
        print("2. Find the location settings or privacy settings.")
        print("3. Enable location services or allow websites to access your location.")
        print("4. Refresh the page or try running the program again.")

if __name__ == "__main__":
    get_current_location()