def is_armstrong(number: int) -> bool:
    number_length = len(str(number))
    power_sum = 0
    for digit in str(number):
        power_sum += int(digit) ** number_length

    return power_sum == number
