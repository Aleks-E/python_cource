def is_armstrong(number: int) -> bool:
    number_length = len(str(number))
    power_sum = 0
    for i in str(number):
        power_sum += int(i) ** number_length

    return power_sum == number
