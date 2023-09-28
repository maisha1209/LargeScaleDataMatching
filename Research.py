import gzip
import xml.etree.ElementTree as ET



with gzip.open('dblp.xml.gz','rt',encoding='UTF-8') as f:
   
   
    article_data = []
    inside_article = False
    current_article = ""

    for line in f:
        # Start of an article tag
    
        if '<article' in line:
          
            inside_article = True
            current_article = line
        elif inside_article:
            current_article += line
        # End of an article tag
        if '</article>' in line:
            
            inside_article = False
            article_data.append(current_article)
            current_article = ""

# Process each article one at a time
#print(article_data[0])
#print("end")
paper_list = []



for article_content in article_data:
    # Parse and process the article using ElementTree
    parser=ET.XMLParser(encoding="utf-8")
    article = ET.fromstringlist([article_content], parser=parser)
   
    paper = {
        'mdate': article.get('mdate'),
        'key': article.get('key'),
        'publtype': article.get('publtype'),
        'authors': [author.text for author in article.findall('author')],
        'title': article.find('title').text,
        'journal': article.find('journal').text,
        'year': int(article.find('year').text),
        'link': article.find('ee').text
    }
    
   
    paper_list.append(paper)
   

for elem in paper_list:
    print(elem)






