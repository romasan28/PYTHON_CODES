from address import address

class mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track
        
    def __str__(self):
            # Форматируем строку согласно заданию
            return (f"Отправление {self.track} из {self.from_address} в {self.to_address}. "
                    f"Стоимость {self.cost} рублей.")