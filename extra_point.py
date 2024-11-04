# Program to calculate the average of a list of numbers

def get_numbers():
    print("Enter numbers separated by spaces:")
    numbers = ""
    while numbers == "":
        numbers = input(">>> ") 
    number_list = numbers.split(" ")
    return [int(num) for num in number_list if num != ""]

def calculate_average(nums):
    total = sum(nums)
    avg = total / len(nums)  
    return avg

def main():
    print("This program calculates the average of your input numbers.")
    numbers = get_numbers()
    average = calculate_average(numbers)
    print(f"The average is: {average}")

# Run the program
if __name__ == "__main__":
    main()
