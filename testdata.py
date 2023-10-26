import gzip
import objects

class Paper:
    def __init__(self, mag_paper_id, doi_number, title):
        self.mag_paper_id = mag_paper_id
        self.doi_number = doi_number
        self.title = title

def create_paper(line):
    fields = line.strip().split('\t')
    mag_paper_id = fields[0]
    doi_number = fields[2]
    title = fields[4]
    return Paper(mag_paper_id, doi_number, title)

def process_paper_callback(paper):
    paper_info = {
        'mag_paper_id': paper.mag_paper_id,
        'doi_number': paper.doi_number,
        'title': paper.title
    }
   # print("Processing paper:", paper_info)
    objects.MyObject = paper_info
    object_list = []


    object_list.append(objects.MyObject)

    print(object_list)
    
paper_list = []

def levenshtein_length_comparison(dataset_A, dataset_B):
    title_lengths_A = [len(paper.title) for paper in dataset_A if paper.title is not None]
    title_lengths_B = [len(title) for title in dataset_B if title is not None]

    # Calculate Levenshtein distances and store them in a list
    distances = []
    for length_A in title_lengths_A:
        for length_B in title_lengths_B:
            distance = abs(length_A - length_B)
            distances.append(distance)

    return distances

def read_file_with_callback(file_path, callback):
    with gzip.open(file_path, 'rt', encoding='utf-8') as f:
        for line in f:
            paper_obj = create_paper(line)
            callback(paper_obj)
            paper_list.append(paper_obj)


if __name__ == "__main__":
 read_file_with_callback('Papers.txt.gz', process_paper_callback)
