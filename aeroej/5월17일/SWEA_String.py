for _ in range(1, 11):
    test_case = int(input())
    word = input()
    sentence = input()

    n = len(word)
    idx = -n
    cnt = 0

    while True:
        try:
            idx = idx + n + sentence[idx+n:].index(word)
            cnt += 1
        except ValueError:
            break

    print('#{} {}'.format(test_case, cnt))
    
