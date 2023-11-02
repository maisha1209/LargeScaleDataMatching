from settings import *
import Levenshtein


# Function to show progress during run time
counter = 0
def show_progress(operation):
    if print_distance and print_frequency and print_papers and print_similarity_score == False:
        global counter
        counter = counter + 1
        print(f'{operation} **** {counter} ****', end='\r')


# List of callback fuctions
callbacks = [
    # Print Callback
    lambda paper: print_paper(paper) if print_papers == True else None,
    # Hashtable Callbacks
    lambda paper: gen_hashtable(paper, k_value, DBLP_hashtable, 'DBLP') if DBLP_parsing == True and generate_dblp_hashtable == True else None,
    lambda paper: gen_hashtable(paper, k_value, MAG_hashtable, 'MAG') if MAG_parsing == True and generate_mag_hashtable == True else None,
    # Cost Callbacks
    lambda paper: get_frequency(paper, k_value, DBLP_hashtable, 'DBLP') if DBLP_parsing == True and generate_dblp_hashtable == True and calculate_frequency_dblp == True else None,
    lambda paper: get_frequency(paper, k_value, MAG_hashtable, 'MAG') if MAG_parsing == True and generate_mag_hashtable == True and calculate_frequency_mag == True else None,
    lambda paper: get_frequency(paper, k_value, DBLP_hashtable, 'MAG') if MAG_parsing == True and generate_mag_hashtable == True and DBLP_parsing == True and generate_dblp_hashtable == True and calculate_frequency_mag_dblp == True else None,
    lambda paper: get_frequency(paper, k_value, MAG_hashtable, 'DBLP') if MAG_parsing == True and generate_mag_hashtable == True and DBLP_parsing == True and generate_dblp_hashtable == True and calculate_frequency_dblp_mag == True else None,
    # Similarity Callbacks
    lambda paper: get_jaccard_similarity_score(paper, k_value, DBLP_hashtable, 'DBLP', 'DBLP', similaritiy_scores_dblp) if DBLP_parsing == True and generate_dblp_hashtable == True and get_similarity_score_dblp == True else None,
    lambda paper: get_jaccard_similarity_score(paper, k_value, MAG_hashtable, 'MAG', 'MAG', similaritiy_scores_mag) if MAG_parsing == True and generate_mag_hashtable == True and get_similarity_score_mag == True else None,
    lambda paper: get_jaccard_similarity_score(paper, k_value, DBLP_hashtable, 'MAG', 'DBLP', similaritiy_scores_mag_dblp) if DBLP_parsing == True and MAG_parsing == True and generate_dblp_hashtable == True and get_similarity_score_mag_dblp == True else None,
    lambda paper: get_jaccard_similarity_score(paper, k_value, MAG_hashtable, 'DBLP', 'MAG', similaritiy_scores_dblp_mag) if DBLP_parsing == True and MAG_parsing == True and generate_mag_hashtable == True and get_similarity_score_dblp_mag == True else None,
    # Levenshtein Distance
    lambda paper: get_levenshtein_distance(paper, titles, levenshtein_distances) if DBLP_parsing == True or MAG_parsing == True and calculate_levenshtein_distance == True else None,
]

# Definition of Callback Functions

# This function will print the Paper Information
def print_paper(paper):
    print("Paper Information:")
    print(f"File Source: {paper.file_source}")
    print(f"Paper ID: {paper.paper_id}")
    print(f"Title: {paper.title}")
    print(f"Author: {paper.author}")
    print(f"Year: {paper.year}")
    print(f"DOI: {paper.doi}")
    print(f"Pages: {paper.pages}")
    print(f"URL: {paper.url}")
    print(f"Publisher: {paper.publisher}")
    print("\n")


# This function will create the hash table consist of shingles and respective list of paper ids
def gen_hashtable(paper, k, hashtable, file_source):
    if paper.file_source == file_source:
        if paper.title:
            shingles = gen_k_shingles(paper.title, k)
            
            for shingle in shingles:
                if shingle not in hashtable:
                    hashtable[shingle] = [paper.paper_id]
                else:
                    hashtable[shingle].append(paper.paper_id)
        
        show_progress('Generating Hash Table')


# This function will generate k-shingles for a given string
def gen_k_shingles(text, k):
    shingles = set()
    for i in range(len(text) - k + 1):
        if lower_case_shingles == True:
            shingle = text[i:i + k].lower()
        else:
            shingle = text[i:i + k]

        shingles.add(shingle)

    return shingles


# This function will match the shingles of query title in a given hash table and calculate the frequency shingles among titles
def get_frequency(paper, k, hashtable, query_source, output):
    if paper.file_source == query_source and paper.title:
        title = paper.title
        frequency = 0

        shingles = gen_k_shingles(title, k)
        for shingle in shingles:
            try:
                for paper in hashtable[shingle]:
                    frequency = frequency + 1

                    if paper in output:
                        output[paper] += 1
                    else:
                        output[paper] = 1

            except KeyError as e:
                pass

        if frequency > 0 and print_frequency:
            print(F'Matching: "{title}" of {query_source}, Shingles Frequency: {frequency} in {len(output)} papers.')

        show_progress('Calculating Shingle Frequencies')


# This function will match the shingles of query title in a given hash table and calculate the similarity score among titles
def get_jaccard_similarity_score(paper, k, hashtable, query_source, target_source, output):
    if paper.file_source == query_source :
        title = paper.title
        if title:
            output.setdefault(paper.paper_id, {})

            shingles_1 = gen_k_shingles(title, k)
            for shingle in shingles_1:
                try:
                    for paper_id in hashtable[shingle]:
                        if paper_id != paper.paper_id:
                            if paper_id not in output[paper.paper_id]:
                                # get all shingles of paper
                                shingles_2 = set()
                                for key, value_list in hashtable.items():
                                    if paper_id in value_list:
                                        shingles_2.add(key)

                                # Calculate the Jaccard similarity coefficient
                                intersection = len(shingles_1.intersection(shingles_2))
                                union = len(shingles_1.union(shingles_2))
                                similarity = intersection / union
                                
                                if similarity >= similarity_threshold:
                                    output[paper.paper_id][paper_id] = similarity

                                    if print_similarity_score == True:
                                        print(F'Jaccard Similarity: \n{query_source} Paper ID: {paper.paper_id}, \n{target_source} Paper ID: {paper_id}, \nScore {similarity}\n')

                except KeyError as e:
                    pass
    
    show_progress('Calculating Similarity Scores')


# This function will calculate the Levenshtein distance and similarity score between two titles
# def get_levenshtein_distance(paper, output):
#     title1 = paper.title
#     if title1:
#         output.setdefault(title1, {})

#         for title2 in output:
#             if title1 != title2:
#                 # Calculate the Levenshtein distance between the two titles
#                 distance = Levenshtein.distance(title1, title2)
    
#                 # Calculate a similarity score (lower distance means higher similarity)
#                 max_length = max(len(title1), len(title2))
#                 similarity = 1 - (distance / max_length)

#                 if similarity >= levenshtein_similarity_threshold:
#                     output[title1].setdefault(title2, {})
#                     output[title1][title2]['distance'] = distance
#                     output[title1][title2]['similarity'] = similarity
    
#                     if print_distance:
#                         print(f'Levenshtein Distance:\nTitle 1: {title1}\nTitle 2: {title2}\nDistance: {distance}, Similarity: {similarity}\n')
    
#                     else:
#                         show_progress('Calculating Levenshtein Distances')
    
def get_levenshtein_distance(paper, titles, output):
    title1 = paper.title
    if title1:
        titles.append(title1)

        for title2 in titles:
            if title1 != title2:
                # Calculate the Levenshtein distance between the two titles
                distance = Levenshtein.distance(title1, title2)

                # Calculate a similarity score (lower distance means higher similarity)
                max_length = max(len(title1), len(title2))
                similarity = 1 - (distance / max_length)

                if similarity >= levenshtein_similarity_threshold:
                    if distance in output:
                        output[distance].append(title1)
                    else:
                        output.setdefault(distance, [])
                        output[distance].append(title1)

                    if print_distance:
                        print(f'Levenshtein Distance:\nTitle 1: {title1}\nTitle 2: {title2}\nDistance: {distance}, Similarity: {similarity}\n')

                    else:
                        show_progress('Calculating Levenshtein Distances')