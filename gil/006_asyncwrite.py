#!/usr/bin/python
# -*- coding: utf-8 -*-


import time
import threading


class AsyncWrite(threading.Thread):

    def __init__(self, text, out):
        super(AsyncWrite, self).__init__()
        self.text = text
        self.out = out

    def run(self):
        with open(self.out, 'a') as f:
            f.write(self.text + '\n')
        time.sleep(2)
        print('Finished background writing to {}'.format(self.out))


def main():
    msg = raw_input('Enter your string to store:\n')
    bkg = AsyncWrite(msg, 'out.text')
    bkg.start()
    print('The program continue to run while it write in another thread')
    print(123 + 424)
    bkg.join()
    print('Wait until background thread completed')

if __name__ == '__main__':
    main()
