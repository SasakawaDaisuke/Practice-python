class Car(object):
    def __init__(self, model_name, mileage, manufacturer):
        self.model_name = model_name
        self.mileage = mileage
        self.manufacturer = manufacturer

    def gas(self):
        print(f"{self.model_name}アクセル全開")

    def breakes(self):
        print()
if __name__ == "__main__":
    prius = Car("Prius", 20, "TOYOTA")
    print(prius.model_name)
    prius.gas()
