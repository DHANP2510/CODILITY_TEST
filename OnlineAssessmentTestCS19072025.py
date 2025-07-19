"""Question: """
"""Solution: """
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, C):
    from datetime import datetime, date

    # Implement your solution here
    a_date = [datetime.strptime(i, "%m-%Y").date() for i in A]
    b_date = [datetime.strptime(i, "%m-%Y").date() for i in B]

    date_range_dict = {}
    x = min(a_date)

    while x <= max(b_date):
        if x.month == 12:
            next_month = 1
            next_year = x.year + 1
        else:
            next_month = x.month + 1
            next_year = x.year
        x = date(next_year, next_month, 1)
        date_range_dict[x] = 0
    
    for i, j, k in zip(a_date, b_date, C):
        date_range_dict[i] = date_range_dict.get((i), 0) + k
        while i < j:
            if i.month == 12:
                next_month = 1
                next_year = i.year + 1
            else:
                next_month = i.month + 1
                next_year = i.year
            i = date(next_year, next_month, 1)
            date_range_dict[i] = date_range_dict.get((i), 0) + k
    
    date_dict = {key.strftime("%m-%Y"): value for key, value in sorted(date_range_dict.items())}
    #print(date_dict)
    
    flag = 0
    
    for i in range (1, 21):
        if flag == 1:
            break
        remainder = 0
        monthly_income = i 
        for key, value in date_dict.items():
            if (monthly_income + remainder - value) < 0:
                monthly_income = -1
                break
            remainder = monthly_income + remainder - value 
        else:
            flag = 1

    #print(monthly_income)
    return monthly_income


print(solution(["03-2021", "04-2021", "05-2021"], 
               ["03-2021", "05-2021", "05-2021"], 
               [20, 10, 15]))

print(solution(["10-2020", "01-2020", "02-2020", "06-2021"], 
               ["07-2021", "03-2020", "10-2020", "07-2021"], 
               [1, 10, 2, 90]))

print(solution(["01-1900", "12-2099", "11-2099", "01-1901"], 
               ["12-1901", "12-2099", "12-2100", "01-1902"], 
               [1, 1000, 998, 1]))    

    
