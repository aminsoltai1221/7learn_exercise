from abc import ABC, abstractmethod

class ProductBase(ABC):
    
    @abstractmethod
    def detail(self):
        pass
    
    @abstractmethod
    def price(self):
        pass




class SUV(ProductBase):
    def __init__(self, name : str, price : int, brand, built_year,model):
        self._price = price
        self.name = name
        self.brand = brand
        self.built_year = built_year
        self.model = model
        
    
    @property
    def price(self):
        return SUVPrice(self)
        
    
    @property
    def detail(self):
        return SUVDetail(self)



class Coupe(ProductBase):
    def __init__(self, name : str, price : int, brand, built_year,model):
        self._price = price
        self.name = name
        self.brand = brand
        self.built_year = built_year
        self.model = model
        
    
    @property
    def price(self):
        return CoupePrice(self)
        
    
    @property
    def detail(self):
        return CoupeDetail(self)




class ShowBase(ABC):
    @abstractmethod
    def show(self):
        pass


class SUVPrice(ShowBase):
    
    def __init__(self, car):
        self.car = car

    
    def show(self):
        return f"car price = {self.car._price}"


class SUVDetail(ShowBase):
    
    def __init__(self, car):
        self.car = car
            
    def show(self):
        return f"car name = {self.car.name} ,car brand = {self.car.brand} ,car built_year = {self.car.built_year} ,car model = {self.car.model}"
    

class CoupePrice(ShowBase):
    
    def __init__(self, car):
        self.car = car
    
    def show(self):
        return f"car price = {self.car._price}"
    
    
class CoupeDetail(ShowBase):
    
    def __init__(self, car):
        self.car = car
        
    def show(self):
        return f"car name = {self.car.name} ,car brand = {self.car.brand} ,car built_year = {self.car.built_year} ,car model = {self.car.model}"
    

if __name__ == "__main__":
    
    car1 = SUV("X6", 30000, "BMW", 2024, "hybrid")
    car2 = SUV("Elg", 31000, "Benz", 2023, "v3")
    car3 = Coupe("S3", 32000, "BMW", 2024, "hybrid")
    car4 = Coupe("Elg", 31500, "Benz", 2022, "Coupe")
    
    for i in [car1, car2, car3, car4]:
        print(i.detail.show())
        print(i.price.show())
