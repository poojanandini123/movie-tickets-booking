from abc import ABC, abstractmethod

class Theatre:
    def __init__(self, name, movies):
        self.name = name
        self.movies = movies

    def show_movies(self):
        print(f"\n---Movies---")
        for movie, price in self.movies.items():
            print(f"{movie} : ₹{price}")

class PaymentRule(ABC):
    @abstractmethod
    def pay(self, amount):
        pass 

class UPIPayment(PaymentRule):
    def pay(self, amount):
        print(f"✅ Paid ₹{amount} via UPI")

class CardPayment(PaymentRule):
    def pay(self, amount):
        print(f"✅ Paid ₹{amount} via Card")

class CounterCash(PaymentRule):
    def pay(self, amount):
        print(f"💰 ₹{amount} to be paid at counter")


class Customer:
    def __init__(self, name, number):
        self.name = name
        self.number = number 

class Booking:
    def __init__(self, theatre, customer):
        self.theatre = theatre
        self.customer = customer
        self.movie = ""   
        self.tickets = 0
       

    def select_movie(self, movie_name):
        if movie_name in self.theatre.movies:
            self.movie = movie_name
            self.tickets = int(input("Enter number of tickets: "))
            price = self.theatre.movies[movie_name]
            self.total = self.tickets * price
            print(f"✅ {movie_name} booked successfully")
        else:
            print("❌ Movie not available")

    def calculate_total(self):
        return self.total

    def show_summary(self):
        if self.movie == "":  
            print("No booking done")
            return

        print("\nBooking Summary:")
        print(f"Theatre : {self.theatre.name}")
        print(f"Customer : {self.customer.name}")
        print(f"Movie : {self.movie}")
        print(f"Tickets : {self.tickets}")
        print(f"Total Bill : ₹{self.total}")
        print(f"Paid via : {self.payment_method}")


def main():
    print("Welcome to pooja Online Movie Ticket Booking App")
    name = input("Enter your name: ")
    mobile = input("Enter your mobile number: ")
    customer = Customer(name, mobile)

    gowri_Movies = {
        "RAAKA": 300 }

    ganga_movies = {
        "pushpa": 150
       
    }

    RRR_movies = {
        "UStaad": 110
    }
    print("\n1. Allu Cinemas")
    print("2. AAA")
    print("3. RRT")

    choice = input("Choose your Theatre: ")

    match choice:
        case "1":
            theatre = Theatre("Allu Cinemas", gowri_Movies)
        case "2":
            theatre = Theatre("AAA", ganga_movies)
        case "3":
            theatre = Theatre("RRT", RRR_movies)
   
        case _:
            print("Invalid option")
            return

    theatre.show_movies()

    booking = Booking(theatre, customer)

    movie_name = input("\nEnter movie name: ")
    booking.select_movie(movie_name)

    total_amount = booking.calculate_total()
    if total_amount == 0:
        return

    print("\nChoose Payment Mode")
    print("1: Via Card")
    print("2: Via UPI")
    print("3: Pay at Counter")

    choice = input("Select 1 or 2 or 3: ")

    if choice == "1":
        payment = CardPayment()
    elif choice == "2":
        payment = UPIPayment()
    elif choice == "3":
        payment = CounterCash()
    else:
        print("Invalid choice")
        return

    booking.payment_method = type(payment).__name__

    payment.pay(total_amount)
    booking.show_summary()

if __name__ == "__main__":
    main()



