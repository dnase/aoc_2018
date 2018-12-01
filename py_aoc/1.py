# save input list as "input_1" - one number per line
seq = [int(s) for s in open("input_1").readlines()]

# question 1
print("Question 1: %d" % sum(seq))

# question 2 - naive solution, but it works
previous_freqs = [0]
current_freq = 0
while 1:
    for delta in seq:
        current_freq += delta
        if current_freq in previous_freqs:
            print("Question 2: %d" % current_freq)
            quit()
        previous_freqs.append(current_freq)
