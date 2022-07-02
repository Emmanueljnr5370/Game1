import string

words = []
class Combinations:
    def findResult(self, record, output, n, size):
        if (len(output) == 4):
            words.append(output)
            print(output)
        if (n == 0):
            return
        i = 0
        while (i < size):
            self.findResult(record, output + str(record[i]), n - 1, size)
            i += 1

def main():
    task = Combinations()
    record = list(string.ascii_letters + string.digits)
    size = len(record)
    n = 4
    task.findResult(record, '', n, size)
main() 

print('length', len(words))
with open('C:/Users/User/OneDrive/Desktop/Game1/word3.txt','w') as file:
    for x in words:
        file.write(f'{x}\n')

# Landing.com        