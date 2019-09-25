def binary_search(L, x):
    left, right = 0, len(L) - 1

    while left <= right:
        mid = (left + right) // 2 # integer division

        if L[mid] == x:
            return mid # We have found our element

        if L[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return -1 # We have not found our element

# This code is to test the above code

if __name__ == "__main__":
    L = [1, 2, 3, 5, 6, 7, 8, 9]

    for x in range(1, 11):
        position = binary_search(L, x)

        if position == -1: # Binary search did not find x so it returned -1

            if x in L:
                print(x,"is in L, but function returned -1")
            else:
                print(x,"not in List")
        else:
            if L[position] == x:
                print(x, "found in correct position.")
            else:
                print("binary search returned", position,"for",x,"which is incorrect")
    print("program terminated")



