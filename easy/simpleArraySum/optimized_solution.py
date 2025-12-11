def simpleArraySum(numbers: list[int]) -> int:
    return sum(numbers)


if __name__ == "__main__":

    numbers = list(map(int, input().strip().split()))
    total = simpleArraySum(numbers)
    print(total)