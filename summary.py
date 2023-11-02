from settings import *

def write_summary(duration, dblp_papers, mag_papers):
        # Print summary of parsing
    print('----------------------------------------------')
    print('SUMMARY')
    print('----------------------------------------------')
    print(f'Simulation Duration: {duration}')
    print(f'DBLP Papers Parsed: {dblp_papers}')
    print(f'MAG Papers Parsed: {mag_papers}')
    print(f'Total Papers Parsed: {dblp_papers + mag_papers}\n')

    if DBLP_parsing == True and generate_dblp_hashtable == True:
        print('DBLP hash table generated.')

    if MAG_parsing == True and generate_mag_hashtable == True:
        print('MAG hash table generated.')

    # Print summary of similarity scores
    get_similarity_score_summary(similaritiy_scores_dblp, 'DBLP', 'DBLP')
    get_similarity_score_summary(similaritiy_scores_mag, 'MAG', 'MAG')
    get_similarity_score_summary(similaritiy_scores_dblp_mag, 'DBLP', 'MAG')
    get_similarity_score_summary(similaritiy_scores_mag_dblp, 'MAG', 'DBLP')

    # Print summary of levenshtein distances
    get_lavenshtein_distance_summary(levenshtein_distances)


def get_similarity_score_summary(similarity_scores, query_dataset, target_dataset):
    if similarity_scores:
        print('\n----------------------------------------------')
        print(f'Similarity: {query_dataset} vs {target_dataset}')
        print('----------------------------------------------')
        
        similarities = 0
        for query_paper, paper in similarity_scores.items():
            scores = [score for key, score in paper.items()]

            try:
                average = sum(scores)/ len(scores)
                similarities = similarities + 1
                if write_long_summary == True:
                    print(f'Title of Paper ID "{query_paper}" is similar to {len(paper)} papers with average score of {average}.')
            except:
                pass

        if similarities == 0:
            print(f'No similarity found considering given similarity threshold of {similarity_threshold}.')
        
        else:
            print(f'Titles having similarity score >= {similarity_threshold}: {similarities}')


def get_lavenshtein_distance_summary(lavenshtein_distances):
    if lavenshtein_distances:
        print('\n----------------------------------------------')
        print(f'Lavenshtein Distances between Titles')
        print('----------------------------------------------')

        total_similar_titles = 0
        total_unique_similar_titles = 0
        total_duplicate_titles = 0

        for distance, titles in lavenshtein_distances.items():
            similar_titles = len(titles)
            unique_similar_titles = len(set(titles))
            duplicate_titles = similar_titles - unique_similar_titles

            total_similar_titles = total_similar_titles + similar_titles
            total_unique_similar_titles = total_unique_similar_titles + unique_similar_titles
            total_duplicate_titles = total_duplicate_titles + duplicate_titles

            if write_long_summary:
                print(f'Lavenshtein Distance: {distance}')
                print(f'Similar Titles: {similar_titles}')
                print(f'Duplicate Titles: {duplicate_titles}')
                print(f'Unique Similar Titles: {unique_similar_titles}\n')
            
        if total_similar_titles == 0:
            print(f'No similarity found considering given Levenshtein similarity threshold of {levenshtein_similarity_threshold}.')
        
        else:
            print(f'Levenshtein Similarity Threshold: {levenshtein_similarity_threshold}')
            print(f'Total Similar Titles: {total_similar_titles}')
            print(f'Total Duplicate Titles: {total_duplicate_titles}')
            print(f'Total Unique Similar Titles: {total_unique_similar_titles}')
            