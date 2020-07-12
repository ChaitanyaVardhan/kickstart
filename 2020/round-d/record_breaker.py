def solve(N, S):
    days = []
    i = 0
    while i < len(S):
        if cond_1(i, S) and cond_2(i, S):
            days.append(i)
        i += 1

    return len(days)


def cond_1(i, S):
    j = 0
    while j < i:
        if S[j] < S[i]:
            j += 1
        else:
            break
    if j == i:
        return True
    else:
        return False

    
def cond_2(i, S):
    if i == len(S) - 1:
        return True
    elif S[i] > S[i+1]:
        return True
    else:
        return False


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        N = int(input())
        S = [int(s) for s in input().split()]
        x = solve(N, S)
        print(f"Case #{i}: {x}")
