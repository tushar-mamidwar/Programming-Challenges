import math
def take_input():
    number_of_students=-1
    expenditure_list=[]
    no_of_students_list=[]
    while True:
        number_of_students=int(input())
        if number_of_students == 0:
            break
        no_of_students_list.append(number_of_students)
        students_expediture_in_one_trip=[]
        for i in range(number_of_students):
            exp=float(input())
            students_expediture_in_one_trip.append(exp)
        expenditure_list.append(students_expediture_in_one_trip)
    calculate_exchange_amount(expenditure_list,no_of_students_list)

def calculate_exchange_amount(expenditure_list,no_of_students_list):
    for i in range(len(expenditure_list)):
        avg=sum(expenditure_list[i])/no_of_students_list[i]
        exchange_amount=0
        give_money=0
        for j in expenditure_list[i]:
            if j<avg:
                exchange_amount+=math.floor((avg-j)*100)/100
            else:
                give_money+=math.floor((j-avg)*100)/100
        print(max(exchange_amount,give_money))
take_input()