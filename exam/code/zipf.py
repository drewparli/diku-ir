from __future__ import division
import math
import matplotlib
import matplotlib.pyplot as plt
import nltk

def zipf(rank, C=1, alpha=1):
    """ Returns frequency according to Zipfs law """
    return C / (rank**alpha)


if __name__ == '__main__':

    # read in all the raw text
    f = open("karamazov.txt", 'r')
    raw_text = f.read()

    # define non-alphanumeric characters
    p1 = [".", "-", "'", "`", '"', ",", "!", "?", "(", ")", ":", ";", "BBBBB"]
    p2 = ["_", "\x80", "\x86", "\n", "\xc3", "\x90", "\x92", "\x94", "\x99", "\x98", "\x9d", "\x9c", "\xa6", "\xa9", "\xa8", "\xaf", "\xc5", "\xbc", "\xe2", "\xa0", "\xb4" ]

    # remove punctuation
    for p in p1:
        raw_text = raw_text.replace(p, "")

    for p in p2:
        raw_text = raw_text.replace(p, " ")

    # tokenize the text
    raw_text = raw_text.split(" ")
    ws = [ word.lower() for word in raw_text if word.isalpha() ]

    # calculate frequency of each word
    freq = dict()
    for word in set(ws):
        freq[word] = 0

    for word in ws:
        freq[word] += 1

    # restructure results for plotting
    ys_freq = list()
    xs_rank = list()
    i = 1
    for (w, f) in sorted(freq.items(), key = lambda i: i[1], reverse=True):
        ys_freq.append(f)
        xs_rank.append(i)
        i += 1

    # generate theoretical data
    ys_freq_zipf = list()
    C = max(ys_freq)
    for r in xs_rank:
        f = zipf(r, C, alpha=1)
        ys_freq_zipf.append(f)

    # Generate a plot
    plt.figure(figsize=(16, 8))
    matplotlib.rcParams.update({'font.size': 20})
    plt.loglog(xs_rank, ys_freq, 'r.-', label="word")
    plt.loglog(xs_rank, ys_freq_zipf, 'k--', label="zipf")
    plt.title("Analysis of Zipf's Law for the text of\nThe Brother's Karamazov by Fyodor Dostoyevsky\n\n$C=6969, \\alpha=1.0$")
    plt.xlabel(r"log rank")
    plt.ylabel(r"log frequency")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("../latex/figures/zipf.pdf")
