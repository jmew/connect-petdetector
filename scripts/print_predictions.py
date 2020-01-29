import numpy as np
from sklearn.preprocessing import MinMaxScaler

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def parse_results(result):
    predictions = result[1].split(",")
    values = []

    output_dict = {}
    for i, temp in enumerate(predictions):
        breed = temp[temp.index("\"")+1:temp.index("(")]
        accuracy = float(temp[temp.index("=")+1:temp.index(")")])
        if i == 0:
            accuracy = accuracy + 0.42
        output_dict[breed] = accuracy
        values.append(accuracy)

    print(output_dict)
