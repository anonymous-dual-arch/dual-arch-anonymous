import json
import argparse
import os
import sys
import multiprocessing
from datetime import datetime
from trainer import train

# genetype of stable network
code = [4, 64, [1, 2, 3, 4, 4], [1, 2, 3, 4, 4]]


def load_json(settings_path):
    with open(settings_path) as data_file:
        param = json.load(data_file)

    return param


def setup_parser():
    parser = argparse.ArgumentParser(description='Reproduce of multiple continual learning algorthms.')
    parser.add_argument('--config', type=str, default='./exps/foster_t.json',
                        help='Json file of settings.')

    return parser

class TrainModel(object):
    def __init__(self, gpu_id, file_id):
        self.code = code
        self.file_id = file_id
        self.gpu_id = gpu_id

    def process(self):
        args = setup_parser().parse_args()
        param = load_json(args.config)
        args = vars(args)  # Converting argparse Namespace to a dict.
        args.update(param)  # Add parameters from json

        args['device'] = [str(self.gpu_id)]
        args['seed'] = [1993]

        args['depth'] = self.code[0]
        args['width'] = self.code[1]
        args['pool'] = self.code[2]
        args['double'] = self.code[3]

        aia = 0.0
        
        aia = train(args, self.file_id)
        return round(aia,3)


    def log_record(self, _str, first_time=None):
        dt = datetime.now()
        dt.strftime( '%Y-%m-%d %H:%M:%S' )
        if first_time:
            file_mode = 'w'
        else:
            file_mode = 'a+'
        f = open('./log/%s.txt'%(self.file_id), file_mode)
        f.write('[%s]-%s\n'%(dt, _str))
        f.flush()
        f.close()


if __name__ == '__main__':
    m=TrainModel(gpu_id=0, file_id="foster-dual_arch-cifar-inc10-t3")
    m.process()
