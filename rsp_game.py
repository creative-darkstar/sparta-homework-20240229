import random

RSP_DATA = {
    "Korean": ["가위", "바위", "보"],
    "English": ["scissors", "rock", "paper"]
    }
INPUT_TEXT = f"[{', '.join(RSP_DATA['Korean'])}] 또는 [{', '.join(RSP_DATA['English'])}] 중 하나를 선택하여 입력하십시오.: "


def play_game():
    com_idx = random.randrange(3)
    user_input = input(INPUT_TEXT).lower()
    
    if user_input in RSP_DATA["Korean"]:
        temp_list = RSP_DATA["Korean"]
    elif user_input in RSP_DATA["English"]:
        temp_list = RSP_DATA["English"]
    else:
        print("유효하지 않은 입력입니다. 다시 시도해주십시오.")
        return
    
    # [일반적인 코드]
    # print(f"사용자: {user_input}, 컴퓨터: {temp_list[com_idx]}")
    # if user_input == "가위":
    #     if temp_list[com_idx] == "가위":
    #         print("무승부입니다.")
    #         status[0] += 1
    #     elif temp_list[com_idx] == "바위":
    #         print("패배했습니다.")
    #         status[2] += 1
    #     else:
    #         print("승리했습니다.")
    #         status[1] += 1
    # elif user_input == "바위":
    #     if temp_list[com_idx] == "가위":
    #         print("승리했습니다.")
    #         status[1] += 1
    #     elif temp_list[com_idx] == "바위":
    #         print("무승부입니다.")
    #         status[0] += 1
    #     else:
    #         print("패배했습니다.")
    #         status[2] += 1
    # else:
    #     if temp_list[com_idx] == "가위":
    #         print("패배했습니다.")
    #         status[2] += 1
    #     elif temp_list[com_idx] == "바위":
    #         print("승리했습니다.")
    #         status[1] += 1
    #     else:
    #         print("무승부입니다.")
    #         status[0] += 1
    user_idx = temp_list.index(user_input)
    print(f"사용자: {temp_list[user_idx]}, 컴퓨터: {temp_list[com_idx]}")
    result = (user_idx - com_idx) % 3
    if result == 0:
        print("무승부입니다.")
    elif result == 1:
        print("승리했습니다.")
    else:
        print("패배했습니다.")
    status[result] += 1


def set_game():
    global status
    
    while True:
        play_game()
        
        command = input("게임을 다시 하시겠습니까? (종료: 'n', 데이터 초기화 후 재시작 'r')\n계속하고 싶다면 그 외의 입력을 해주십시오.\n입력: ").lower()
        if command == 'n':
            print("게임을 종료합니다.")
            print(f"전적: {status[1]}승 {status[2]}패 {status[0]}무")
            break
        elif command == 'r':
            print("이전 게임 플레이어의 전적을 초기화 합니다...")
            status = [0, 0, 0]
    

if __name__ == "__main__":
    # [무, 승, 패]
    status = [0, 0, 0]
    set_game()
