from functools import cache


def count_palindromic_substring(value: str) -> int:
    count, is_palindrome = _count_palindromic_substring(value)
    return count


@cache
def _count_palindromic_substring(value: str) -> tuple[int, bool]:
    if (len(value)) == 0:
        return 0, True
    if (len(value)) == 1:
        return 1, True
    if (len(value)) == 2:
        if value[0] == value[1]:
            return 3, True
        return 2, False

    left, _ = _count_palindromic_substring(value[:-1])
    middle, middle_is_palindrome = _count_palindromic_substring(value[1:-1])
    right, _ = _count_palindromic_substring(value[1:])
    is_palindrome = middle_is_palindrome and value[0] == value[-1]
    count = left + right - middle + is_palindrome
    return count, is_palindrome


if __name__ == "__main__":
    print(count_palindromic_substring("abccba"))
