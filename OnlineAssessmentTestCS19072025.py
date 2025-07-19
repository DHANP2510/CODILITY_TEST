"""Question: You are given two arrays A and B of N strings each, and an array C of N positive integers. 
             They describe N monthly expenses (numbered from 0 to N-1) set up on an account. 
             The K-th expense charges the account with an amount C[K] at the end of each month, starting from month A[K] and ending in month B[K] (inclusive). 
            
             The format of each string is "MM-YYYY" (where MM denotes month, between 01 and 12, and YYYY denotes year, between 1900 and 2100), 
             for example: "06-2021". What is the minimum monthly income needed for all of these charges to be paid? We cannot go into debt. 
             
             In other words, the amount of money that remains in the account at the end of each month (after all the payments) should not drop below 0. 
             The monthly income starts in the earliest month given in array A. The income is transfered onto the account at the beginning of the month, 
             i.e. income for a given month is always on the account before any of the charges are payed. 
             
             The balance that remains in the Write a function: def solution (A, B, C) that, given arrays A and B consisting of N strings each 
             and an array C consisting of N positive integers, representing the expenses as described above, 
             returns the minimum monthly income needed to cover all of the expenses. 
             
             Examples: 1. Given A = ["03-2021", "04-2021", "05- 2021], B = ["03-2021", "05-2021", "05- 2021"], and C = [20, 10, 15], the function should return 20. 
                       The total expenses are: 20 (in March), 10 (in April) and 25 (in May). Starting with income 20 (in March), 
                       the total balance at the end of each month will be: 0 (in March), 10 (in April), and 5 (in May) write simple biggner friendly solution
"""
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

    
