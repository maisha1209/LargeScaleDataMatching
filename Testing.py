import gzip
from typing import List


        

class Paper:
 def __init__(self, mag_paper_id, doi_number, title):
        self.mag_paper_id = mag_paper_id
        self.doi_number = doi_number
        self.title = title


paper_list = []
def create_paper(line):

    fields = line.strip().split('\t')
   
    mag_paper_id = fields[0]
    doi_number = fields[2]
    title = fields[4]

    return Paper(mag_paper_id, doi_number, title)


#INSIDE LOOP -> 
#for line in file:

 #paper_obj = create_paper(line)
#paper_list.append(paper_obj)

with gzip.open('Papers.txt.gz','rt', encoding='utf-8') as f:
   # file_content=f.readlines()
    for line in f:
        print("paper_objcreatestart")
        paper_obj = create_paper(line)
        print("paper_objcreateend")
        paper_list.append(paper_obj)
        #print(paper_list[0].mag_paper_id, paper_list[0].doi_number,paper_list[0].title)        
