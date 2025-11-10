# Check if all the odd indices are alphabets and even indices are digits
# Given a string, check if all the odd indices are alphabets and the even indices are digits.

# Note: indices starts from 0.


# template code


# def is_odd_indices_alpha_and_even_indices_digits(string: str) -> bool:
#     '''
#     Given a string, check if all the odd indices are alphabets and the even indices are digits.

#     Note: indices starts from 0.

#     Arguments:
#     string: str - the input string

#     Return:
#     bool - True if all odd indices are alphabets and even indices are digits, else False
#     '''
    
def is_odd_indices_alpha_and_even_indices_digits(string :str) -> bool :
    for i in range(len(string)):
        if (i % 2 ==0):
            digits = '0123456789'
            if (string[i] in digits):
                return (True)
            else :
                return (False)
        elif (i % 2 != 0):
            alphas = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
            if (string[i] in alphas):
                return (True)
            else:
                return (False)

    if (is_odd_indices_alpha_and_even_indices_digits(string) == True):
        return True
    else:
        return False

a = is_odd_indices_alpha_and_even_indices_digits("1e2l3")
print (a)


# def is_odd_indices_alpha_and_even_indices_digits(string : str) -> bool:
#     len_string