# Some tips from the book "Effective Python: 59 Specific Ways to Write Better Python"

def tip11():
    """
    Use ZIP to process iterators in parallel
    """
    print("|---tip11>")
    names = ['Cecilia', 'Lise', 'Marie']
    letters = (len(n) for n in names)

    longest_name = None
    max_letters = 0
    for name, count in zip(names, letters):
        if count > max_letters:
            longest_name = name
            max_letters = count
    print("Longest name ---> %s" % longest_name)
    print("Be careful with truncated output, when the lenght is not the same on all zipped lists")
    names.append("Rosalinda")
    # let's make 'letters' a list instead of a generator expression
    letters = [len(n) for n in names[:-1]]
    print("Names: %s" % str(names))
    for name, count in zip(names, letters):
        print("\t- %s" % name)
    print("<---|")

if __name__ == '__main__':
    print("<--- Tips and tricks from the book --->")
    tip11()
