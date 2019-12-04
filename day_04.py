from collections import Counter

if __name__ == '__main__':
    # Generate a list of all possible passwords
    num_list = [str(i) for i in range(347312, 805915+1)]
    password_list = []

    # Part 1:
    for num in num_list:
        previous_digit = None
        has_two_adjacent_digits = False
        incrementing = True

        for digit in num:
            if previous_digit is None:
                previous_digit = digit
            else:
                # Check two adjacent digits
                if previous_digit == digit:
                    has_two_adjacent_digits = True

                # Digits never decrease
                if int(previous_digit) > int(digit):
                    incrementing = False
                    break

                previous_digit = digit

        if has_two_adjacent_digits and incrementing:
            password_list.append(num)

    print("Number of different passwords:", len(password_list))

    # Part 2:
    filtered_password_list = []
    for num in password_list:
        counter = Counter(num)
        if 2 in counter.values():
            filtered_password_list.append(num)

    print("Number of different passwords:", len(filtered_password_list))
