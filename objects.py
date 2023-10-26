class Object:
    def _init_(self, author, doi, year, pages, title, url, published_through, source): 
        self.author = author
        self.doi = doi
        self.year = year
        self.pages = pages
        self.title = title
        self.url = url
        self.published_through = published_through
        self.source = source

# Create a paper object
paper1 = Object(author=author, doi=doi, year=year, pages=pages, title=title, url=url, published_through=published_through, source=Source)

# Access the attributes
print("Author:", paper1.author)
print("DOI:", paper1.doi)
print("Year:", paper1.year)
print("pages", paper1.pages)
print("title", paper1.title)
print("url", paper1.url)
print("published_through", paper1.published_through)
print("source", paper1.source)
