import string

def solution(S):
    LETTERS = string.ascii_lowercase + string.ascii_uppercase
    max_ = -1
    for word in S.split(" "):
        if check_word(word, LETTERS):
            max_ = max(max_, len(word))
    return max_

def check_word(word, LETTERS):
    letter_count = 0
    digit_count = 0
    for char in word:
        if char in LETTERS:
            letter_count += 1
        elif char in string.digits:
            digit_count += 1
        else:
            return False
    if letter_count % 2 == 1 or digit_count % 2 == 0:
        return False
    return True
