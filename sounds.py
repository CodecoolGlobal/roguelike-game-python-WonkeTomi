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
