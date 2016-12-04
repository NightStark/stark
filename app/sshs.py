# -*- coding: utf-8 -*-
# !/usr/bin/python
import paramiko
import threading


class SshCmd:
    def __init__(self, cmd):
        self.cmd = cmd


class RemoteSsh:
    result_list = []

    def __init__(self, ip, username, password, port=22, timeout=5):
        self.ip = ip
        self.username = username
        self.password = password
        self.port = port
        self.timeout = timeout
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def connect(self):
        try:
            print("connect to:[ip: " + self.ip +
                  "\n\rport: " + self.port.__str__() +
                  "\n\rusername: " + self.username +
                  "\n\rpassword: " + self.password +
                  "\n\rtimeout:" + self.timeout.__str__() + "]\n")
            self.ssh.connect('192.168.98.1', 22, "bhuroot", "Bihu400!%**%^^", timeout=5)
            print('%s\t connect OK\n' % (ip))
        except:
            print('%s\tError\n' % (ip))

    def dis_connect(self):
        self.ssh.close()

    def run_cmd(self, cmd):
        try:
            for m in cmd:
                stdin, stdout, stderr = self.ssh.exec_command(m)
                # stdin.write("Y")   #简单交互，输入 ‘Y’
                out = stdout.readlines()
                self.result_list.append(out)
                # 　print(out)
                # 屏幕输出
                '''
                for line in out:
                    line = line.strip('\n')
                    print(line)
                    '''

                print('%s\tOK\n' % (ip))
            return
        except:
            print('%s\tError\n' % (ip))

    def get_result(self):
        return self.result_list


def ssh2(ip, username, password, cmd):
    rssh = RemoteSsh(ip, username, password)
    rssh.connect()
    rssh.run_cmd(cmd)
    rssh.dis_connect()
    result = rssh.get_result()
    #print(result)
    for lines in result:
        print(lines)
        for line in lines:
            line = line.__str__().strip('\n')
            print(line)



cmd = ['date', 'echo hello!', 'sleep 1 && ps']  # 你要执行的命令列表
username = "bhuroot"  # 用户名
password = "Bihu400!%**%^^"  # 密码
threads = []  # 多线程
print("Begin......")
# for i in range(1, 254):
ip = '192.168.98.1'
#a = threading.Thread(target=ssh2, args=(ip, username, password, cmd))
#a.start()

ssh2(ip, username, password, cmd)