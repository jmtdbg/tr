from sql_alchemy import banco

class PrecoMedioModel(banco.Model):
    __tablename__ = 'media_preco'

    neighbourhood_group = banco.Column(banco.String(80), primary_key=True)
    room_type = banco.Column(banco.String(80))
    price = banco.Column(banco.Float(precision=2))

    def __init__(self, neighbourhood_group, room_type, price):
        self.neighbourhood_group = neighbourhood_group
        self.room_type = room_type
        self.price = price

    def json(self):
        return {
            'neighbourhood_group': self.neighbourhood_group,
            'room_type': self.room_type,
            'price': self.price
        }

