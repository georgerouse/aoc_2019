if __name__ == '__main__':    
    num_list = [str(i) for i in range(347312, 805915+1)]
    password_count = 0
    
    for num in num_list:
        # Check two adjacent digits
        previous_digit = None
        has_two_adjacent_digits = False
        incrementing = True
        
        for digit in num:
            print(previous_digit, digit)
            if previous_digit is None:
                previous_digit = digit
            else:
                if previous_digit == digit:
                    has_two_adjacent_digits = True
                if int(previous_digit) > int(digit):
                    incrementing = False
                    break
                previous_digit = digit
                    
            if has_two_adjacent_digits and incrementing:
                password_count += 1
                print(num)
                import pdb;pdb.set_trace()
    print(password_count)
           


# Two adjacent digits are the same (like 22 in 122345).
# Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
# Other than the range rule, the following are true:

# 111111 meets these criteria (double 11, never decreases).
# 223450 does not meet these criteria (decreasing pair of digits 50).
# 123789 does not meet these criteria (no double).
