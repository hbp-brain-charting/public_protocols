import os

data_file = 'wordlist.txt'
data_folder = '.'

input_encoding = 'cp1252' # latin-1 or utf-8 instead 
output_encoding = 'utf-8'

if not os.path.exists(data_folder):
    os.makedirs(data_folder)


with open(data_file, 'rb') as f:
    for line in f:
        line = line.decode(input_encoding)
        name, value = line.strip().split(':')
        filename = os.path.join(data_folder, name) + '.txt'
        print('writing to %s' % filename)
        with open(filename, 'wb') as out:
            out.write(value.encode(output_encoding))
