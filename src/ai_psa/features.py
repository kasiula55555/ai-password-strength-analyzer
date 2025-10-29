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