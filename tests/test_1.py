'''File doc string --> tells what it does
addiyion of two numbers
'''

import os
from script import addition

import sys

sys.path.insert(0, os.getcwd())

def test_add():
    subj = addition(7, 9)
    print(subj)
    assert subj == 16


test_add()  # call
