from sql_alchemy import banco

class PrecoMedioModel(banco.Model):
    __tablename__ = 'media_preco'

    # hotel_id = banco.Column(banco.String, primary_key=True)
    neighbourhood_group = banco.Column(banco.String(80), primary_key=True)
    room_type = banco.Column(banco.String(80))
    price = banco.Column(banco.Float(precision=2))

    def __init__(self, neighbourhood_group, room_type, price):
        # self.hotel_id = hotel_id
        self.neighbourhood_group = neighbourhood_group
        self.room_type = room_type
        self.price = price

    def json(self):
        return {
            # 'hotel_id': self.hotel_id,
            'neighbourhood_group': self.neighbourhood_group,
            'room_type': self.room_type,
            'price': self.price
        }

    # @classmethod
    # def find_hotel(cls, hotel_id):
    #     hotel = cls.query.filter_by(hotel_id=hotel_id).first()
    #     if hotel:
    #         return hotel
    #     return None

    # def save_hotel(self):
    #     banco.session.add(self)
    #     banco.session.commit()

    # def update_hotel(self, nome, estrelas, diaria, cidade):
    #     self.nome = nome
    #     self.estrelas = estrelas
    #     self.diaria = diaria
    #     self.cidade = cidade

    # def delete_hotel(self):
    #     banco.session.delete(self)
    #     banco.session.commit()
