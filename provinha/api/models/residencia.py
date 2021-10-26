from sql_alchemy import banco

class ResidenciaModel(banco.Model):
    __tablename__ = 'residencias'

    id = banco.Column(banco.Integer, primary_key=True)
    name = banco.Column(banco.String(80))
    host_id = banco.Column(banco.String(20))
    host_name = banco.Column(banco.String(80))
    neighbourhood_group = banco.Column(banco.String(80))
    neighbourhood = banco.Column(banco.String(80))
    latitude = banco.Column(banco.Float)
    longitude = banco.Column(banco.Float)
    room_type = banco.Column(banco.String(80))
    price = banco.Column(banco.Float)
    minimum_nights = banco.Column(banco.String(20))
    number_of_reviews = banco.Column(banco.String(20))
    last_review = banco.Column(banco.String(80))
    reviews_per_month = banco.Column(banco.Float)
    calculated_host_listings_count = banco.Column(banco.String(20))
    availability_365 = banco.Column(banco.String(20))
    like = banco.Column(banco.String)
    
    def __init__(self, id, name, host_id, host_name, neighbourhood_group, neighbourhood, latitude, longitude, room_type, price, minimum_nights, number_of_reviews, last_review, reviews_per_month, calculated_host_listings_count, availability_365, like):
        self.id = id
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
        self.like = like
        

    def json(self):
        return {
            'id': self.id,  
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
            'availability_365': self.availability_365,
            'like': self.like
        }
    @classmethod
    def find_residencia(cls, id):
        # SELECT * FROM residencias WHERE id = $id LIMIT 1;
        residencia = cls.query.filter_by(id=id).first()
        if residencia:
            return residencia
        return None
    
    def save_residencia(self):
        banco.session.add(self)
        banco.session.commit()

    def update_residencia(self, name, host_id, host_name, neighbourhood_group, neighbourhood, latitude, longitude, room_type, price, minimum_nights, number_of_reviews, last_review, reviews_per_month, calculated_host_listings_count, availability_365, like):
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
        self.like = like
    
    def delete_residencia(self):
        banco.session.delete(self)
        banco.session.commit()

class ResidenciaLikeModel(banco.Model):

    id = banco.Column(banco.Integer, primary_key=True)
    like = banco.Column(banco.String)
    
    def __init__(self, id, like):
        self.id = id
        self.like = like
        

    def json(self):
        return {
            'id': self.id,  
            'like': self.like
        }
    @classmethod
    def find_residencia(cls, id):
        # SELECT * FROM residencias WHERE id = $id LIMIT 1;
        residencia = cls.query.filter_by(id=id).first()
        if residencia:
            return residencia
        return None
    
    def save_residencia(self):
        banco.session.add(self)
        banco.session.commit()

    def update_residencia(self, like):
        self.like = like
    
    def delete_residencia(self):
        banco.session.delete(self)
        banco.session.commit()