import gzip
from paper import Paper


def parse_data(file_path, callbacks, papers_count, file_source='DBLP'):
    def process_line(line, paper, file_source):
        if file_source == 'DBLP':
            if 'key="' in line:
                key_start = line.find('key="') + 5
                key_end = line.find('"', key_start)

                if key_start != -1 and key_end != -1:
                    paper.paper_id = line[key_start:key_end]

            elif '<title>' in line:
                paper.title = line.replace('<title>', '').replace('</title>', '').strip()

            elif '<author>' in line:
                paper.author = line.replace('<author>', '').replace('</author>', '').strip()

            elif '<year>' in line:
                paper.year = line.replace('<year>', '').replace('</year>', '').strip()

            elif '<ee' in line:
                doi_value = line.replace('<ee', '').replace('</ee>', '').strip()
                doi_value = doi_value.replace('https://doi.org/', '')
                paper.doi = doi_value

            elif '<pages>' in line:
                paper.pages = line.replace('<pages>', '').replace('</pages>', '').strip()

            elif '<url>' in line:
                paper.url = line.replace('<url>', '').replace('</url>', '').strip()

            elif '<publisher>' in line:
                paper.publisher = line.replace('<publisher>', '').replace('</publisher>', '').strip()

        elif file_source == 'MAG':
            fields = line.strip().split('\t')

            if fields[0]:
                paper.paper_id = fields[0]
            
            if fields[2]:
                paper.doi = fields[2]

            if fields[4]:
                paper.title = fields[4]

            if fields[7]:
                paper.year = fields[7]

            if fields[9]:
                paper.publisher = fields[9]


    def run_callback(paper):
        for callback in callbacks:
            callback(paper)
            
        paper = None


    current_paper = None

    with gzip.open(file_path, 'rt', encoding='utf-8') as zip_file:
        parsed_papers = 0

        for current_line in zip_file:
            if parsed_papers == papers_count:
                break
            
            if file_source == 'DBLP':
                opening_tags = ['<article', '<inproceedings', '<incollection', '<book']
                closing_tags = ['</article>', '</inproceedings>', '</incollection>', '</book']
                
                # Start Paper
                if any(tag in current_line for tag in opening_tags):
                    current_paper = Paper()
                
                # End & Start Paper
                elif any(close_tag in current_line and open_tag in current_line for close_tag, open_tag in zip(closing_tags, opening_tags)):
                    run_callback(current_paper)
                    current_paper.file_source = file_source
                    parsed_papers += 1

                # End Paper
                elif any(tag in current_line for tag in closing_tags):
                    current_paper.file_source = file_source
                    parsed_papers += 1
                    run_callback(current_paper)

                if current_paper:
                    process_line(current_line, current_paper, file_source)

            elif file_source == 'MAG':
                current_line = current_line.encode('utf-8', errors='replace').decode('utf-8')
                current_paper = Paper()
                process_line(current_line, current_paper, file_source)
                current_paper.file_source = file_source
                parsed_papers += 1
                run_callback(current_paper)

    return parsed_papers