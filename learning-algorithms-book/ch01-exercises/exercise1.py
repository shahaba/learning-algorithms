""" is Palindrome Exercise

Compare performance of two is_palindrome methods agaisnt our own custom algorithm
"""


# Test Algorithm 1
def is_palindrome1(w):
    """Create slice with negative step and confirm equality with w."""
    return w[::-1] == w


# Test Algorithm 2
def is_palindrome2(w):
    """Strip outermost characters if same, return false when mismatch."""
    while len(w) > 1:
        if w[0] != w[-1]:  # if mismatch, return False
            return False
        w = w[1:-1]  # strip characters on either end; repeat

    return True  # must have been palindrome


# My ALgorithm
def is_palindrome(word):
    """Check if Palindrome

    Space Complexity - O(1)
    Time Complexity - O(N)
    """
    # clean string of spaces, punctuation, and mixed capitilization
    word = helper_clearn_word(word)
    left, right = 0, len(word) - 1

    while left <= right:  # iterate from both sides of Word
        if word[left] != word[right]:
            return False

        right -= 1
        left += 1

    return True


def helper_clearn_word(word):
    punc = "!()[]{};:,.<>?@#$%^&*~-_"

    for char in word:
        if char in punc:
            word = word.replace(char, "")

    word = word.lower()
    word = word.replace(" ", "")

    return word


if __name__ == "__main__":
    print(
        is_palindrome1("madam"),
        is_palindrome2("madam"),
        is_palindrome("madam"),
        is_palindrome("mad"),
        is_palindrome("racecar"),
        is_palindrome("A man, a plan, a canal. Panama!"),
    )
