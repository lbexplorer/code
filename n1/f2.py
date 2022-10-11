def judge(a, b, c, highprecision=True):  # 首先进行判断，确保参数为数字
    # 由于计算机表示实数时存在精度的问题，所以不能使用==来判断实数是否为0
    # 函数的最后一个参数highmiddle为True表示进行高精度的计算，False表示低精度的计算
    if not isinstance(a, (int, float, complex)) or abs(a) < 1e-6:
        print('error')
        return
    if not isinstance(b, (int, float, complex)):
        print('error')
        return
    if not isinstance(c, (int, float, complex)):
        print('error')
        return

    # delta<0时无解
    d = b ** 2 - 4 * a * c
    # 根据一元二次方程求根公式进行计算
    # 当d<0时，在实数域内无解，d**0.5会得到复数
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)

    if isinstance(x1, complex):
        if highprecision:
            # 高精确度考虑虚数
            x1 = round(x1.real, 3) + round(x1.imag, 3) * 1j
            x2 = round(x2.real, 3) + round(x2.imag, 3) * 1j
            return (x1, x2)
        else:
            # 精确度较低只考虑实数根
            print('no answer')
            return
    # 如果是实数根，保留3位小数
    return (round(x1, 3), round(x2, 3))


def main():
    temp = judge(2433, 10000, 80000, True)
    if isinstance(temp, tuple):
        print('x1={0[0]}\nx2={0[1]}'.format(temp))


if __name__ == '__main__':
    main()
