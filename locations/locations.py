""" Locations are few locations saved in the app memory """
LOCATIONS=[]

class Location:
    def __init__(self, name, address, longtitude, latitude):
        self.name = name
        self.address = address
        self.longtitude = longtitude
        self.latitude = latitude

    def get_locations() -> list[dict]:
        """
        Get all locations in app memory
        """
        return LOCATIONS

    def post_location(location: dict) -> dict:
        LOCATIONS.append(location)
        return location