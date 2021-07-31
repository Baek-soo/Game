import random

#뽑을 숫자 갯수
how_many_number = 3

#무작위 수를 3개 뽑기
def random_numbers():
    numbers = []
    while len(numbers) < how_many_number:
        num = random.randint(0,9)
        if num not in numbers:
            numbers.append(num)
    print(f"0과 9사이의 서로 다른 숫자 {how_many_number}개를 뽑았습니다.")
    return numbers

#받을 숫자
def take_guess():
    print(f"숫자 {how_many_number}개를 하나씩 차례대로 입력해주세요")

    my_number = []
    while len(my_number) < how_many_number:
        new_number = int(input(f"{len(my_number)+1}번째 숫자를 입력하세요"))

        if new_number < 0 or new_number > 9:
            print("범위를 벗어난 숫자입니다. 다시 입력해주세요")
        elif new_number in my_number:
            print("중복된 숫자입니다. 다시 입력해주세요")
        else:
            my_number.append(new_number)
    return my_number

#strike ball count 
def get_score(guess, solution):
    strike_count = 0
    ball_count = 0

    for i in range(how_many_number):
        if guess[i] == solution[i]:
            strike_count += 1
        elif guess[i] in solution:
            ball_count += 1

    return strike_count, ball_count

#게임 시작
Answer = random_numbers()
tries = 0

while True:
    user_guess = take_guess()
    s, b = get_score(user_guess, Answer)

    print(f"{s}S {b}B\n")
    tries += 1

    if s == how_many_number:
        break
print(f"축하드립니다 {tries}번 만에 성공하셨습니다.")
