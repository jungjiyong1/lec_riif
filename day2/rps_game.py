import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(player, computer):
    if player == computer:
        return 'tie'

    wins = {
        ('rock', 'scissors'): 'player',
        ('scissors', 'paper'): 'player',
        ('paper', 'rock'): 'player'
    }

    return wins.get((player, computer), 'computer')

def play_round(player_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(player_choice, computer_choice)

    return {
        'player': player_choice,
        'computer': computer_choice,
        'result': result
    }

def get_player_choice():
    choice_map = {
        '가위': 'scissors',
        '바위': 'rock',
        '보': 'paper',
        'rock': 'rock',
        'paper': 'paper',
        'scissors': 'scissors'
    }

    while True:
        player_input = input("당신의 선택 (가위/바위/보): ").strip()
        if player_input in choice_map:
            return choice_map[player_input]
        print("❌ 다시 입력해주세요 (가위/바위/보)")

def display_round(round_data):
    choice_names = {'rock': '바위', 'paper': '보', 'scissors': '가위'}
    print(f"\n당신: {choice_names[round_data['player']]} vs 컴퓨터: {choice_names[round_data['computer']]}")
    if round_data['result'] == 'player':
        print("✓ 이겼습니다!")
    elif round_data['result'] == 'computer':
        print("✗ 졌습니다.")
    else:
        print("= 비겼습니다.")

def play_game():
    results = []
    for round_num in range(1, 6):
        print(f"\n【 {round_num}판 】")
        player_choice = get_player_choice()
        round_result = play_round(player_choice)
        display_round(round_result)
        results.append(round_result['result'])

    return results

def display_final_stats(results):
    win_count = results.count('player')
    loss_count = results.count('computer')
    tie_count = results.count('tie')

    print("\n" + "="*30)
    print("【 최종 결과 】")
    print(f"승: {win_count}  무: {tie_count}  패: {loss_count}")
    print("="*30)

def main():
    while True:
        print("\n=== 가위바위보 게임 ===")
        results = play_game()
        display_final_stats(results)

        play_again = input("\n한 번 더 하시겠습니까? (Y/n): ").strip().lower()
        if play_again in ['n', 'no']:
            print("\n게임을 종료합니다.")
            break

if __name__ == '__main__':
    main()
