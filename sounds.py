import pygame


def init_music_player():
    pygame.init()
    pygame.mixer.init()


def play_sound():
    pygame.mixer.music.play(-1)


def stop_sound():
    pygame.mixer.music.stop()


def load_sound(sound_file_name):
    pygame.mixer.music.load(sound_file_name)


def playsound_background_music():
    init_music_player()
    sound1 = pygame.mixer.Sound("Willow_Escape.wav")
    pygame.mixer.find_channel().play(sound1)


def playsound_next_room():
    init_music_player()
    sound1 = pygame.mixer.Sound('walking_2.wav')
    pygame.mixer.find_channel().play(sound1)


def playsound_error():
    init_music_player()
    load_sound('error_1.wav')
    pygame.mixer.music.play(loops=0)
