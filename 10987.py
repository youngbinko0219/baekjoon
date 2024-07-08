word = input()
vowels = 'aeiou'
vowel_count = 0

# 입력받은 단어에서 각 문자를 순회하면서 모음인지 확인
for letter in word:
    if letter.lower() in vowels:  # 대소문자 구분을 없애기 위해 소문자로 변환 후 확인
        vowel_count += 1

print(vowel_count)