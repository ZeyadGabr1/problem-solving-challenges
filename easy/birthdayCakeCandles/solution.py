def birthdayCakeCandles(candles):
    tallest_candle = max(candles)  
    count_tallest_candles = candles.count(tallest_candle)
    return count_tallest_candles

if __name__ == "__main__":
    candles = list(map(int, input().split()))

    print(birthdayCakeCandles(candles))