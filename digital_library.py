import pandas as pd
try:
    df = pd.read_csv("library.csv", encoding="latin1")
except:
    df = pd.DataFrame(columns=["ID", "Book Name", "Author Name", "Year", "Availability"])

while True:
    print("\n--- Library Menu ---")
    print("1. View all books")
    print("2. Add a new book")
    print("3. Search book by title")
    print("4. Issue a book")
    print("5. Return a book")
    print("6. Save and Exit")

    choice = input("Enter your Choice: ")
    if choice == "1":
        print(df)
    elif choice == "2":
        id = input("Enter your Book ID: ")
        name = input("Enter your Book name: ")
        author = input("Enter Author's name: ")
        year = input("Enter year: ")
        availability = "yes"

        new_row = pd.DataFrame([{
            "ID": id,
            "Book Name": name,
            "Author Name": author,
            "Year": year,
            "Availability": availability
        }])

        df = pd.concat([df, new_row], ignore_index=True)

        print("Book added!")
    elif choice == "3":
        title = input("Enter book name: ")
        result = df[df["Book Name"].str.lower() == title.lower()]

        if not result.empty:
            print("Book found:")
            print(result)
        else:
            print("Book not found.")
    elif choice == "4":
        title = input("Enter book name to issue: ")
        idx = df[df["Book Name"].str.lower() == title.lower()].index

        if not idx.empty and df.loc[idx[0], "Availability"].lower() == "yes":
            df.loc[idx[0], "Availability"] = "no"
            print("Book issued successfully!")
        else:
            print("Book not found or already issued.")
    elif choice == "5":
        title = input("Enter book name to return: ")
        idx = df[df["Book Name"].str.lower() == title.lower()].index

        if not idx.empty and df.loc[idx[0], "Availability"].lower() == "no":
            df.loc[idx[0], "Availability"] = "yes"
            print("Book returned successfully!")
        else:
            print("Book was not issued or not found.")
    elif choice == "6":
        df.to_csv("library.csv", index=False)
        print("Library saved. Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")
