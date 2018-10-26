# -*- coding: utf-8 -*-
import json
import os
import socket

__all__ = ['AGENT_HOME', 'CONFIG_DIR', 'HOSTNAME']


AGENT_HOME = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'agent')
CONFIG_DIR = os.path.join(AGENT_HOME, 'config')


def _get_hostname():
    agent_conf_file = os.path.join(AGENT_HOME, 'config', 'cfg.json')
    if os.path.exists(agent_conf_file):
        with open(agent_conf_file, 'r') as f:
            agent_cfg_json = json.load(f)
            return agent_cfg_json['hostname']
    else:
        return socket.gethostname()


HOSTNAME = _get_hostname()
