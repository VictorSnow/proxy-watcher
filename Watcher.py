#!/bin/python

import subprocess


class watcher:
    def __init__(self, check_cmd, start_cmd):
        self.check_cmd = check_cmd
        self.start_cmd = start_cmd

    def append_crontab(self):
        # @todo append crontab auto
        return self

    def check(self):
        p = subprocess.Popen(self.check_cmd, shell=True,
                             stdout= subprocess.PIPE, stderr= subprocess.PIPE)
        out, err = p.communicate()

        if out and out > 0:
            # alive
            print "alive"
        else:
            # not alive
            p = subprocess.Popen(self.start_cmd, shell=True,
                                 stdout= subprocess.PIPE, stderr= subprocess.PIPE)

if __name__ == 'main':
    check_cmd = 'pgrep beam'
    start_cmd = 'cd /home/erlang-proxy-tunnel/bin && erl -noshell -detached -s back back_start'
    watcher(check_cmd, start_cmd).append_crontab().check()