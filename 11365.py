# 사용자가 입력한 문장을 받아옵니다.
lines = []
while True:
    line = input()
    if line == "END":
        break
    lines.append(line)

# 영어로 번역된 문장들을 담을 리스트 초기화
translated_lines = []

# 각 줄을 올바른 영어 문장으로 번역
for line in lines:
    # 거꾸로 된 문자열을 다시 뒤집어서 원래대로 되돌림
    reversed_line = line[::-1]
    
    # 영어로 번역된 문장 추가
    translated_lines.append(reversed_line)

# 번역된 문장들을 출력
for translated_line in translated_lines:
    print(translated_line)