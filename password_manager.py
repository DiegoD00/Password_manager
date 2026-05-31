def password_management():
   
    option = ""

    while option != "4":
        print("\n")
        print("1. Add account")
        print("2. View accounts")
        print("3. Search accounts")
        print("4. Exit\n")

        option = input("Select an option: \n")

        if option == "1":
            website = input("Enter the website: ")
            username = input("Enter the username: ")
            password = input("Enter the password: \n")
            with open("password.txt", "a") as f:
                f.write(f"{website},{username},{password}\n")
       
       
        elif option == "2":
    
            try:
                with open("password.txt") as f:
                    for line in f:
                        line = line.strip()
                        website, username, password = line.split(",")
                        print(f"\nWebsite: {website} | Username: {username} | Password: {password}")
                    print("\n")
            except FileNotFoundError:
                print("No accounts found.\n")

        elif option == "3":
            search_website = input("Enter the website to search for: \n")
            found = False
    
            try:
                for data in open("password.txt"):
                    data = data.strip()
                    website, username, password = data.split(",")
                    if search_website.lower() == website.lower():
                        found = True
                        print(f"Website: {website} | Username: {username} | Password: {password}\n")
                if not found:
                    print("No accounts found for the specified website.\n")
            except FileNotFoundError:
                print("No accounts found.\n")

        elif option == "4":
            print("\nExiting the application. Goodbye!\n")
        else:
            print("\nInvalid option. Please try again.\n")

password_management()



    
