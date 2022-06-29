import emoji


main_character = {
    "NAME": "",
    "HP": 200,
    "ATK": 0,
    "DEF": 0,
    "MANA": 100,
    "EXP": 0,
    "LVL": 1,
    "BAG": [],
    "EMOJI": emoji.emojize(":baby:")}

# MOBOK

CROCODILE = {
    "HP": 50,
    "ATK": 0,
    "DEF": 10,
    "HAND": 0,
    "MANA": 100,
    "LVL": 1,
    "EMOJI": emoji.emojize(":crocodile:"),
    "SOUND": ""}

SKUNK = {
    "HP": 20,
    "ATK": 0,
    "DEF": 5,
    "HAND": 0,
    "MANA": 100,
    "LVL": 1,
    "EMOJI": emoji.emojize(":skunk:"),
    "SOUND": ""}

BUTTERFLY = {
    "HP": 20,
    "ATK": 0,
    "DEF": 1,
    "HAND": 0,
    "MANA": 100,
    "LVL": 1,
    "EMOJI": emoji.emojize(":butterfly:"),
    "SOUND": ""
}

IT = {
    "HP": 40,
    "ATK": 0,
    "DEF": 30,
    "HAND": 0,
    "MANA": 100,
    "LVL": 1,
    "EMOJI": emoji.emojize(":clown_face:"),
    "SOUND": ""}

DODO = {
    "HP": 30,
    "ATK": 0,
    "DEF": 10,
    "HAND": 0,
    "MANA": 100,
    "LVL": 1,
    "EMOJI": emoji.emojize(":dodo:"),
    "SOUND": ""}

MOSQUITO = {
    "HP": 5,
    "ATK": 0,
    "DEF": 1,
    "HAND": 0,
    "MANA": 100,
    "LVL": 1,
    "EMOJI": emoji.emojize(":mosquito:"),
    "SOUND": ""}

ZOMBIE = {
    "HP": 55,
    "ATK": 0,
    "DEF": 30,
    "HELMET": 1,
    "CHEST": 0,
    "BOOTS": 0,
    "HAND": 0,
    "MANA": 100,
    "LVL": 1,
    "EMOJI": emoji.emojize(":zombie:"),
    "SOUND": ""}

VAMPIRE = {
    "HP": 150,
    "ATK": 0,
    "DEF": 50,
    "HAND": 0,
    "MANA": 100,
    "LVL": 1,
    "EMOJI": emoji.emojize(":vampire:"),
    "SOUND": ""}

# BOSSOK

PUTYIN_BOSS = {
    "HP": 2500,
    "ATK": 0,
    "DEF": 100,
    "HAND": 0,
    "MANA": 100,
    "EXP": 0,
    "LVL": 1,
    "EMOJI": emoji.emojize(":Russia:"),
    "SOUND": ""}


T_REX_BOSS1 = {
    "HP": 2000,
    "ATK": 0,
    "DEF": 70,
    "HAND": 0,
    "MANA": 100,
    "EXP": 0,
    "LVL": 1,
    "EMOJI": emoji.emojize(":T-Rex:"),
    "SOUND": ""}

CODECOOLER_BOSS2 = {
    "HP": 2250,
    "ATK": 0,
    "DEF": 1000,
    "HAND": 0,
    "MANA": 100,
    "EXP": 0,
    "LVL": 1,
    "EMOJI": emoji.emojize(":laptop:"),
    "SOUND": ""}

mobs = [CROCODILE, SKUNK, BUTTERFLY, MOSQUITO, ZOMBIE, IT, DODO, VAMPIRE]
bosses = [PUTYIN_BOSS, T_REX_BOSS1, CODECOOLER_BOSS2]
# print(main_character["EMOJI"])
