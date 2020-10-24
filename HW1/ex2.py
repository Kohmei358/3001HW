def ispalindrome(arr):
    # Base case 1:
    # An empty array is always palindrome -> return True
    if not arr:
        return True

    # Base case 2:
    # An array of a single element is always palindrome -> return True
    if len(arr) == 1:
        return True

    # Base case 3:
    # If the first and last elements of arr are not identical ,
    # the array is not palindrome -> return False
    if arr[0] != arr[-1]:
        return False
    # If we get here it's because the first and last
    # elements are identical , therefore :
    else:
        # Recursive call :
        # Call ispalindrome () dropping the first and last
        # elements of arr
        return ispalindrome(arr[1:-1])


# --- Test Cases
# #Assert => True
# print(ispalindrome([]))
# #Assert => True
# print(ispalindrome([1, 1]))
# #Assert => True
# print(ispalindrome([1, 2, 3, 2, 1]))
# #Assert => True
# print(ispalindrome([1, 2, 9, 9, 9, 9, 2, 1]))
# #Assert => False
# print(ispalindrome([1, 2, 9, 9, 8, 9, 2, 1]))
# #Assert => False
# print(ispalindrome([1, 3]))
