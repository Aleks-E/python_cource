"""
You are given the following code:

class Order:
    morning_discount = 0.25

    def __init__(self, price):
        self.price = price

    def final_price(self):
        return self.price - self.price * self.morning_discount

Make it possible to use different discount programs.
Hint: use strategy behavioural OOP pattern.
https://refactoring.guru/design-patterns/strategy

Example of the result call:

def morning_discount(order):
    ...

def elder_discount(order):
    ...

order_1 = Order(100, morning_discount)
assert order_1.final_price() == 50

order_2 = Order(100, elder_discount)
assert order_1.final_price() == 10
"""



class Order:
    def __init__(self, price, discount):
        self.price = price
        self.discount = discount


    def set_discount(self, discount):
        self.discount = discount


    def final_price(self):
        return self.price - self.price * self.discount()


def morning_discount():
    return 0.2


def elder_discount():
    return 0.4




order_1 = Order(100, morning_discount)
print(order_1.final_price())

order_2 = Order(100, elder_discount)
print(order_2.final_price())

order_1.set_discount(elder_discount)
print(order_1.final_price())


# --------------------------------------------------------


# class Order:
#     def __init__(self, price, discount):
#         self.price = price
#         self.discount = discount
#
#     def set_discount(self, discount):
#         self.discount = discount
#
#     def final_price(self):
#         return self.price - self.price * self.discount.discount()
#
#
# class MorningDiscount:
#     def discount(self):
#         return 0.2
#
#
# class ElderDiscount:
#     def discount(self):
#         return 0.4
#
#
# order_1 = Order(100, MorningDiscount())
# print(order_1.final_price())
#
# order_2 = Order(100, ElderDiscount())
# print(order_2.final_price())
#
# order_1.set_discount(ElderDiscount())
# print(order_2.final_price())








# --------------------------------------------------------

# from __future__ import annotations
# from abc import ABC, abstractmethod
# from typing import List


# class Context():
#     # print("Context")
#     """
#     Контекст определяет интерфейс, представляющий интерес для клиентов.
#     """
#
#     def __init__(self, strategy: Strategy) -> None:
#         print("Context.__init__")
#         """
#         Обычно Контекст принимает стратегию через конструктор, а также
#         предоставляет сеттер для её изменения во время выполнения.
#         """
#
#         self._strategy = strategy
#
#     @property
#     def strategy(self) -> Strategy:
#         """
#         Контекст хранит ссылку на один из объектов Стратегии. Контекст не знает
#         конкретного класса стратегии. Он должен работать со всеми стратегиями
#         через интерфейс Стратегии.
#         """
#
#         return self._strategy
#
#     @strategy.setter
#     def strategy(self, strategy: Strategy) -> None:
#         """
#         Обычно Контекст позволяет заменить объект Стратегии во время выполнения.
#         """
#
#         self._strategy = strategy
#
#     def do_some_business_logic(self) -> None:
#         """
#         Вместо того, чтобы самостоятельно реализовывать множественные версии
#         алгоритма, Контекст делегирует некоторую работу объекту Стратегии.
#         """
#
#         # ...
#
#         print("Context: Sorting data using the strategy (not sure how it'll do it)")
#         result = self._strategy.do_algorithm(["a", "b", "c", "d", "e"])
#         print(",".join(result))
#
#         # ...
#
#
# class Strategy(ABC):
#     # print("Strategy")
#     """
#     Интерфейс Стратегии объявляет операции, общие для всех поддерживаемых версий
#     некоторого алгоритма.
#
#     Контекст использует этот интерфейс для вызова алгоритма, определённого
#     Конкретными Стратегиями.
#     """
#
#     @abstractmethod
#     def do_algorithm(self, data: List):
#         pass
#
#
# """
# Конкретные Стратегии реализуют алгоритм, следуя базовому интерфейсу Стратегии.
# Этот интерфейс делает их взаимозаменяемыми в Контексте.
# """
#
#
# class ConcreteStrategyA(Strategy):
#     # print("ConcreteStrategyA")
#     def do_algorithm(self, data: List) -> List:
#         return sorted(data)
#
#
# class ConcreteStrategyB(Strategy):
#     def do_algorithm(self, data: List) -> List:
#         return reversed(sorted(data))





# if __name__ == "__main__":
#     # Клиентский код выбирает конкретную стратегию и передаёт её в контекст.
#     # Клиент должен знать о различиях между стратегиями, чтобы сделать
#     # правильный выбор.
#
#     context = Context(ConcreteStrategyA())
#     print("Client: Strategy is set to normal sorting.")
#     context.do_some_business_logic()
#     print()
#
#     print("Client: Strategy is set to reverse sorting.")
#     context.strategy = ConcreteStrategyB()
#     context.do_some_business_logic()
















