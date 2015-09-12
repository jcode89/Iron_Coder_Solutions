def fizz_buzz(n):
    fin_list = []
    for number in range(1, n + 1):
        if number % 3 == 0 and number % 5 == 0:
            fin_list.append('fizzbuzz')
        elif number % 3 == 0:
            fin_list.append('fizz')
        elif number % 5 == 0:
            fin_list.append('buzz')
        else:
            fin_list.append(number)
    return fin_list