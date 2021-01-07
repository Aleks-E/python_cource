from hw11.task_2 import Order


def test_set_new_strategy():
    def morning_discount(order_price):
        return order_price - order_price * 0.2

    def elder_discount(order_price):
        return order_price - order_price * 0.4

    price = 100
    order_1 = Order(price, morning_discount)
    assert order_1.final_price() == 80
    order_1.set_discount(elder_discount)
    assert order_1.final_price() == 60
