def PrimeList(N):
    """
    返回一个字符串，包含所有小于 N 的质数（按升序），以单个空格分隔，末尾无空格。
    参数:
      - N: 整数
    返回:
      - 若 N <= 2 返回空字符串 ""
      - 否则返回形如 "2 3 5 7 ..." 的字符串
    实现说明:
      使用埃拉托斯特尼筛法，时间复杂度约为 O(N log log N)。
    """
    if not isinstance(N, int):
        raise TypeError("N must be an integer")
    if N <= 2:
        return ""
    sieve = [True] * N
    sieve[0] = sieve[1] = False
    limit = int(N ** 0.5) + 1
    for i in range(2, limit):
        if sieve[i]:
            step = i
            start = i * i
            sieve[start:N:step] = [False] * ((N - 1 - start) // step + 1)
    primes = [str(i) for i, is_p in enumerate(sieve) if is_p]
    return " ".join(primes)


if __name__ == "__main__":
    # 简单演示
    print(PrimeList(30))  # 输出: 2 3 5 7 11 13 17 19 23 29
