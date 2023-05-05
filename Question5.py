def check_matching_values(arr1, arr2):
    for val in arr1:
        if val in arr2:
            print(f"Matching value found: {val}")


# Example arrays
arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 6, 7, 8, 9]

# Call the function
check_matching_values(arr1, arr2)