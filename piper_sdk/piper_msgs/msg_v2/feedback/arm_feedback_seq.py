#!/usr/bin/env python3
# -*-coding:utf8-*-
import math
from typing_extensions import (
    Literal,
)
class ArmMsgFeedbackSeq:
    '''
    '''
    def __init__(self, 
                 seq:int = 0,
                 seq1:int = 0,
                 seq2:int = 0,
                 seq3:int = 0                 
                 ):
        self.seq = seq
        self.seq1 = seq1
        self.seq2 = seq2
        self.seq3 = seq3

    def __str__(self):
        return (f"ArmMsgFeedbackSeq(\n"
                f"  seq: {self.seq},\n"
                f"  seq1: {self.seq1},\n"
                f"  seq2: {self.seq2},\n"
                f"  seq3: {self.seq3},\n"
                f")")

    def __repr__(self):
        return self.__str__()
