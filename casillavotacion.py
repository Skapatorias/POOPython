class CasillaDeVotacion:

    def __init__(self, identificador, pais):
        self._identificador = identificador
        self._pais = pais
        self._region = None

    @property
    def region(self):
        return self._region

    @region.setter
    def set_region(self, region):
        if region in self._pais:
            self._region = region
        else:

            raise ValueError(f'La region {region} no es valida en {self._pais}')


casilla = CasillaDeVotacion(123,['Mexico','Morelos'])
print(casilla.set_region)
casilla.set_region = 'Mexico'
print(casilla.set_region)