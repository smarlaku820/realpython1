from random import choice
n = []
v = []
a = []
ad = []
p = []


def makePoem():
    if a[0][0] in ['a', 'e', 'o', 'i', 'u']:
        custom_letter = 'An'
    else:
        custom_letter = 'A'
    return """{} {} {}
    \n{} {} {} {} {} the {} {}
{}, the {} {}
the {} {} {} a {} {}
    """.format(custom_letter, a[0], n[0], custom_letter, a[0], n[0], v[0], p[0], a[1], n[1], ad[0], n[0], v[1], n[1], v[2], p[1], a[2], n[2])


def build_vocab(lis, num):
    voc = []
    while num != 0:
        word = choice(lis)
        if word not in voc:
            voc.append(word)
            num -= 1
    return voc


if __name__ == "__main__":
    nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
    verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
    adjectives = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening", "ambient", "erroneous"]
    adverbs = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]
    prepositions = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]
    n = build_vocab(nouns, 3)
    v = build_vocab(verbs, 3)
    a = build_vocab(adjectives, 3)
    ad = build_vocab(adverbs, 1)
    p = build_vocab(prepositions, 2)
    poem = makePoem()
    print(poem)