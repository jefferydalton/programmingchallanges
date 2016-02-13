with open('../../../common/shakespeare.txt','rt') as fh:
    content = fh.read()
    count = len(str.split(content))
    print('Words:',count)
