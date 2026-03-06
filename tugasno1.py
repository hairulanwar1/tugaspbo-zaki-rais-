class Restaurant:
    def _init_(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Nama Restoran:", self.restaurant_name)
        print("Jenis Masakan:", self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name, "sekarang buka!")
        

# Membuat instance
restaurant = Restaurant("Warung Nusantara", "Masakan Indonesia")

# Mencetak atribut secara terpisah
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

# Memanggil method
restaurant.describe_restaurant()
restaurant.open_restaurant()