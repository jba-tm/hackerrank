def minion_game(word):
    gamers = {
        'kevin': 0,
        'stuart': 0
    }
    vowels = 'AIEOU'

    for itr, char in enumerate(word):
        print(len(word) - itr)
        gamers['kevin' if char in "AIEOU" else 'stuart'] += len(word) - itr
    if gamers['kevin']>gamers['stuart']:
        print('Kevin', gamers['kevin'])
    elif gamers['kevin']<gamers['stuart']:
        print('Stuart', gamers['stuart'])
    else:
        print('Draw')

if __name__ == '__main__':
    s = 'banana'
    minion_game(s.upper())
