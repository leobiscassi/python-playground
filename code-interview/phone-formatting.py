def solution(S):
    number = "".join([c for c in S if c.isdigit()])
    x = 0
    phone_number = ""

    for i in range(3, len(number), 3):
        phone_number += f"-{number[x:i]}" if len(phone_number) > 0 else number[x:i]
        x = i
        if (len(number) - (i+3) < 2) and (len(number) - (i+3) != 0):
            for z in range(i, len(number), 2):
                phone_number += f"-{number[z:z+2]}"
            break
    else:
        phone_number += f"-{number[x:]}"

    return phone_number

if __name__ == '__main__':
    print(solution("00-44  48 5555 8361"))
    print(solution("0 - 22 1985--324"))
    print(solution("555372654"))
    print(solution("5556780989"))
    print(solution("5556780*****&&&989"))