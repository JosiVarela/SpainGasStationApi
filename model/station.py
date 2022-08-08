class Station:
    def __init__(self, name, cp, direction, schedule, latitude, locality, longitude, city, province, sell_type,
                 biodiesel, bioetanol, gas_natural_comp, gas_natural_licuado, gas_licuado_petroleo, gasoleo_a,
                 gasoleo_b, gasoleo_premium, gasolina_95_e10, gasolina_95_e5, gasolina_95_e5_premium, gasolina_98_e10,
                 gasolina_98_e5, hidrogeno):
        self.name = name
        self.cp = cp
        self.direction = direction
        self.schedule = schedule
        self.latitude = latitude
        self.locality = locality
        self.longitude = longitude
        self.city = city
        self.province = province
        self.sell_type = sell_type
        self.biodiesel = biodiesel
        self.bioetanol = bioetanol
        self.gas_natural_comp = gas_natural_comp
        self.gas_natural_licuado = gas_natural_licuado
        self.gas_licuado_petroleo = gas_licuado_petroleo
        self.gasoleo_a = gasoleo_a
        self.gasoleo_b = gasoleo_b
        self.gasoleo_premium = gasoleo_premium
        self.gasolina_95_e10 = gasolina_95_e10
        self.gasolina_95_e5 = gasolina_95_e5
        self.gasolina_95_e5_premium = gasolina_95_e5_premium
        self.gasolina_98_e10 = gasolina_98_e10
        self.gasolina_98_e5 = gasolina_98_e5
        self.hidrogeno = hidrogeno

    @staticmethod
    def from_dict(stations):
        return Station(stations['Rótulo'],
                       stations['C.P.'],
                       stations['Dirección'],
                       stations['Horario'],
                       stations['Latitud'],
                       stations['Localidad'],
                       stations['Longitud (WGS84)'],
                       stations['Municipio'],
                       float(stations['Precio Biodiesel'].replace(',', '.')) if stations['Precio Biodiesel'] != ''
                       else None,

                       )