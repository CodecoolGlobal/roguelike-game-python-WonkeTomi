import emoji

def create_char(name):
    main_character = {
        "NAME": name,
        "HP": 200,
        "MANA": 100,
        "EXP": 0,
        "LVL": 1,
        "BAG": [],
        "EMOJI": emoji.emojize(":baby:")}
    return main_character
# MOBOK

CROCODILE = {
    "HP": 50,
    "DEF": 10,
    "HELMET": 0,
    "CHEST": 0,
    "BOOTS": 0,
    "HAND": 0,
    "MANA": 100,
    "LVL": 1,
    "EMOJI": emoji.emojize(":crocodile:"),
    "SOUND": ""}

SKUNK = {
    "HP": 20,
    "DEF": 5,
    "HELMET": 0,
    "CHEST": 0,
    "BOOTS": 0,
    "HAND": 0,
    "MANA": 100,
    "LVL": 1,
    "EMOJI": emoji.emojize(":skunk:"),
    "SOUND": ""}

BUTTERFLY = {
    "HP": 20,
    "DEF": 1,
    "HELMET": 0,
    "CHEST": 0,
    "BOOTS": 0,
    "HAND": 0,
    "MANA": 100,
    "LVL": 1,
    "EMOJI": emoji.emojize(":butterfly:"),
    "SOUND": ""
}

IT = {
    "HP": 40,
    "DEF": 30,
    "HELMET": 0,
    "CHEST": 0,
    "BOOTS": 0,
    "HAND": 0,
    "MANA": 100,
    "LVL": 1,
    "EMOJI": emoji.emojize(":clown_face:"),
    "SOUND": ""}

DODO = {
    "HP": 30,
    "DEF": 10,
    "HELMET": 0,
    "CHEST": 0,
    "BOOTS": 0,
    "HAND": 0,
    "MANA": 100,
    "LVL": 1,
    "EMOJI": emoji.emojize(":dodo:"),
    "SOUND": ""}

MOSQUITO = {
    "HP": 5,
    "DEF": 1,
    "HELMET": 0,
    "CHEST": 0,
    "BOOTS": 0,
    "HAND": 0,
    "MANA": 100,
    "LVL": 1,
    "EMOJI": emoji.emojize(":mosquito:"),
    "SOUND": ""}

ZOMBIE = {
    "HP": 55,
    "DEF": 30,
    "HELMET": 1,
    "CHEST": 0,
    "BOOTS": 0,
    "HAND": 0,
    "MANA": 100,
    "LVL": 1,
    "EMOJI": emoji.emojize(":man_zombie:"),
    "SOUND": ""}

VAMPIRE = {
    "HP": 150,
    "DEF": 50,
    "HELMET": 0,
    "CHEST": 0,
    "BOOTS": 0,
    "HAND": 0,
    "MANA": 100,
    "LVL": 1,
    "EMOJI": emoji.emojize(":man_vampire_dark_skin_tone:"),
    "SOUND": ""}

# BOSSOK

PUTYIN_BOSS = {
    "HP": 2500,
    "DEF": 100,
    "HELMET": 0,
    "CHEST": 0,
    "BOOTS": 0,
    "HAND": 0,
    "MANA": 100,
    "EXP": 0,
    "LVL": 1,
    "EMOJI": emoji.emojize(":Russia:"),
    "SOUND": ""}


T_REX_BOSS1 = {
    "HP": 2000,
    "DEF": 70,
    "HELMET": 0,
    "CHEST": 0,
    "BOOTS": 0,
    "HAND": 0,
    "MANA": 100,
    "EXP": 0,
    "LVL": 1,
    "EMOJI": emoji.emojize(":T-Rex:"),
    "SOUND": ""}

CODECOOLER_BOSS2 = {
    "HP": 2250,
    "DEF": 1000,
    "HELMET": 0,
    "CHEST": 0,
    "BOOTS": 0,
    "HAND": 0,
    "MANA": 100,
    "EXP": 0,
    "LVL": 1,
    "EMOJI": emoji.emojize(":man_technologist:"),
    "SOUND": ""}

mobs = [CROCODILE, SKUNK, BUTTERFLY, MOSQUITO, ZOMBIE, IT, DODO, VAMPIRE]
bosses = [PUTYIN_BOSS, T_REX_BOSS1, CODECOOLER_BOSS2]
# print(main_character["EMOJI"])
