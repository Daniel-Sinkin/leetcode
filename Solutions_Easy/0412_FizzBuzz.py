"""
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.


Example 1:

Input: n = 3
Output: ["1","2","Fizz"]
Example 2:

Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
Example 3:

Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
"""

n_to_str_map: dict[int, str] = {3: "Fizz", 5: "Buzz"}


# Alternative if we want to expand to multiple
def _fizzBuzz_generic(n: int) -> str:
    does_divide_map: dict[int, bool] = {i: (n % i) == 0 for i in n_to_str_map}

    s = ""
    for i, does_divide in does_divide_map.items():
        if does_divide:
            s += n_to_str_map[i]

    # No hits
    if s == "":
        return str(n)
    else:
        return s


def _fizzBuzz(i: int) -> str:
    div3 = (i % 3) == 0
    div5 = (i % 5) == 0

    if not div3 and not div5:
        return str(i)
    elif div3 and not div5:
        return "Fizz"
    elif not div3 and div5:
        return "Buzz"
    else:
        return "FizzBuzz"


def fizzBuzz(n: int) -> list[str]:
    return list(map(_fizzBuzz, range(1, n + 1)))


if __name__ == "__main__":
    print(fizzBuzz(20))
