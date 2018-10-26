#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
import sys
import time

PLUGIN_HOME = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..')
sys.path.insert(0, PLUGIN_HOME)


def main():
    this_fn = os.path.basename(__file__).replace('.py', '')
    conf_json_file = os.path.join(CONFIG_DIR, this_fn + '.json')

    if os.path.exists(conf_json_file):
        with open(conf_json_file, 'r') as f:
            conf_json = json.load(f)
            if 'files' not in conf_json:
                return
            output = []
            pid_files = conf_json['files']
            for pid_file in pid_files:
                t = dict()
                t['metric'] = 'pid.file'
                t['endpoint'] = HOSTNAME
                t['timestamp'] = int(time.time())
                t['step'] = 60
                t['counterType'] = 'GAUGE'
                t['tags'] = 'name=' + parse_process_name(pid_file)
                t['value'] = 1 if os.path.exists(pid_file) else 0
                output.append(t)
            print json.dumps(output)


def parse_process_name(path):
    fn = os.path.basename(path)
    return fn.replace('.pid', '')


if __name__ == '__main__':
    from common import CONFIG_DIR, HOSTNAME

    main()
