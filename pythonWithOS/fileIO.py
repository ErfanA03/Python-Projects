#import os


"""
# One way of doing it.
file = open('test.txt', 'r')
content = file.read()
print(content)
file.close()


# Another way of doing it.
with open('test.txt', 'r') as f:
    content = f.read()
    print(content)
    f.close()
"""

"""
def writeData():
    data = '\nHello, World!'
    with open('test.txt', 'a') as f:
        f.write(data)
        f.close()
"""



def openFile():
    with open('test.txt', 'r') as f:
        content = f.read()
        print(content)

        f.close()


if __name__ == "__main__":
    openFile()

