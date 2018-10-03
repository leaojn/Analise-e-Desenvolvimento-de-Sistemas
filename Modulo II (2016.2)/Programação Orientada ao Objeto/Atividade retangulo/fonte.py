from teste import Retangulo
from teste import Ponto

def main():
	
	print ("Retangulo 1")
	pontos1 = Ponto(10,3)
	rect1 = Retangulo(5,8)
	rect1.perimetro()
	rect1.area()
	rect1.base_altura()
	pontos1.x_y()


	print ("Retangulo 2")
	rect2 = Retangulo(4,6)
	rect2.perimetro()
	rect2.area()
	rect2.base_altura()
	comparation()

def comparation():
	print (rect1)


if __name__ == '__main__':
	main()