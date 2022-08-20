class Trie():
    def __init__(self, char=None):
        self.value = char
        self.children = {}
        self.word = False
    
    def add_word(self, word):
        for char in word:
            if char not in self.children:
                self.children[char] = Trie(char)
            self = self.children[char]
        self.word = True

    def is_word(self, word):
        for char in word:
            if char not in self.children:
                return False
            self = self.children[char]
        if self.word:
            return True
        return None

    def print_trie(self, prefix=""):
        if self.word:
            print(prefix)
        for char in self.children:
            self.children[char].print_trie(prefix+char)


base = Trie()

with open('/Users/evan/leetcode/word_searches/countries') as f:
    lines = f.readlines()

flag = False
search = []
for line in lines:
    if '::' in line:
        flag = True
    if flag:
        for each in line.split(" "):
            base.add_word(each.strip())
    else:
        search.append(line.strip().replace('\n','').replace('\t',''))


res = []
c, r = len(search[0]), len(search)

rows = [""]*r
cols = [""]*c
diag = [""] * (max(r,c)+1)

for i,each in enumerate(search):
    rows[i] = each
    for j,val in enumerate(each):
        cols[j] += val
        diag_ind = (c*i+j)%(c+1)
        diag[diag_ind] += val
print(diag)
for row in rows:
    for j in range(c):
        for k in range(j+1, c+1):
            temp = base.is_word(row[j:k])
            if temp == True:
                res.append(row)
                j = k
                break
            if temp == False:
                break
            temp = base.is_word(row[j:k][::-1])
            if temp == True:
                res.append(row)
                j = k
                break


for col in cols:
    for i in range(r):
        for j in range(i+1, r+1):
            temp = base.is_word(col[i:j])
            if temp == True:
                res.append(col)
                i = j
                break
            if temp == False:
                break
            temp = base.is_word(col[i:j][::-1])
            if temp == True:
                res.append(col)
                i = j
                break


            
print(res)