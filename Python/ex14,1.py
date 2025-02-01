from sys import argv

script, user_name, kit = argv
prompt = '>+< '

print(f"Привет, {user_name} {kit}, я - сценарий {script}.")
print("Я хочу задать тебе несколько вопросов.")
print(f"Я тебе нравлюсь, {user_name} {kit}?")
likes = input(prompt)

print(f"Где ты живешь, {user_name} {kit}?")
lives = input(prompt)

print("На каком компьютере ты работаешь?")
computer = input(prompt)

print("Ты любишь")

print(f"""
Итак, ты ответил {likes} на вопрос, нравлюсь ли я тебе.
Ты живешь {lives}.НЕ ПРЕДСТАВЛЯЮ где это
И у тебя есть компьютер {computer}. Прекрасно!
""")
