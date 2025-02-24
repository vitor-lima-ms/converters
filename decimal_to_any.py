"""Decimal number to any base"""

N_BASE10: int = 119
BASE: int = 2

quotient: int = int()
div_remainder: int = int()
quotient_list: list[int] = list()
div_remainder_list: list[int] = list()
counter: int = int()

while True:
    
    if counter == 0:
        quotient: int = N_BASE10 // BASE #Quotient
        div_remainder: int = N_BASE10 % BASE #Remainder
        quotient_list.append(quotient)
        div_remainder_list.append(div_remainder)
        counter += 1

    else:
        quotient = quotient_list[-1] // BASE
        div_remainder = quotient_list[-1] % BASE
        quotient_list.append(quotient)
        div_remainder_list.append(div_remainder)
    
    if quotient_list[-1] == 0:
        break

ordered_div_remainder_list = div_remainder_list[::-1]

result = str()
for remainder in ordered_div_remainder_list:
    result += str(remainder)

print(f'The number in base {BASE} equivalent to the decimal number {N_BASE10} is {result}')