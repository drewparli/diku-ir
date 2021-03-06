from __future__ import division
import math
import matplotlib
import matplotlib.pyplot as plt
import nltk


if __name__ == '__main__':

    f = open("karamazov.txt", 'r')
    raw_text = f.read()

    p1 = [".", "-", "'", "`", '"', ",", "!", "?", "(", ")", ":", ";"]
    p2 = ["_", "\x80", "\x86", "\n", "\xc3", "\x90", "\x92", "\x94", "\x99", "\x98", "\x9d", "\x9c", "\xa6", "\xa9", "\xa8", "\xaf", "\xc5", "\xbc", "\xe2", "\xa0", "\xb4" ]

    for p in p1:
        raw_text = raw_text.replace(p, "")

    for p in p2:
        raw_text = raw_text.replace(p, " ")

    # divide each chapter
    chapters = raw_text.split("BBBBB")
    n_chapters = len(chapters)
    # print "Found {} chapters".format(n_chapters)


    words_per_chapter = list()
    xs = list()
    acc = 0
    # find the length of each chapter
    for i in range(n_chapters):
        c = chapters[i]
        text = c.split(" ")
        ws = [ word.lower() for word in text if word.isalpha() ]
        words_per_chapter.append(ws)
        acc += len(ws)
        xs.append(acc)

    wordset_per_chapter = list()
    # find the distinct set of words for each chapter
    for i in range(n_chapters):
        chapter = words_per_chapter[i]
        ws = { word for word in chapter }
        wordset_per_chapter.append(ws)

    ys = list()
    acc = set()
    for c in wordset_per_chapter:
        acc = acc.union(c)
        ys.append(len(acc))

    print max(xs)

    plt.figure(figsize=(16, 8))
    matplotlib.rcParams.update({'font.size': 20})
    plt.plot(xs, ys, 'r.-', label="word")
    plt.axis( [0,max(xs)+500,0,16000] )

    xs = range(0, max(xs)+500, 500)

    k,b = 21, 0.5
    heap = lambda x: x**(b) * k
    plt.plot(xs, map(heap, xs), 'b-', label="Heaps")

    # plt.loglog(xs_rank, ys_freq_zipf, 'k--', label="zipf")
    plt.title("Analysis of Heaps' Law\nThe Brother's Karamazov by Fyodor Dostoyevsky\n\n$k=21, b=0.5$")
    plt.xlabel(r"text length")
    plt.ylabel(r"frequency")
    plt.grid(True)
    plt.legend(loc=4)
    plt.tight_layout()
    # plt.show()
    plt.savefig("../latex/figures/heaps.pdf")
