DBLP_file_path = 'datasets/dblp.xml.gz'
MAG_file_path = 'datasets/Papers.txt.gz'

# Summary at the end of parsing
write_short_summary = True                  # Print short summary at the end of parsing
write_long_summary = True                  # Print detailed summary at the end of parsing if applicable

# Parsing of DBLP
DBLP_parsing = True                         # Set to True for parsing of DBLP dataset
DBLP_paper_count = 100                      # No of papers to be parsed from DBLP dataset
DBLP_hashtable = {}                         # Don't change this line. DBLP hashtable saved in this variable
generate_dblp_hashtable = True              # Set to True for generation of hashtable for DBLP dataset

# Parsing of MAG
MAG_parsing = False                          # Set to True for parsing of MAG dataset
MAG_paper_count = 10                        # No of papers to be parsed from MAG dataset
MAG_hashtable = {}                          # Don't change this line. MAG hashtable saved in this variable
generate_mag_hashtable = True               # Set to True for generation of hashtable for MAG dataset

# K shingle settings
k_value = 3                                 # Hashtables are generated using K-Shingle method. This sets the value of K
lower_case_shingles = True                  # Set to True if you need hashtable in lower case

# Print Callback Function
print_papers = False                        # Set to True if you want to print paper information of each parsed paper

# Shingle Frequency Callback Functions
frequencies = {}                            # Don't change this line, All calculated frequencies saved in this variable
print_frequency = True                      # Set to True if you want to print the frequencies

calculate_frequency_dblp = False            # Calculate shingle frequency of each paper in DBLP dataset with respect to same dataset             
calculate_frequency_mag = False             # Calculate shingle frequency of each paper in MAG dataset with respect to same dataset
calculate_frequency_dblp_mag = False        # Calculate shingle frequency of each paper in DBLP dataset with respect to each paper in MAG dataset
calculate_frequency_mag_dblp = False        # Calculate shingle frequency of each paper in MAG dataset with respect to each paper in DBLP dataset

# Similarity Callback Functions
similaritiy_scores_dblp = {}                # Don't change this line. DBLP similarity score saved in this variable 
similaritiy_scores_mag = {}                 # Don't change this line. MAG similarity score saved in this variable 
similaritiy_scores_dblp_mag = {}            # Don't change this line. DBLP_MAG similarity score saved in this variable 
similaritiy_scores_mag_dblp = {}            # Don't change this line. MAG_DBLP similarity score saved in this variable 

similarity_threshold = 0.5                  # Save or print information of papers having similarity score >= similarity_threshold
print_similarity_score = False              # To print similarity score of each paper

get_similarity_score_dblp = False           # Get similarity score of each paper in DBLP dataset with respect to same dataset
get_similarity_score_mag = False            # Get similarity score of each paper in MAG dataset with respect to same dataset
get_similarity_score_dblp_mag = False       # Get similarity score of each paper in DBLP dataset with respect to each paper in MAG dataset
get_similarity_score_mag_dblp = False       # Get similarity score of each paper in MAG dataset with respect to each paper in DBLP dataset

# Levenshtein Distance Callback Function
titles = []                                 # Don't change this line. Parsed titles saved in this variable
levenshtein_distances = {}                  # Don't change this line. Lavenshtein distance saved in this variable
levenshtein_similarity_threshold = 0.5      # Save or print information of papers having similarity score >= levenshtein_similarity_threshold
print_distance = True                      # To print Lavenshtein distance between each pair of titles
calculate_levenshtein_distance = True       # Calculate Lavenshtein distance between two titles