# write your code here
import random
friends_amount = int(input("Enter the number of friends joining (including you):\n").strip())
print()
friends = {}

if friends_amount > 0:
    print("Enter the name of every friend (including you), each on a new line:")

    for i in range(friends_amount):
        friend_name = input().strip()
        friends[f"{friend_name}"] = 0
    print()
    bill_total = int(input("Enter the total bill value:\n").strip())
    print()

    split_bill = bill_total / friends_amount
    lucky_feature = input("Do you want to use the \"Who is lucky?\" feature? Write Yes/No \n").strip()
    print()

    # print(friends)
    if lucky_feature == "Yes":
        split_bill = bill_total / (len(list(friends.items())) - 1)
        lucky_name = random.choice(list(friends.items()))
        print(f"{lucky_name[0]} is the lucky one!")
        print()

        for key in friends:
            if key == lucky_name[0]:
                continue
            else:
                friends[f"{key}"] = split_bill
        print(friends)
        print()
    else:
        print("No one is going to be lucky")
        print()
        for name in friends:
            friends[f"{name}"] = round(split_bill, 2)
        print(friends)
        print()

else:
    print("No one is joining for the party")
