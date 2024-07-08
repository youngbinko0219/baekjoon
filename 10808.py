# 사용자로부터 단어 입력 받기
word = input()

# 각 알파벳의 개수를 저장할 딕셔너리 초기화
letter_count = {}

# 알파벳 'a'부터 'z'까지를 키로 하는 딕셔너리 초기화
for letter in 'abcdefghijklmnopqrstuvwxyz':
    letter_count[letter] = 0

# 입력받은 단어에서 각 알파벳의 개수 세기
for letter in word:
    if letter in letter_count:
        letter_count[letter] += 1

# 결과를 한 줄로 출력하기 위한 변수 초기화
output = ""

# 각 알파벳의 개수를 공백을 이용하여 한 줄로 이어붙이기
for letter in 'abcdefghijklmnopqrstuvwxyz':
    output += str(letter_count[letter]) + " "

# 마지막 공백 제거 후 결과 출력
print(output.rstrip())