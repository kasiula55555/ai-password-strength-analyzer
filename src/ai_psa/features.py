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

