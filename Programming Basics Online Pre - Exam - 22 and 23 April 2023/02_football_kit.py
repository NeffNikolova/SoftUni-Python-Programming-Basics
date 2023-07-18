shirt_price = float(input())
present_amount = float(input())

shorts_price = 0.75 * shirt_price
socks_price = shorts_price * 0.20
shoes_price = 2 * (shirt_price + shorts_price)

discount = 0.15

money_spent = (shirt_price + shorts_price + socks_price + shoes_price) * (1 - discount)

if money_spent >= present_amount:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {money_spent:.2f} lv.")
else:
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {(present_amount - money_spent):.2f} lv. more.")

