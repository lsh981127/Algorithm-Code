input = int(input())
# input : N키로그램

def suger(input):
    fiveMax = input // 5   # 5로 나눴을때 최대 몫
    if input % 5 == 0:
        return fiveMax
    
    val = fiveMax
    if fiveMax == 0:
        if input % 3 == 0:
            temp = input // 3
            return temp
        
    while True:
        rest = input - 5 * val      # 5 배수로 뺀 값
        if rest % 3 == 0:
            return val + (rest // 3)              
        val -= 1
        if val < 0:
            break


    return -1


print(f"{suger(input)}")


