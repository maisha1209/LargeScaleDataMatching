import gzip

with gzip.open('dblp.xml.gz','rb') as f:
    file_content=f.readlines(1000)
    for line in file_content:
        print(line)
     