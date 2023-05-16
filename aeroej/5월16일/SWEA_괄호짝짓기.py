for test_case in range(1, 11):
    n = int(input())
    stack = []

    flag = False
    for word in list(map(str, input())):
        idx = '([{<)]}>'.index(word)

        # 열린 괄호
        if idx < 4:
            stack.append(idx)

        # 닫힌 괄호
        elif 4 <= idx < 8:
            # 열린 괄호가 없거나 짝이 안 맞는 경우
            if len(stack) == 0 or idx - stack.pop() != 4:
                flag = True
                break

    result = 1
    # 열린 괄호가 남아있는 경우
    if flag or len(stack) > 0:
        result = 0

    print('#{} {}'.format(test_case, result))

