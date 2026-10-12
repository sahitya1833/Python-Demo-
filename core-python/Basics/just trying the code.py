def generate_harmonic_series(n):
    """
    Generates the terms of a harmonic series up to n terms
    and calculates their total sum.
    """
    if n <= 0:
        print("Please enter a positive integer greater than 0.")
        return

    terms = []
    total_sum = 0.0

    print(f"\nHarmonic Series for {n} terms:")

    for i in range(1, n + 1):
        # Calculate the current term
        term_value = 1 / i
        total_sum += term_value

        # Format the term as a string (e.g., "1/3")
        terms.append(f"1/{i}")

    # Join the terms to display the complete series layout
    series_string = " + ".join(terms)
    print(series_string)
    print(f"Total Sum: {total_sum:.6f}")


# Example usage:
try:
    num_terms = int(input("Enter the number of terms: "))
    generate_harmonic_series(num_terms)
except ValueError:
    print("Invalid input! Please enter a valid integer.")