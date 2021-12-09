class Wordplay:
    def __init__(self, words_list):
        self.words_list = words_list

    def words_with_length(self, length):
        my_list_length = [ i for i in self.words_list if len(length) == len(i)]
        return my_list_length
    def starts_with(self, s):
        my_list_length = [i for i in self.words_list if s == i[0]]
        return my_list_length
    def ends_with(self, s):
        my_list_length = [i for i in self.words_list if s == i[-1]]
        return my_list_length
    def palindromes(self):
        my_list_length = [i for i in self.words_list if i == i[::-1]]
        return my_list_length
    def only(self, L):
        my_list_length = [i for i in self.words_list if L in i]
        return my_list_length
    def avoids(self, L):
        my_list_length = [i for i in self.words_list if L not in i ]
        return my_list_length

x = Wordplay(['asddsa', 'Karl', 'Lisa', 'ada'])
print(x.words_with_length('ada'))
print(x.starts_with('a'))
print(x.ends_with('l'))
print(x.palindromes())
print(x.only('L'))
print(*x.avoids('L'))





