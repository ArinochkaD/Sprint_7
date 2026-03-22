class OrderData:
    def __init__(
            self, 
            firstName,
            lastName,
            address,
            metroStation,
            phone,
            rentTime,
            deliveryDate,
            comment,
            color,
        ):
        self.firstName = firstName
        self.lastName = lastName
        self.address = address
        self.metroStation = metroStation
        self.phone = phone
        self.rentTime = rentTime
        self.deliveryDate = deliveryDate
        self.comment = comment
        self.color = color
    
    @staticmethod
    def test_order():
        return OrderData(
            'ArinaTest',
            'Test',
            'улица Пушкина',
            'Сокольники',
            '89000000000',
            2,
            '01.01.2027',
            'Test',
            [],
        )

    def toMap(self) -> dict:
        return {
            'firstName': self.firstName,
            'lastName': self.lastName,
            'address': self.address,
            'metroStation': self.metroStation,
            'phone': self.phone,
            'rentTime': self.rentTime,
            'deliveryDate': self.deliveryDate,
            'comment': self.comment,
            'color': self.color,
        }

    def copyWith(
            self,
            firstName = None,
            lastName = None,
            address = None,
            metroStation = None,
            phone = None,
            rentTime = None,
            deliveryDate = None,
            comment = None,
            color = None,
    ) -> OrderData:
        return OrderData(
            firstName if firstName is not None else self.firstName,
            lastName if lastName is not None else self.lastName,
            address if address is not None else self.address,
            metroStation if metroStation is not None else self.metroStation,
            phone if phone is not None else self.phone,
            rentTime if rentTime is not None else self.rentTime,
            deliveryDate if deliveryDate is not None else self.deliveryDate,
            comment if comment is not None else self.comment,
            color if color is not None else self.color,
        )
