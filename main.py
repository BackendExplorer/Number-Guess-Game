import random
import sys

def main():
    sys.stdout.buffer.write(b'Guess-the-number-game Start!\n')
    
    # 最小値(n) と最大値(m) を入力する（再入力ループ付き）
    while True:
        sys.stdout.buffer.write(b'Please enter a minimum value (n) : ')
        sys.stdout.flush()
        n = int(sys.stdin.buffer.readline())
        sys.stdout.buffer.write(b'Please enter a maximum value (m) : ')
        sys.stdout.flush()
        m = int(sys.stdin.buffer.readline())

        if n <= m:
            break
        # n > m の場合は再入力を促す
        sys.stdout.buffer.write(b'The minimum value should be less than or equal to the maximum value.\n')

    # 難易度を選択する
    sys.stdout.buffer.write(
        b'Choose a difficulty level between 0 and 2\n'
        b'easy  (Input : 0)\n'
        b'medium(Input : 1)\n'
        b'hard  (Input : 2)\n'
        b'Input : '
    )
    sys.stdout.buffer.write = sys.stdout.buffer.write  # flush呼び出しのために残しています
    sys.stdout.buffer.flush()
    select_mode = int(sys.stdin.buffer.readline())

    if select_mode == 0:
        number_of_attempts = 15
    elif select_mode == 1:
        number_of_attempts = 10
    elif select_mode == 2:
        number_of_attempts = 5
    else:
        return sys.stdout.buffer.write(b'Could not set difficulty...\nExiting game')

    random_num = random.randint(n, m)

    # 推測ループ
    for i in range(number_of_attempts):
        s1 = f'Time : {i+1}/{number_of_attempts}\n'
        sys.stdout.buffer.write(s1.encode('utf-8'))
        
        s2 = f'Enter a number between {n} and {m} : '
        sys.stdout.buffer.write(s2.encode('utf-8'))
        sys.stdout.buffer.flush()
        answer_num = int(sys.stdin.buffer.readline())
        
        if random_num == answer_num:
            # 試行回数を表示して終了
            msg = f"That's correct! You guessed it in {i+1} attempts.\nEnd the game\n"
            return sys.stdout.buffer.write(msg.encode('utf-8'))
        
        sys.stdout.buffer.write(b"That's Incorrect\n")
    
    # 試行回数を使い切った場合
    s3 = f'Game over\nThe correct answer was {random_num}\n'
    return sys.stdout.buffer.write(s3.encode('utf-8'))


if __name__ == '__main__':
    main()
