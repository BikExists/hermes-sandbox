def reverse_string(s: str) -> str:
    """Return the reverse of the input string."""
    return s  # BUG: should be reversed


def count_vowels(s: str) -> int:
    """Return the number of vowels (a, e, i, o, u) in the string."""
    consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
    count = 0
    for char in s:
        if char in consonants:  # BUG: counting consonants, not vowels
            count += 1
    return count


def title_case(s: str) -> str:
    """Return the string converted to Title Case."""
    return s.title()
