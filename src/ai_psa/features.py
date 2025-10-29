import math
import re
from collections import Counter
from typing import Dict


cammon_pass = {
    "123456","password","123456789","qwerty","abc123","111111","123123","letmein",
    "admin","welcome","iloveyou","monkey","dragon","sunshine","princess"
}

sequences = ["abcdefghijklmnopqrstuvwxyz", "qwertyuiop", "asdfghjkl", "zxcvbnm", "0123456789"]

def shannon_entropy(passwd: str) -> float:
    #gdy pusty string
    if not passwd:
        return 0
    counts = Counter(passwd)
    n = len(passwd)

    return -sum((c/n) * math.log2(c/n) for c in counts.values())


def has_sequence(passwd:str, min_run:int = 3) -> bool:
    passwd_lower = passwd.lower()

    for seq in sequences:
        for i in range(len(seq) - min_run -1):
            run = seq[i:i+min_run]
            if run in passwd_lower or run[::-1] in passwd_lower:
                return True
        rseq = seq[::-1]
        for i in range(len(rseq) - min_run -1):
            run = rseq[i:i+min_run]
            if run in passwd_lower:
                return True
    return False

def repeated_characters(passwd:str)->float
    if not passwd:
        return 0.0
    counts = counter(passwd)
    most = max(counts.values())

    return most / len(passwd)

def char_classes(passws:str)->Dict[str,int]:
    classes = {
        "lower":0,
        "upper":0,
        "digit":0,
        "special":0
    }

    for c in passws:
        if c.islower():
            classes["lower"] += 1
        elif c.isupper():
            classes["upper"] += 1
        elif c.isdigit():
            classes["digit"] += 1
        else:
            classes["special"] += 1
    return classes

def features_main(passwd:str)->Dict[str,float]:
    classes = char_classes(passdw)
    len_passwd = len(passwd)
    diversity = sum(1 for v in classes.values() if v > 0)
    features = {
        "length": len_passwd,
        "diversity": diversity,
        "lowercase_count": classes["lower"],
        "uppercase_count": classes["upper"],
        "digit_count": classes["digit"],
        "special_count": classes["special"],
        "shannon_entropy": shannon_entropy(passwd),
        "has_sequence": int(has_sequence(passwd)),
        "repeated_char_fraction": repeated_characters(passwd),
        "is_common_password": int(passwd in cammon_pass)
    }
    features_order=[
        "length",
        "diversity",
        "lowercase_count",
        "uppercase_count",
        "digit_count",
        "special_count",
        "shannon_entropy",
        "has_sequence",
        "repeated_char_fraction",
        "is_common_password"
    ]

def vectorize_features(passwd:str):
    f = features_main(passwd)
    return [f[feat] for feat in features_order]
