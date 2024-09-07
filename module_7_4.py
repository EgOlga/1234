#Использование %:

print('В команде Мастера кода участников: %d !' % (5))
print('В команде Мастера кода участников: %(team1_num)d !' % {'team1_num' : 5})
print("Итого сегодня в командах участников: %(team1_num)s и %(team2_num)s !" % {'team1_num' : 5, 'team2_num' : 6})

team1 = 'Мастера кода'
team2 = 'Волшебники данных'
team1_num = 5
team2_num = 6
print('В команде %s участников: %d!' % (team1, team1_num))
print("Итого сегодня в командах участников: %d и %d!" % (team1_num, team2_num))

#Использование format():
score_1 = 40
score_2 = 42
print("Команда {} решила задач: {}!".format(team2, score_2))
team1_time = 18015.2
print("{} решили задачи за {} с !".format(team2, team1_time))

#Использование f-строк:
print(f"Команды решили {score_1} и {score_2} задач.")

team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2

def challenge_result(score_1, score_2, team1_time, team2_time):
    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        result = 'Победа команды Мастера кода!'
        print(f'Результат битвы: {result}')
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        result = 'Победа команды Волшебники Данных!'
        print(f'Результат битвы: {result}')
    else:
        result = 'Ничья!'
        print(f'Результат битвы: {result}')
challenge_result(score_1, score_2, team1_time, team2_time)

print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.")
