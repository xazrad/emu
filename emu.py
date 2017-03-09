import random


G_RNB = 0
G_EH = 1
G_POP = 2
G_NONE = 3
GENRES = {G_RNB: 'RnB', G_EH: 'electrohouse', G_POP: 'pop'}
ACTIONS = {G_RNB: 'moves his body and head back and forth, crouched, arms bent'
                  ' at the elbows',
           G_EH: 'moves his body back and forth, doesnt move his head, his '
                 'arms move in circles, his legs are dancing to the beat',
           G_POP: 'slowly moves his body, head, legs and arms',
           G_NONE: 'goes to bar and drinks vodka'}


class Club:
    playing = None

    def __init__(self):
        self.people = []

    def change_music(self, genre):
        if genre in GENRES:
            print('Club changed music to {0}!'.format(GENRES[genre]))
            self.playing = genre
            for i, man in enumerate(self.people):
                man.change_state(genre)
                print('Man #{0} {1}!'.format(i + 1, ACTIONS[man.state]))
        else:
            print('This club doesnt play such music!')


class Man:
    state = None

    def __init__(self, genres):
        self.genres = genres

    def change_state(self, genre):
        self.state = genre if genre in self.genres else G_NONE

if __name__ == '__main__':
    club = Club()
    for i in range(random.randint(5, 15)):
        genres = []
        for g in GENRES:
            if random.random() >= 0.5:
                genres.append(g)
        club.people.append(Man(genres))
    tracklist = [random.randint(0, 2) for i in range(random.randint(5, 15))]
    for track in tracklist:
        club.change_music(track)
