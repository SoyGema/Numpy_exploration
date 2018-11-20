
## bonAppetit has the following parameter(s):

    # bill: an array of integers representing the cost of each item ordered
    # k: an integer representing the zero-based index of the item Anna doesn't eat
    # b: the amount of money that Anna contributed to the bill




def bonAppetit(bill, k, b):

    b_actual = int((sum(bill) - bill[k]) / 2 )
    b_charged = int(b_actual + (bill[k] / 2))


    if b_charged - b_actual != 0:
        print(b_charged - b_actual)
    if b_charged == b_actual:
        print('Bon Apetit')
