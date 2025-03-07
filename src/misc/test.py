candidates = ['Donald', 'Barack', 'Hillary', 'Mitt']
votes = [9, 7, 1, 3]
votes, candidates = (list(t) for t in zip(*sorted(zip(votes, candidates))[::-1]))
