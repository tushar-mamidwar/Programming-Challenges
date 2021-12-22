test_cases = int(input())
output_list = []
for i in range(test_cases):
    working_days_lost = 0
    days = int(input())
    no_of_parties = int(input())
    hartals = []
    for j in range(no_of_parties):
        hartals.append(int(input()))

    for day in range(1, days + 1):
        if day % 7 != 6 and day % 7 != 0:
            for hartal in hartals:
                if day % hartal == 0:
                    working_days_lost += 1
                    break
    output_list.append(working_days_lost)
for output in output_list:
    print(output)
