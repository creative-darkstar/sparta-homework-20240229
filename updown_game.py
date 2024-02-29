import random

MAX_AVAILABLE_TRY = 100


def is_minus(input_value):
    if input_value[0] == '-':
        return input_value[1:].isdigit()
    else:
        return False


def is_valid(input_value):
    if input_value.isdigit() or is_minus(input_value):
        input_num = int(input_value)
        if (input_num >= 1 and input_num <= 100):
            return True
        else:
            print("유효한 범위 내의 숫자를 입력하십시오. (1~100 사이 자연수)")
            return False
    else:
        print("유효하지 않은 입력입니다. 다시 시도해주십시오.")
        return False


def play_game():
    answer  = random.randint(1, 100)
    try_num = 1
    
    while (try_num <= MAX_AVAILABLE_TRY):
        input_value = input("숫자를 입력하십시오. (1~100 사이 자연수): ")
        if is_valid(input_value) is True:
            input_num = int(input_value)
            if answer == input_num:
                print(f"정답입니다. 시도한 횟수: {try_num}")
                break
            else:
                print(f"{'업' if answer > input_num else '다운'}")
        try_num += 1
    
    if try_num > MAX_AVAILABLE_TRY:
        print(f"숫자를 맞추지 못하셨습니다. 제한 횟수({MAX_AVAILABLE_TRY})에 도달하여 게임을 종료합니다.")
        try_num = 0
    
    return try_num


def set_game():
    global max_try
    
    while True:
        prev_try = play_game()
        max_try = prev_try if prev_try > max_try else max_try
        
        command = input("게임을 다시 하시겠습니까? (종료: 'n', 데이터 초기화 후 재시작 'r')\n계속하고 싶다면 그 외의 입력을 해주십시오.\n입력: ").lower()
        if command == 'n':
            print("게임을 종료합니다.")
            break
        elif command == 'r':
            print("이전 게임 플레이어의 기록을 초기화 합니다...")
            max_try = 0
        print(f"이전 게임 플레이어의 최고 시도 횟수: {max_try}")


if __name__ == "__main__":
    max_try = 0
    set_game()
