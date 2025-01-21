debug_index = 0
class Citation:
    text = ''
    authors = []
    title = ''
    author_end = -1

    def __init__(self, text):
        self.text = text
        self.update_authors()
        self.update_title()

    def author_cleaner(a):
        and_idx = a.find('and')
        if and_idx >= 0:
            a = a[and_idx + len('and'):]

        return a.strip()

    def update_authors(self):
        if len(self.text) == 0:
            return

        # try to get author list using API with self.title
        # otherwise...
        author_end_index = self.text.index('.')
        is_initial = lambda x: x == 1 or (not self.text[x-2].isalpha())

        while is_initial(author_end_index):
            author_end_index += self.text[author_end_index+1:].index('.') + 1

        self.author_end = author_end_index
        all_authors = self.text[:author_end_index]
        self.authors = [Citation.author_cleaner(a) for a in all_authors.split(',')]
        return author_end_index


    def update_title(self):
        if len(self.text) == 0 or len(self.authors) == 0:
            return

        self.title = self.text[self.author_end+1:].split('.')[0] + '.'




def get_ref_list(references):
    index_open_split = references.split('[')
    ref_list = []
    citations = []

    for s in index_open_split:
        if len(s) == 0 or s.index(']') < 0:
            continue
        ref = s.split(']')[1].strip().replace('\n', ' ')
        ref_list.append(ref)
        citations.append(Citation(ref))


    return ref_list, citations

with open('refs.txt', 'r') as f:
    refs = f.read()


new_refs = refs.split('REFERENCES')[1].strip()

ref_list, citations = get_ref_list(new_refs)
'''
for r in ref_list[:len(ref_list)//5]:
    print(r)
    print()
'''

for c in citations[:]:
    print(c.authors)
    print(c.title)
