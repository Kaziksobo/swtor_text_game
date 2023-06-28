def read_game_text(filename):
    with open(f'texts\{filename}', 'r') as f:
        game_text = f.read()
    return game_text.split('*****')

game_text_list = read_game_text('setup_texts.txt')
print(game_text_list[0])

test = input(game_text_list[0])