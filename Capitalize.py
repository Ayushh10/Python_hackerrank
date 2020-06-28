def solve(s):
    first_half, second_half = s.split(" ")
    first_letter, second_letter = first_half[0], second_half[0]
    first_rem, second_rem = first_half[1:], second_half[1:]
    return first_letter.capitalize()+first_rem+" "+second_letter.capitalize()+second_rem
