# Find the Runner-up Score
if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    winner = max(arr)
    try:
        while True: 
            arr.remove(winner)
    except ValueError:
        pass
    print(max(arr))
