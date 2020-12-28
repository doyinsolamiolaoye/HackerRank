# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    return round(meal_cost*(1 + (tip_percent/100) + (tax_percent/100)))

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    print(solve(meal_cost, tip_percent, tax_percent))