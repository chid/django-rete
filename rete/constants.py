# -*- coding: utf-8 -*-

EQ_IDX = 1
NE_IDX = 2
LT_IDX = 3
LE_IDX = 4
GT_IDX = 5
GE_IDX = 6
OPERATION_INDEXES = [
    EQ_IDX,
    NE_IDX,
    LT_IDX,
    LE_IDX,
    GT_IDX,
    GE_IDX
]

EQ_SYM = '='
NE_SYM = '≠'
LT_SYM = '<'
LE_SYM = '≤'
GT_SYM = '>'
GE_SYM = '≥'
OPERATION_NAMES = [
    EQ_SYM,
    NE_SYM,
    LT_SYM,
    LE_SYM,
    GT_SYM,
    GE_SYM,
]

OPERATIONS = list(zip(OPERATION_INDEXES,OPERATION_NAMES))
OP_IDX_TO_NAME = dict(OPERATIONS)
OP_NAME_TO_IDX = dict(list(zip(OPERATION_NAMES,OPERATION_INDEXES)))

DC = DONT_CARE = '?'