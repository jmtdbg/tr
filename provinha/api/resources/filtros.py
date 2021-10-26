
# Tratando parametros vazios e parametros default
def normalize_path_params(id = None, 
                          name = None,
                          host_id = None,
                          host_name = None,
                          neighbourhood_group = None,
                          neighbourhood = None,
                          latitude = None,
                          longitude = None,
                          room_type = None,
                          price = None,
                          minimum_nights = None,
                          number_of_reviews = None,
                          last_review = None,
                          reviews_per_month = None,
                          calculated_host_listings_count = None,
                          availability_365 = None,
                          like = None, 
                          limit = 50, 
                          offset = 0, **dados):
    if neighbourhood_group:
        return {
            'id': id,
            'name': name,
            'host_id': host_id,
            'host_name': host_name,
            'neighbourhood_group': neighbourhood_group,
            'neighbourhood': neighbourhood,
            'latitude': latitude,
            'longitude': longitude,
            'room_type': room_type,
            'price': price,
            'minimum_nights': minimum_nights,
            'number_of_reviews': number_of_reviews,
            'last_review': last_review,
            'reviews_per_month': reviews_per_month,
            'calculated_host_listings_count': calculated_host_listings_count,
            'availability_365': availability_365,
            'like': like,
            'limit': limit,
            'offset': offset}
    return {
            'id': id,
            'name': name,
            'host_id': host_id,
            'host_name': host_name,
            'neighbourhood_group': neighbourhood_group,
            'neighbourhood': neighbourhood,
            'latitude': latitude,
            'longitude': longitude,
            'room_type': room_type,
            'price': price,
            'minimum_nights': minimum_nights,
            'number_of_reviews': number_of_reviews,
            'last_review': last_review,
            'reviews_per_month': reviews_per_month,
            'calculated_host_listings_count': calculated_host_listings_count,
            'availability_365': availability_365,
            'like': like,
            'limit': limit,
            'offset': offset}

consulta_sem_ng = "SELECT * FROM residencias \
            WHERE id = ? and name = ? and host_id = ? and host_name = ? and neighbourhood_group = ?\
            and neighbourhood = ? and latitude = ? and longitude = ? and room_type = ? and price = ?\
            and minimum_nights = ? and number_of_reviews = ? and last_review = ? and reviews_per_month = ?\
            and calculated_host_listings_count = ? and availability_365 = ? and like = ?\
            LIMIT ? OFFSET ?"

consulta_com_ng = "SELECT * FROM residencias \
            WHERE id = ? and name = ? and host_id = ? and host_name = ? and neighbourhood_group = ?\
            and neighbourhood = ? and latitude = ? and longitude = ? and room_type = ? and price = ?\
            and minimum_nights = ? and number_of_reviews = ? and last_review = ? and reviews_per_month = ?\
            and calculated_host_listings_count = ? and availability_365 = ? and like = ?\
            LIMIT ? OFFSET ?"

#########     preco-medio    ###########

def normalize_path_params_pm(neighbourhood_group=None,
                          room_type = None,
                          price = 0,
                          limit = 50,
                          offset = 0, **dados):
    if neighbourhood_group:
        return {
            'neighbourhood_group': neighbourhood_group,
            'room_type': room_type,
            'price': price,
            'limit': limit,
            'offset': offset}
    return {
        'neighbourhood_group': neighbourhood_group,
        'room_type': room_type,
        'price': price,
        'limit': limit,
        'offset': offset}

consulta_sem_ng_mp= "SELECT * FROM media_preco \
            WHERE (neighbourhood_group = ?) and (room_type = ?) \
            and (price = ?) \
            LIMIT ? OFFSET ?"

consulta_com_ng_mp = "SELECT * FROM media_preco \
            WHERE (neighbourhood_group = ?) and (room_type = ?) \
            and (price = ?) \
            LIMIT ? OFFSET ?"