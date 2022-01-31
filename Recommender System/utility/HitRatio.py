import pandas as pd
target_list = [217, 241, 317, 277, 674, 511, 804, 786, 346, 637, 431, 433, 58, 269, 588, 584, 340, 780, 335, 657]
def hit_ratio(model, attack_type,attack_size, N):
    count = 0
    directory = "C://Users//user//Desktop//Bachelor Project//dataset//filmtrust//Prediction Shift//"
    raw_dit = directory + model + "_raw.txt"
    attack_dit = directory + model + "_" + attack_type + "_" + str(attack_size) + ".txt"
    df = pd.read_csv(attack_dit, names=['user', 'item', 'rating', 'pred_rating'], sep=' ')
    user_list = list(df['user'].unique())
    U = len(user_list)
    for user in user_list:
        topN = sorted(list(df[df['user']==user]['pred_rating']))[0:5]







label_y = []
N = 5
for i in [0.03, 0.06, 0.09, 0.12, 0.15]:
    label_y.append(hit_ratio('RSTE', 'random', i,N))
    label_x = [0.03, 0.06, 0.09, 0.12, 0.15]
print(label_y)