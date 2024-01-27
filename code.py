from random import randint
 
import matplotlib.pyplot as plt
import seaborn as sns
 
 
MIN_NUM_PEOPLE = 2
MAX_NUM_PEOPLE = 100
NUM_POSSIBLE_BIRTHDAYS = 365
NUM_TRIALS = 10000
 
 
def generate_random_birthday():
    birthday = randint(1, NUM_POSSIBLE_BIRTHDAYS)
    return birthday
 
 
def generate_k_birthdays(k):
    birthdays = [generate_random_birthday() for _ in range(k)]
    return birthdays
 
 
def aloc(birthdays):
    unique_birthdays = set(birthdays)
 
    num_birthdays = len(birthdays)
    num_unique_birthdays = len(unique_birthdays)
    has_coincidence = (num_birthdays != num_unique_birthdays)
 
    return has_coincidence
 
 
def estimate_p_aloc(k):
    num_aloc = 0
    for _ in range(NUM_TRIALS):
        birthdays = generate_k_birthdays(k)
        has_coincidence = aloc(birthdays)
        if has_coincidence:
            num_aloc += 1
 
    p_aloc = num_aloc / NUM_TRIALS
    return p_aloc
 
 
def estimate_p_aloc_for_range(ks):
    k_probabilities = []
 
    for k in ks:
        p_aloc = estimate_p_aloc(k)
        k_probabilities.append(p_aloc)
         
    return k_probabilities
 
 
ks = range(MIN_NUM_PEOPLE, MAX_NUM_PEOPLE + 1)
k_probabilities = estimate_p_aloc_for_range(ks)
 
 
fig, ax = plt.subplots(figsize=(10, 10), dpi=49)
ax.set_facecolor('#F8F8FF')
ax.xaxis.set_tick_params(width=5, color='#009ACD')
ax.yaxis.set_tick_params(width=5, color='#009ACD')
 
sns.lineplot(x=ks, y=k_probabilities, color='#DC143C')
 
plt.xticks(fontsize=15, color='#030303')
x_range = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
y_range = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
plt.yticks(y_range, fontsize=15, color='#030303')
plt.grid()
plt.xlim([0, 75])
plt.ylim([0, 1])
plt.xlabel('Number of people', fontsize=30, color='#030303')
plt.ylabel('P(1 shared birthday)', fontsize=30, color='#030303')
 
plt.show()
