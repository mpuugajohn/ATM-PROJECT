#Step 1 setting variables
pin = 2026
balance = 1000000
attempts = 0


# Step 2: Input the PIN
while attempts < 3:
    entered_pin = int(input("Enter PIN: "))

    if entered_pin == pin:
        print("Thank you,You are successful!")
        break
    else:
        attempts += 1
        print("Invalid Input PIN.")
        print("You have", 3 - attempts, "tries left.")

# If the user fails all 3 attempts
if attempts == 3:
    print("Invalid,BLOCKED!")

else:
    # Step 3: Show the continuous menu
    while True:
        print("\n*** ATM MENU ***")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

      # Step  4: Choices

        if choice == '1':
            print("Your current balance is:", balance)

        elif choice == '2':
      # Step 5: Deposits
            amount = float(input("Enter amount to deposit: "))

            if amount > 0:
                balance += amount
                print("Deposit successful!")
                print("Your new balance is:", balance)
            else:
                print("Error: Deposit amount must be greater than zero.")

        elif choice == '3':
      # Step  5: Withdrawals
            amount = float(input("Enter amount to withdraw: "))

            if amount <= 0:
                print("Error: Enter an amount greater than 0.")
            elif amount > balance:
                print("Error: You do not have enough money!")
            else:
                balance -= amount
                print("Cash dispensed:", amount)
                print("Your new balance is:", balance)

        elif choice == '4':
            print("OUR ESTEEMED CUSTOMER,Thank you!")
            break

        else:
            print("Invalid choice! Please enter 1, 2, 3, or 4.")