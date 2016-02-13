def wordcount(content):
    return len(str.split(content))

with open('../../../common/shakespeare.txt','rt') as fh:
    print('Words:', wordcount(fh.read()))
