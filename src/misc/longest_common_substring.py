import functools

from common import colours


@functools.cache
def _longest_left_aligned_common_substring(a: str, b: str) -> str:
    cursor = 0
    while True:
        if cursor >= len(a): break
        if cursor >= len(b): break
        if a[cursor] != b[cursor]: break
        cursor += 1
    return a[:cursor]


@functools.cache
def _longest_common_substring(a: str, b: str) -> (str, int, int):
    best: str = ""
    best_a_start_index: int = 0
    best_b_start_index: int = 0

    if len(a) == 0 or len(b) == 0:
        return best, best_a_start_index, best_b_start_index

    def consider(common_substring: str, a_start_index: int, b_start_index: int) -> None:
        nonlocal best, best_a_start_index, best_b_start_index
        if len(common_substring) <= len(best):
            return
        best = common_substring
        best_a_start_index = a_start_index
        best_b_start_index = b_start_index

    consider(_longest_left_aligned_common_substring(a, b), 0, 0)

    case_one_best, case_one_best_a_start_index, case_one_best_b_start_index = _longest_common_substring(a[1:], b)
    case_one_best_a_start_index += 1
    consider(case_one_best, case_one_best_a_start_index, case_one_best_b_start_index)

    case_two_best, case_two_best_a_start_index, case_two_best_b_start_index = _longest_common_substring(a, b[1:])
    case_two_best_b_start_index += 1
    consider(case_two_best, case_two_best_a_start_index, case_two_best_b_start_index)

    return best, best_a_start_index, best_b_start_index


def longest_common_substring(a: str, b: str) -> (str, slice, slice):
    best, best_a_start_index, best_b_start_index = _longest_common_substring(a, b)
    best_a_index = slice(best_a_start_index, best_a_start_index + len(best))
    best_b_index = slice(best_b_start_index, best_b_start_index + len(best))
    return best, best_a_index, best_b_index


def pretty_print_longest_common_substring(a: str, b: str, result: (str, slice, slice)):
    substring, a_index, b_index = result

    left_pad_to_length: int = max(a_index.start, b_index.start)
    print(f"{a[:a_index.start]:>{left_pad_to_length}}{colours.pink}{a[a_index]}{colours.reset}{a[a_index.stop:]}")
    print(f"{b[:b_index.start]:>{left_pad_to_length}}{colours.pink}{b[b_index]}{colours.reset}{b[b_index.stop:]}")
    print(f"{colours.pink}{'':>{left_pad_to_length}}{'^' * len(substring)}{colours.reset}")


def main():
    my_email = "me@lordfirespeed.dev"
    my_password = "dethrone1earldom.colorings@HARPOON0insider"  # not a password I actually use for anything :)

    result = longest_common_substring(my_email, my_password)
    substring, a_index, b_index = result
    assert substring == my_email[a_index]
    assert substring == my_password[b_index]

    pretty_print_longest_common_substring(my_email, my_password, result)


if __name__ == "__main__":
    main()
