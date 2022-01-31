import pandas as pd
import matplotlib.pyplot as plt
target_list = [217, 241, 317, 277, 674, 511, 804, 786, 346, 637, 431, 433, 58, 269, 588, 584, 340, 780, 335, 657]
def prediction_shift(model, attack_type,attack_size):
    count = 0
    sum = 0
    directory = "C://Users//user//Desktop//Bachelor Project//dataset//filmtrust//Prediction Shift//"
    raw_dit = directory + model + "_raw.txt"
    #print(raw_dit)
    attack_dit = directory + model + "_" + attack_type + "_" + str(attack_size) + ".txt"
    #print(attack_dit)
    raw = pd.read_csv(raw_dit, names=['user', 'item', 'rating', 'pred_rating'], sep=' ')
    raw = raw[raw['item'].isin(target_list)]
    attack = pd.read_csv(attack_dit, names=['user', 'item', 'rating', 'pred_rating'], sep=' ')
    attack = attack[attack['item'].isin(target_list)]
    for line in raw.itertuples():
        user = line[1]
        item = line[2]
        temp = attack[(attack['user'] == user) & (attack['item'] == item)]
        if temp.size != 0:
            count += 1
            sum += temp.iloc[0][3] - line[4]
        else:
            continue
    return sum/count

label_y = []
for i in [0.03, 0.06, 0.09, 0.12, 0.15]:
    label_y.append(prediction_shift('RSTE', 'random', i))
    label_x = [0.03, 0.06, 0.09, 0.12, 0.15]
print(label_y)