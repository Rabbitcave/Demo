def categorize_age(age):
    if age < 0:
        return "Invalid age"
    elif age <= 1:
        return "Infant"
    elif age <= 12:
        return "Child"
    elif age <= 19:
        return "Teenager"
    else:
        return "Adult"

def main():
    try:
        age = int(input("Please enter the person's age (in years): "))
    except ValueError:
        print("⚠️ Please enter a valid integer.")
        return

    category = categorize_age(age)
    print(f"The person is categorized as: {category}")

if __name__ == "__main__":
    main()
