from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import os


train_cmd = 'python ./part1.py  '
eval_cmd = 'python ./part2.py '

if __name__ == '__main__':

    print('current working dir [{0}]'.format(os.getcwd()))
    w_d = os.path.dirname(os.path.abspath(__file__))
    print('change wording dir to [{0}]'.format(w_d))
    os.chdir(w_d)

    for i in range(30):
        
        print('################    train    ################')
        p = os.popen(train_cmd)
        for l in p:
            print(p.strip())

        # eval
        print('################    eval    ################')
        p = os.popen(eval_cmd)
        for l in p:
            print(p.strip())
