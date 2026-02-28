from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    customer_list = []
    for one_customer in customers:
        customer_list.append(Customer(one_customer["name"],
                                      one_customer["food"]))
        one_customer = Customer(one_customer["name"], one_customer["food"])
        CinemaBar.sell_product(one_customer, one_customer.food)
    clean = Cleaner(cleaner)
    CinemaHall(hall_number).movie_session(movie, customer_list, clean)
    Cleaner(cleaner)
