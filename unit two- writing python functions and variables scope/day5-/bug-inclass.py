def input_bug_counts(bug_type):
    count = int(input(f"Enter the count of {bug_type} bugs: "))
    return count
def calculate_percent(total, count):
    percentage = (count / total) * 100
    return percentage
def input_bug_type_and_count():
    bug_type = input("Enter the type of bug: ")
    count = input_bug_counts(bug_type)
    return bug_type, count
def display_table(bug1, count1, bug2, count2, bug3, count3):
    total = count1 + count2 + count3
    percent1 = calculate_percent(total, count1)
    percent2 = calculate_percent(total, count2)
    percent3 = calculate_percent(total, count3)

    print("Bug Type    Count    Percentage")
    print("="*40)
    print(f"{bug1:>10}{count1:^10}{percent1:.2f}%")
    print(f"{bug2:>10}{count2:^10}{percent2:.2f}%")
    print(f"{bug3:>10}{count3:^10}{percent3:.2f}%")
    print("="*40)
    print(f"total {total:^10}")
bug1_type, bug1_count = input_bug_type_and_count()
bug2_type, bug2_count = input_bug_type_and_count()
bug3_type, bug3_count = input_bug_type_and_count()
display_table(bug1_type, bug1_count, bug2_type, bug2_count, bug3_type, bug3_count)

                    