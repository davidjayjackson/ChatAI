#!/usr/bin/env python

import pandas as pd

def signal(data, moving_average):
    signal = []
    for i in range(len(data)):
        if data['close'][i] > moving_average[i]:
            signal.append('Buy')
        else:
            signal.append('Sell')
    return signal

def main(file, window):
    data = pd.read_csv(file)
    data['moving_average'] = data['close'].rolling(window=window).mean()
    data['signal'] = signal(data, data['moving_average'])
    return data

if __name__ == '__main__':
    file = input('Enter file name: ')
    window = int(input('Enter window size: '))
    output_file = input('Enter output file name: ')
    output = main(file, window)
    output.to_csv(output_file, index=False)
    print("The output has been written to {}".format(output_file))
