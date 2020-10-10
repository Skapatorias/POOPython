class Coordenada:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia (self, otra_coordenada):
        x_diff = (self.x - otra_coordenada.x)**2
        y_diff = (self.y - otra_coordenada.y)**2

        return (x_diff + y_diff)**0.5


if __name__ == "__main__":
    cord1 = Coordenada(20,20)
    cord2 = Coordenada(10,5)

    print (cord1.distancia(cord2))
    
    print (isinstance(cord2, Coordenada))
    print (isinstance(cord1, Coordenada))