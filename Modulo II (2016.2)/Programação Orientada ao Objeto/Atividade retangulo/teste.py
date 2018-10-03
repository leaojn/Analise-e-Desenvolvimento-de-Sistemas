class Retangulo():
	
	def __init__(self, largura, altura):
		self.largura = largura
		self.altura = altura
		largura = self.largura
	def base_altura(self):
		print ("Largura:",self.largura ,"Altura", self.altura)

	def perimetro(self):
		perimetro = (self.largura * 2 ) + (self.altura * 2)
		print ("Perimetro:", perimetro)
	def area(self):
		area = self.largura * self.altura
		print ("Area:", area)

class Ponto():
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def x_y(self):
		print("x:",self.x,"y:",self.y)
class App():
	