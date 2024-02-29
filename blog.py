import hashlib

MAX_SIGNUP_TIME = 10
MAX_LOGIN_TIME = 5
MAX_SEARCH_TIME = 5
MAX_POST_TIME = 50


class Member():
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
    
    def display(self):
        # 회원명, ID를 출력할 때 첫 글자 제외 *로 표시하여 정보를 보호한다.
        show_name = self.name[0] + len(self.name[1:]) * '*'
        show_username = self.username[0] + len(self.username[1:]) * '*'
        print(f" 회원명: {show_name}, ID: {show_username}")
        

class Post(Member):
    def __init__(self, title, content, name, username, password):
        self.title = title
        self.content = content
        super().__init__(name, username, password)
        self.author = self.username


# 회원가입 함수
def sign_up():
    print("\n'1. 회원가입'을 선택하셨습니다.\n")
    
    # 회원가입 시도 횟수
    try_num = 0
    
    # 회원가입 시작
    while (try_num < MAX_SIGNUP_TIME):
        print("[회원가입]\n회원 정보를 입력합니다...\n")
        
        # h: sha256 해싱 객체
        # 반복할 때마다 initialize 한다. (중복된 해싱을 피하기 위함)
        h = hashlib.sha256()
        
        # 회원가입에 필요한 정보 입력
        add_name = input("이름을 입력하십시오.: ")
        add_username = input("ID를 입력하십시오.: ")
        add_password = input("PW를 입력하십시오.: ")
        
        # 회원가입 진행 여부 확인
        # True: 회원가입 진행 / False: 회원가입 취소
        if input(f"\n입력하신 정보는 아래와 같습니다.\n이름: {add_name}\nID: {add_username}\nPW: {add_password}\n\n맞다면 'y'를 입력하십시오.\n취소하고 싶다면 그 외의 입력을 해주십시오.\n입력: ").lower() == 'y':
            print("\n회원가입을 진행합니다...")
            # 해싱
            h.update(add_password.encode("utf-8"))
            # 회원 정보 추가
            members.append(Member(add_name, add_username, h.hexdigest()))
            print("완료\n")
        else:
            print("\n작성하신 정보로 가입 진행을 취소하셨습니다.\n")
        
        # 회원가입 시도 횟수 +1
        try_num += 1
        
        # 회원가입 중지 여부 결정
        if input("회원가입을 그만하고 싶으면 'y'를 입력하십시오.\n계속하고 싶다면 그 외의 입력을 해주십시오.\n입력: ").lower() == 'y':
            print("\n회원가입을 종료합니다. 메인 화면으로 이동합니다.\n")
            break
    
    print(".........................................")


# 로그인 함수
def log_in():
    print("\n'2. 로그인'을 선택하셨습니다.\n")
    global login_info
    
    # 이미 로그인을 한 경우 계정을 변경할지 변경하지 않고 로그인을 종료할지 선택
    if login_info:
        if input("이미 로그인한 상태입니다. 다른 계정으로 로그인 하시겠습니까?\n맞다면 'y'를 입력하십시오. 기존의 계정은 로그아웃합니다.\n아니라면 그 외의 입력을 해주십시오. 메인 화면으로 이동합니다.\n\n입력: ").lower() == 'y':
            print("\n기존 계정은 로그아웃하고 다른 계정으로 로그인을 시도합니다.\n")
            login_info = list()
        else:
            print("\n기존 계정으로 진행합니다. 메인 화면으로 이동합니다.\n")
            print(".........................................")
    
    # 로그인 시도 횟수
    try_num = 0
    
    # 로그인 시작
    while (try_num < MAX_LOGIN_TIME):
        print("[로그인]\n가입한 회원 정보로 로그인을 시도합니다...\n")
        
        # 로그인에 필요한 정보 입력
        check_username = input("ID를 입력하십시오.: ")
        check_password = input("PW를 입력하십시오.: ")
        
        # h: sha256 해싱 객체
        # 반복할 때마다 initialize 한다. (중복된 해싱을 피하기 위함)
        h = hashlib.sha256()
        # 해싱
        h.update(check_password.encode("utf-8"))
        
        # 로그인 진행
        for member in members:
            if check_username == member.username and h.hexdigest() == member.password:
                login_info = [member.name, member.username, member.password]
                print("\n로그인 하였습니다. 글 작성을 하실 수 있습니다.\n")
                break
        
        # 로그인 성공
        if login_info:
            break
        # 로그인 실패
        else:
            print("\n닉네임이 존재하지 않거나 잘못된 비밀번호입니다. 다시 시도하십시오.\n")
            
            # 로그인 중지 여부 결정
            if input("로그인을 그만하고 싶으면 'y'를 입력하십시오.\n계속하고 싶다면 그 외의 입력을 해주십시오.\n입력: ").lower() == 'y':
                print("로그인을 종료합니다.\n")
                break
        
        # 로그인 시도 횟수 +1
        try_num += 1

    print(".........................................")


# 글 작성 함수
def post():
    print("\n'3. 글 작성'을 선택하셨습니다.\n")
    global login_info
    
    # 로그인을 하지 않은 경우 경고 메시지를 출력하고 글 쓰기 종료
    if not login_info:
        print("로그인 하지 않아 글 작성을 할 수 없습니다. 먼저 로그인 해주십시오.\n메인 화면으로 이동합니다.\n")
        print(".........................................")
        return
    
    # 글 작성 시도 횟수
    try_num = 0
    
    # 글 작성 시작
    while (try_num < MAX_POST_TIME):
        print("[글 쓰기]\n글을 작성합니다...\n")
        
        # 글 작성에 필요한 정보 입력
        title = input("작성하실 글 제목을 입력하십시오: ")
        content = input("작성하실 글 내용을 입력하십시오: ")
        
        # 글 작성 진행 여부 확인
        # True: 글 작성 진행 / False: 글 작성 취소
        if input(f"\n입력하신 정보는 아래와 같습니다.\n제목: {title}\n내용: {content}\n\n맞다면 'y'를 입력하십시오.\n취소하고 싶다면 그 외의 입력을 해주십시오.\n입력: ").lower() == 'y':
            print("\n작성하신 글을 등록합니다...")
            # login_info[0]: member.name
            # login_info[1]: member.username
            # login_info[2]: member.password
            posts.append(Post(title, content, login_info[0], login_info[1], login_info[2]))
            print("완료\n")
        else:
            print("\n글 작성을 취소하셨습니다.\n")
        
        # 글 작성 시도 횟수 +1
        try_num += 1
        
        # 글 작성 중지 여부 결정
        if input("글 작성을 그만하고 싶으면 'y'를 입력하십시오.\n계속하고 싶다면 그 외의 입력을 해주십시오.\n입력: ").lower() == 'y':
            print("\n글 작성을 종료합니다. 메인 화면으로 이동합니다.\n")
            break
    
    print(".........................................")


# 글 검색 함수
def search():
    print("\n'4. 글 검색'을 선택하셨습니다.\n")
    
    # 글 검색 시도 횟수
    try_num = 0
    
    # 검색 시작
    while (try_num < MAX_SEARCH_TIME):
        print("[글 검색]\n특정 조건에 맞는 글을 검색합니다....\n")
        
        # 검색 결과 갯수
        results = 0
        
        # 검색 옵션 선택
        search_opt = input("검색 옵션을 선택하십시오.\n\n1. 내용에 해당 단어가 포함\n2. 제목에 해당 단어가 포함\n3. 내용 또는 제목에 해당 단어가 포함\n4. 해당 닉네임으로 작성함\n\n입력: ").lower()
        if search_opt not in ['1', '2', '3', '4']:
            print("\n유효하지 않은 검색 옵션입니다. 다시 시도하십시오.\n")
            continue
        
        # 검색 키워드 입력
        search_word = input("검색할 키워드를 입력하십시오.: ")
        
        # 옵션, 키워드에 맞는 검색 진행
        for post in posts:
            # 1. 내용에 해당 단어가 포함
            if search_opt == '1':
                if search_word in post.content:
                    print(f"\n'{search_word}' 키워드가 내용에 포함된 글 제목은 '{post.title}' 입니다.")
                    results += 1
            # 2. 제목에 해당 단어가 포함
            elif search_opt == '2':
                if search_word in post.title:
                    print(f"\n'{search_word}' 키워드가 제목에 포함된 글 제목은 '{post.title}' 입니다.")
                    results += 1
            # 3. 내용 또는 제목에 해당 단어가 포함
            elif search_opt == '3':
                if (search_word in post.content) or (search_word in post.title):
                    print(f"\n'{search_word}' 키워드가 내용 또는 제목에 포함된 글 제목은 '{post.title}' 입니다.")
                    results += 1
            # 4. 해당 닉네임으로 작성함
            elif search_opt == '4':
                if search_word == post.author:
                    print(f"\n{search_word} 님이 작성하신 글 제목은 '{post.title}' 입니다.")
                    results += 1
        
        # 검색 결과 갯수 출력
        if not results:
            print("\n검색 조건에 맞는 글이 존재하지 않습니다.\n")
        else:
            print(f"\n검색 결과 총 {results}개의 글을 찾았습니다.\n")
        
        # 검색 시도 횟수 +1
        try_num += 1
        
        # 검색 중지 여부 결정
        if input("검색을 그만하고 싶으면 'y'를 입력하십시오.\n계속하고 싶다면 그 외의 입력을 해주십시오.\n입력: ").lower() == 'y':
            print("검색을 종료합니다.\n")
            break
    
    print(".........................................")


# 전체 회원 조회 함수
def show_members():
    print("\n'5. 전체 회원 조회'를 선택하셨습니다.\n")
    
    # 전체 회원 조회 시작
    print("┌───────────[현재 모든 회원 목록]───────────┐")
    
    # 회원이 존재하지 않으면 대체 텍스트 출력
    # 회원이 존재할 경우 전체 회원 출력
    if not members:
        print("\t  회원이 존재하지 않습니다.")
    else:
        for member in members:
            member.display()
    print("└───────────────────────────────────────────┘\n")


# 메인 함수
def main():
    print("┌───────────Spartans' Blog───────────┐")
    print("│ 글을 작성하고 회원들과 공유하세요. │")
    print("└────────────────────────────────────┘\n")
    
    while True:
        main_command = input("원하는 작업을 선택하세요.\n\n1. 회원가입\n2. 로그인\n3. 글 작성\n4. 글 검색\n5. 전체 회원 조회\n\n종료를 원하면 x나 q를 입력하십시오.\n\n입력: ").lower()
        if main_command == '1':
            # 회원가입
            sign_up()
        elif main_command == '2':
            # 로그인
            log_in()
        elif main_command == '3':
            # 글 작성
            post()
        elif main_command == '4':
            # 글 검색
            search()
        elif main_command == '5':
            # 전체 회원 조회
            show_members()
        elif main_command == 'x' or main_command == 'q':
            print("\n프로그램을 종료합니다.")
            break
        else:
            print("\n유효하지 않은 입력입니다. 다시 시도하십시오.\n")
            continue


if __name__ == "__main__":
    # posts: Post 인스턴스들의 리스트
    # members: Member 인스턴스들의 리스트
    # login_info: 로그인 계정의 정보 (구성: [member.name, member.username, member.password])
    posts = list()
    members = list()
    login_info = list()
    main()
