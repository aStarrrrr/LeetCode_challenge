def armstrong(number):
    input_number = str(number)
    size = len(input_number)
    sum_out = 0
    for digit in input_number:
        sum_out += int(digit)**size
    if sum_out == number:
        print("Armstrong")
    else:
        print("Not armstrong")
armstrong(153)