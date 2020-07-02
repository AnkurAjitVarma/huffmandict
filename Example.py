from EntropyCoding import huffmandict
symbols = ['A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7']
probabilities = [0.25, 0.2, 0.15, 0.12, 0.1, 0.08, 0.05, 0.05]
dictionary, avg_len = huffmandict(symbols, probabilities)
print('%-10s\t%-10s\t%-10s'%('Symbols','Probabilities','Codewords'))
for n, i in enumerate(dictionary):
    print("%-9s\t%-10.2f\t%s"%(i, probabilities[n], dictionary[i]))
print('average word length = %0.2f'%(avg_len))
