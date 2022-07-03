import sys

current_key = None
word_sum = 0
sys.stdin = "1cf54b530128257d72 4cdf3efa01036a9a48 8c3e7fb30261aaf9cf 4cfe6230016553c3ed 76e1b8690176f801bb \
 e7409c39013c9db7b4 a5f1519c02b22550e6 83a119ef02346d0879"

for line in sys.stdin:
    try:
        key, count = line.strip().split()
        count = int(count)
    except ValueError as e:
        continue
    if current_key != key:
        if current_key:
            print("{}\t{}".format(current_key, word_sum))
        word_sum = 0
        current_key = key
    word_sum += count

if current_key:
    print("{}\t{}".format(current_key, word_sum))
