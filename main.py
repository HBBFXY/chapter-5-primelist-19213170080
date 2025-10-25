def PrimeList(N):
    prime_list = []
    # 遍历 2 到 N-1 的所有数（因为要找“小于 N”的质数）
    for num in range(2, N):
        is_prime = True  # 先假设当前数是质数
        # 只需检查到 num 的平方根（优化效率）
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:  # 能被整除，说明不是质数
                is_prime = False
                break
        if is_prime:  # 如果是质数，加入列表
            prime_list.append(str(num))
    # 用空格连接所有质数字符串，得到最终结果
    return " ".join(prime_list)


    
