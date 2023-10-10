from dataclasses import dataclass
from datetime import date
from typing import List


@dataclass
class Customer:
    id: int
    last_name: str
    first_name: str
    middle_name: str
    address: str
    card_number: int
    bank_namber: int


    @classmethod
    def create_customers(cls):
        customer = list()

        customer.append(
            cls(1, 'Чауш', 'Энвер', 'Ленурович', 'ул. Пушкина, д.11', 11111111111, 121234))
        customer.append(
            cls(2, 'Чауш', 'Сервер', 'Ленурович', 'ул. Ленина, д.8', 11111111113, 127434))
        customer.append(
            cls(3, 'Мамутов', 'Эрнест', 'Ленурович', 'ул. Гоголя, д.40', 11111111110, 12334))
        customer.append(
            cls(4, 'Абкеримов', 'Эльмир', 'Абкуермович', 'ул. Изумрудная, д.1', 11111111112, 12634))
        return customer


class Filter:
    def __init__(self, customer: List[Customer]):
        self.customer = customer
    
    def get_customers_alf(self, *_):
        print('а) список в алф порядке.', sorted(self.customer,key=lambda x: x.last_name), sep='\n', end='\n\n')

    def get_customers_num(self, *, min: int, max: int):
        print(
            'd) список номеров.',
            *filter(lambda customer: customer.card_number >= min and customer.card_number <= max, self.customer),
            sep='\n', end='\n\n'
        )


customers_list = Customer.create_customers()
customer_filter = Filter(customers_list)

customer_filter.get_customers_alf()
customer_filter.get_customers_num(min= 11111111111, max = 11111111114)