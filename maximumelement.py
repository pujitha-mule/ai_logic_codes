def maximumSwap(num):
    digits = list(str(num))
    n = len(digits)
    last = [0] * 10
    for i in range(n):
        last[int(digits[i])] = i

    for i in range(n):
        for d in range(9, int(digits[i]), -1):
            if last[d] > i:
                # Swap if we find a larger digit
                digits[i], digits[last[d]] = digits[last[d]], digits[i]
                return int(''.join(digits))
    return num  

num = 2736
print(maximumSwap(num))  # Output: 7236
