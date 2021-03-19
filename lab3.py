import lab2
from math import log, factorial

possibilities = [0.5, 0.6, 0.7, 0.8, 0.85, 0.9, 0.92, 0.94]
linkMatrix = [[0, 1, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 1, 1, 0, 0, 0],
              [0, 0, 0, 1, 0, 1, 0, 1],
              [0, 0, 0, 0, 1, 1, 0, 1],
              [0, 0, 0, 0, 0, 1, 1, 0],
              [0, 0, 0, 0, 0, 0, 1, 1],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0]]

'''possibilities = [0.74, 0.14, 0.56, 0.35, 0.20, 0.21]
linkMatrix = [[0, 0, 1, 1, 1, 0],
              [0, 0, 1, 1, 0, 1],
              [0, 0, 0, 1, 1, 1],
              [0, 0, 0, 0, 1, 1],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0]]'''
t = 1000
k1 = 1
k2 = 1

possibility = lab2.lab2(possibilities, linkMatrix)
qssibility = 1 - possibility
t_average = -t / log(possibility)
print("Базова імовірність безвідмовної роботи = {}\n"
      "Базова імовірність відмови = {}\n"
      "Базовий середній наробіток на відмову = {}\n".format(possibility, qssibility, t_average))


def loaded_joint(t, k, qssib, possib, t_aver):
    q_1 = 1 / factorial(k + 1) * qssib
    p_1 = 1 - q_1
    t_aver1 = -t / log(p_1)
    g_q1 = q_1 / qssib
    g_p1 = p_1 / possib
    g_t1 = t_aver1 / t_aver
    print("Імовірність безвідмовної роботи системи з навантаженим загальним резервуванням = {}\n"
          "Імовірність відмови системи з навантаженим загальним резервуванням = {}\n"
          "Середній час роботи системи з навантаженим загальним резервуванням = {}".format(p_1, q_1, t_aver1))
    print("Виграш системи з навантаженим загальним резервуванням по імовірності безвідмовної роботи = {}\n"
          "Виграш системи з навантаженим загальним резервуванням по імовірності відмови = {}\n"
          "Виграш системи з навантаженим загальним резервуванням по середньому часу роботи = {}\n".format(g_p1, g_q1, g_t1))


def loaded_distributed(t, k, qssib, poss, possib, t_aver, link_mat):
    new_possibilities = list(map(lambda x: 1 - (1 - x) ** (k + 1), possib))
    p_2 = lab2.lab2(new_possibilities, link_mat)
    q_2 = 1 - p_2
    t_aver2 = -t / log(p_2)
    g_q2 = q_2 / qssib
    g_p2 = p_2 / poss
    g_t2 = t_aver2 / t_aver
    print("Імовірність безвідмовної роботи системи з навантаженим розподіленим резервуванням = {}\n"
          "Імовірність відмови системи з навантаженим розподіленим резервуванням = {}\n"
          "Середній час роботи системи з навантаженим розподіленим резервуванням = {}".format(p_2, q_2, t_aver2))
    print("Виграш системи з навантаженим розподіленим резервуванням по імовірності безвідмовної роботи = {}\n"
          "Виграш системи з навантаженим розподіленим резервуванням по імовірності відмови = {}\n"
          "Виграш системи з навантаженим розподіленим резервуванням по середньому часу роботи = {}\n".format(g_p2, g_q2, g_t2))


loaded_joint(t, k1, qssibility, possibility, t_average)
loaded_distributed(t, k2, qssibility, possibility, possibilities, t_average, linkMatrix)
