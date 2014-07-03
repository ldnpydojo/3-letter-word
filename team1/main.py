
import random


class Game(object):
    def __init__(self, word):
        self.word = word.lower()

    def check(self, guess):
        if len(guess) != len(self.word):
            return (0, 0)
        guess = guess.lower()
        wrong = ""
        unused = ""
        right = 0
        for index, char in enumerate(guess):
            if self.word[index] == char:
                right += 1
            else:
                wrong += char
                unused += self.word[index]
        wrongpos = 0
        for char in wrong:
            i = unused.find(char)
            if i >= 0:
                wrongpos += 1
                unused = unused[:i] + unused[i + 1:]
        return (right, wrongpos)

    @staticmethod
    def choose_word(length=3):
        with open('/usr/share/dict/words') as dic:
            words = dic.read().splitlines()
        words = [word for word in words if len(word) == length and
                 word.islower() and word.isalpha()]
        out = random.choice(words)
        return out


def test():
    g = Game('cat')
    assert g.check('hat') == (2, 0)
    assert g.check('abt') == (1, 1)
    assert g.check('Ccc') == (1, 0)
    assert g.check('aaa') == (1, 0)
    assert g.check('TCa') == (0, 3)
    for length in range(2, 10):
        word = Game.choose_word(length=length)
        assert len(word) == length
        assert word.islower()
        assert word.isalpha()


def game_loop():
    g = Game(Game.choose_word(length=3))

    for i in range(10):
        guess = raw_input('Guess: ').strip()
        correct, misplaced = g.check(guess)
        if correct == len(g.word):
            print 'Win!'
            break
        print 'Correct:', correct, 'Misplaced', misplaced
    else:
        print 'You loose!',
    print 'Correct word is ', g.word


if __name__ == '__main__':
    test()
    game_loop()
