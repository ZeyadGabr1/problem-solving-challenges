def simpleArraySum(numbers: list[int]) -> int:
    total = 0
    for n in numbers:
        total += n

    return total


if __name__ == "__main__":
    numbers = list(map(int, input().strip().split()))
    total = simpleArraySum(numbers)
    print(total)