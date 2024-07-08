# 초성, 중성, 종성의 갯수
CHO = 19
JUNG = 21
JONG = 28

# 한글 시작 유니코드 값
HANGUL_BASE = 0xAC00  # '가'의 유니코드 값

# 사용자로부터 번호 입력 받기
num = int(input())

# 입력받은 숫자에 해당하는 한글 글자 계산
unicode_value = HANGUL_BASE + num - 1  # 입력받은 숫자에서 1을 빼고 계산
hangul_char = chr(unicode_value)

# UTF-8로 인코딩하여 출력
print(hangul_char)