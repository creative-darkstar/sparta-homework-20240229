import random

RSP_DATA = {
    "Korean": ["가위", "바위", "보"],
    "English": ["scissors", "rock", "paper"]
    }


def play_game_web(user_input):
    com_idx = random.randrange(3)
    
    if user_input in RSP_DATA["Korean"]:
        temp_list = RSP_DATA["Korean"]
    elif user_input in RSP_DATA["English"]:
        temp_list = RSP_DATA["English"]
    else:
        print("유효하지 않은 입력입니다. 다시 시도해주십시오.")
        return None
    
    user_idx = temp_list.index(user_input)
    
    # result
    # 0: 무승부, 1: 승리, 2: 패배
    result = (user_idx - com_idx) % 3
    if result == 0:
        result_text = "무승부"
    elif result == 1:
        result_text = "승리"
    else:
        result_text = "패배"
    
    return {"Computer": temp_list[com_idx], "User": user_input, "Result": result_text}
