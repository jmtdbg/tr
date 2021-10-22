

class ResidenciaModel:
    def __init__(self, id, name, host_id, host_name, neighbourhood_group, neighbourhood, latitude, longitude, room_type, price, minimum_nights, number_of_reviews, last_review, reviews_per_month, calculated_host_listings_count, availability_365):
        self.residencia_id = id
        self.name = name
        self.host_id = host_id
        self.host_name = host_name
        self.neighbourhood_group = neighbourhood_group
        self.neighbourhood = neighbourhood
        self.latitude = latitude
        self.longitude = longitude
        self.room_type = room_type
        self.price = price
        self.minimum_nights = minimum_nights
        self.number_of_reviews = number_of_reviews
        self.last_review = last_review
        self.reviews_per_month = reviews_per_month
        self.calculated_host_listings_count = calculated_host_listings_count
        self.availability_365 = availability_365

    def json(self):
        return {
            'id': self.residencia_id,  
            'name': self.name,
            'host_id': self.host_id,
            'host_name': self.host_name,
            'neighbourhood_group': self.neighbourhood_group,
            'neighbourhood': self.neighbourhood,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'room_type': self.room_type,
            'price': self.price,
            'minimum_nights': self.minimum_nights,
            'number_of_reviews': self.number_of_reviews,
            'last_review': self.last_review,
            'reviews_per_month': self.reviews_per_month,
            'calculated_host_listings_count': self.calculated_host_listings_count,
            'availability_365': self.availability_365
        }
