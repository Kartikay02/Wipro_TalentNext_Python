def main():
    try:
        filename = input("Enter the file name: ")
        total_items = 0
        free_items = 0
        total_amount = 0
        discount = 0
        
        with open(filename + ".txt", "r") as file:
            for line in file:
                entry = line.strip()
                if not entry:
                    continue  # Skip blank lines
                parts = entry.split()
                
                if parts[0].lower() == "discount":
                    try:
                        discount = int(parts[1])
                    except (IndexError, ValueError):
                        print("Invalid discount entry. Skipping...")
                    continue

                if len(parts) != 2:
                    print(f"Invalid line format: '{entry}'. Skipping...")
                    continue
                
                item, price = parts
                if price.lower() == "free":
                    free_items += 1
                else:
                    try:
                        total_amount += int(price)
                        total_items += 1
                    except ValueError:
                        print(f"Invalid price value for '{item}'. Skipping...")

        final_amount = total_amount - discount
        
        print(f"No of items purchased: {total_items}")
        print(f"No of free items: {free_items}")
        print(f"Amount to pay: {total_amount}")
        print(f"Discount given: {discount}")
        print(f"Final amount paid: {final_amount}")

    except FileNotFoundError:
        print("File not found. Please check the file name and try again.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()



