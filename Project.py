class Phone:
    def __init__(self, model, variant, color):
        self.model = model
        self.variant = variant
        self.color = color
        self.camera = None
        self.battery = None
        self.display_size = None
        self.ram = None
        self.os = None
        self.processor = None
        self.price = None

    def set_specification(self, camera, battery, display_size, ram, os, processor, price):
        self.camera = camera
        self.battery = battery
        self.display_size = display_size
        self.ram = ram
        self.os = os
        self.processor = processor
        self.price = price

    def get_details(self):
        print("\n" + "="*40)
        print(f"{'Phone Details'}")
        print("="*40)
        return {
            "Model": self.model,
            "Variant": self.variant,
            "Color": self.color,
            "Camera": self.camera,
            "Battery": self.battery,
            "Display size": self.display_size,
            "RAM": self.ram,
            "OS": self.os,
            "Processor": self.processor,
            "Price": self.price
        }

class S21(Phone):
    def __init__(self, variant, color):
        super().__init__("Samsung S21", variant, color)
        self.set_specification(
            camera="108 MP + 10 MP + 10 MP + 12 MP",
            battery="5000 mAh",
            display_size="6.8 inches",
            ram="12 GB",
            os="Android 11",
            processor="Exynos 2100",
            price="120000"
        )

class S22(Phone):
    def __init__(self, variant, color):
        super().__init__("Samsung S22", variant, color)
        self.set_specification(
            camera="108 MP + 10 MP + 10 MP + 12 MP",
            battery="4500 mAh",
            display_size="6.7 inches",
            ram="12 GB",
            os="Android 12",
            processor="Snapdragon 888",
            price="150000"
        )

class S23(Phone):
    def __init__(self, variant, color):
        super().__init__("Samsung S23", variant, color)
        self.set_specification(
            camera="200 MP + 10 MP + 10 MP + 12 MP",
            battery="4800 mAh",
            display_size="6.9 inches",
            ram="16 GB",
            os="Android 13",
            processor="Snapdragon 8 Gen 1",
            price="160000"
        )

class Iphone14(Phone):
    def __init__(self, variant, color):
        super().__init__("IPHONE 14", variant, color)
        self.set_specification(
            camera="12 MP + 12 MP",
            battery="3279 mAh",
            display_size="6.1 inches",
            ram="6 GB",
            os="iOS 15",
            processor="A15 Bionic",
            price="70000"
        )

class Iphone15(Phone):
    def __init__(self, variant, color):
        super().__init__("IPHONE 15", variant, color)
        self.set_specification(
            camera="12 MP + 12 MP",
            battery="3400 mAh",
            display_size="6.1 inches",
            ram="6 GB",
            os="iOS 16",
            processor="A16 Bionic",
            price="80000"
        )

class Iphone15pro(Phone):
    def __init__(self, variant, color):
        super().__init__("IPHONE 15 PRO", variant, color)
        self.set_specification(
            camera="48 MP + 12 MP + 12 MP",
            battery="4300 mAh",
            display_size="6.1 inches",
            ram="8 GB",
            os="iOS 16",
            processor="A16 Bionic",
            price="120000"
        )

def phone():
    while True:
        print("-"*40)
        print("Which Phone do you want? ")
        print("1. Samsung")
        print("2. Apple")
        print("Choose your brand:")
        choice1 = input()
        if choice1 == "1" or choice1.upper() == "SAMSUNG":
            selected_phone = samsung()
            if selected_phone:
                details = selected_phone.get_details()
                for key, value in details.items():
                    print(f"{key}: {value}")
        elif choice1 == "2" or choice1.upper() == "APPLE":
            selected_phone = apple()
            if selected_phone:
                details = selected_phone.get_details()
                for key, value in details.items():
                    print(f"{key}: {value}")
        else:
            print("Invalid choice. Please try again.")
            continue
        break

def samsung():
    while True:
        print("-"*40)
        print("Which model in Samsung are you looking for? ")
        print("1. S21")
        print("2. S22")
        print("3. S23")
        print("Choose your preferred model:")
        choose = input()
        
        if choose == "1" or choose.upper() == "S21":
            variant = get_variant()
            color = get_color()
            return S21(variant, color)
        elif choose == "2" or choose.upper() == "S22":
            variant = get_variant()
            color = get_color()
            return S22(variant, color)
        elif choose == "3" or choose.upper() == "S23":
            variant = get_variant()
            color = get_color()
            return S23(variant, color)
        else:
            print("Invalid model. Please try again.")
            
        

def apple():
    while True:
        print("-"*40)
        print("Which Model in Apple are you looking for?")
        print("1. iPhone 14")
        print("2. iPhone 15")
        print("3. iPhone 15 Pro")
        print("Choose your model:")
        choose2 = input()

        if choose2 == "1" or choose2.upper() == "IPHONE 14":
            variant1 = get_variant1()
            color = get_color()
            return Iphone14(variant1, color)
        elif choose2 == "2" or choose2.upper() == "IPHONE 15":
            variant1 = get_variant1()
            color = get_color()
            return Iphone15(variant1, color)
        elif choose2 == "3" or choose2.upper() == "IPHONE 15 PRO":
            variant1 = get_variant1()
            color = get_color()
            return Iphone15pro(variant1, color)
        else:
            print("Invalid model. Please try again.")
            

def get_variant():
    while True:
        print("-"*40)
        print("Choose Your Variant: ")
        print("1. 128GB")
        print("2. 256GB")
        variant = input().upper()
        if(variant.upper() == "128GB"):
            return variant.upper()
        elif(variant.upper() == "256GB"):
            return variant.upper()
        else:
            print("Invalid variant,Try again!")
            

def get_color():
    while True:
        print("-"*40)
        print("Which color do you want: ")
        print("1. White")
        print("2. Black")
        print("3. Silver")
        color = input().upper()
        if(color.upper() == "WHITE"):
            return color
        elif(color.upper() == "BLACK"):
            return color
        elif(color.upper() == "SILVER"):
            return color
        else:
            print("Invalid color choice")

def get_variant1():
    while True:
        print("-"*40)
        print("Choose Your Variant: ")
        print("1. 128GB")
        print("2. 256GB")
        print("3. 512GB")
        variant1 = input().upper()
        if(variant1.upper() == "128GB"):
            return variant1.upper()
        elif(variant1.upper() == "256GB"):
            return variant1.upper()
        elif(variant1.upper() == "512GB"):
            return variant1.upper()
        else:
            print("Invalid variant")

def main():
    print("-" * 40)
    print("Purchasing a Phone: ")
    print("-" * 40)
    while True:
        try:
            print("Do you want a Phone?")
            print("1. YES")
            print("2. NO")
            print("Enter your response: ")
            choice = input().strip().upper()
            
            if choice == "1" or choice == "YES":
                phone()
                break
            elif choice == "2" or choice == "NO":
                print("Thanks for the response.")
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    print("=" * 40)

main()
