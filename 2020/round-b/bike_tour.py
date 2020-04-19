def solve_for_peaks(N, S):
    i = 1
    peak_count = 0
    while i < len(S):
        if i < len(S) - 1 and S[i] > S[i+1] and S[i] > S[i-1]:
            peak_count += 1
        i += 1

    return peak_count


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        N = int(input())
        S = [int(i) for i in input().split()]
        ans = solve_for_peaks(N, S)
        print("Case #{}: {}".format(str(i+1), ans))
