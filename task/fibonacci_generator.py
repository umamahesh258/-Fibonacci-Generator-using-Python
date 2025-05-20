# Fibonacci Generator - Detailed Version with Iteration and Recursion Options

def fibonacci_iterative(n):
    """Generate Fibonacci series using iteration."""
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def fibonacci_recursive(n):
    """Generate nth Fibonacci number using recursion (not efficient for large n)."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def get_fibonacci_series_recursive(n):
    """Build the full series recursively."""
    return [fibonacci_recursive(i) for i in range(n)]

def main():
    print("=" * 50)
    print("📌 Welcome to the Fibonacci Series Generator")
    print("=" * 50)
    
    while True:
        try:
            # Asking user for number of terms
            n = int(input("Enter how many Fibonacci numbers you'd like to generate: "))
            if n <= 0:
                print("⚠️ Please enter a **positive integer** greater than 0.")
                continue
        except ValueError:
            print("❌ Invalid input. Please enter a valid integer.")
            continue

        print("\nChoose the method for generating Fibonacci series:")
        print("1. Iterative (Fast and Efficient)")
        print("2. Recursive (Slow for large n, but elegant)")

        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            series = fibonacci_iterative(n)
            print("\n✅ Fibonacci series (Iterative Method):")
        elif choice == '2':
            if n > 30:
                print("⚠️ Recursive method is not recommended for n > 30 due to performance issues.")
                confirm = input("Do you still want to proceed with recursion? (y/n): ")
                if confirm.lower() != 'y':
                    continue
            series = get_fibonacci_series_recursive(n)
            print("\n✅ Fibonacci series (Recursive Method):")
        else:
            print("❌ Invalid choice. Please select 1 or 2.")
            continue

        print(" -> ".join(str(num) for num in series))
        print("=" * 50)

        again = input("Do you want to generate another series? (y/n): ")
        if again.lower() != 'y':
            print("🎉 Thank you for using the Fibonacci Generator. Goodbye!")
            break

# Run the main function
if __name__ == "__main__":
    main()
