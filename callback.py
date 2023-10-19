class Callback:
    def __init__(self,paper_list):
        self.paper_list = paper_list

    def print_paper(self):

        for elem in self.paper_list:
            authors_str = ", ".join(elem['Authors:'])
            print("")
            print("Title: " + elem['Title'])
            print("List of Authors: " + authors_str)
            print("Year: " + elem['Year'])
            print("Journal: " + elem['Journal'])
            print("EE: " + elem['EE'])
            print("mdate: " + elem["Mdate"])
            print("key: " + elem["Key"])
            print("publtype: " + elem["Publtype"])
            print("")
            print("-----------------------------------------------------------------------------------")

    def count_paper(self):
        print("Completing paper object creation...")
        print("Total " + str(len(self.paper_list)) + " paper objects created")
