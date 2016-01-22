__author__ = 'Alec'

"""
Given: A file containing at most 1000 lines.

Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.

Sample Dataset:

Bravely bold Sir Robin rode forth from Camelot
Yes, brave Sir Robin turned about
He was not afraid to die, O brave Sir Robin
And gallantly he chickened out
He was not at all afraid to be killed in nasty ways
Bravely talking to his feet
Brave, brave, brave, brave Sir Robin
He beat a very brave retreat

Sample Output:

Yes, brave Sir Robin turned about
And gallantly he chickened out
Bravely talking to his feet
He beat a very brave retreat

"""
file_name = raw_input("File name? ")

# new line
print

the_file = open(file_name, "r")

# convert lines of file into list
lines = list(the_file)

the_file.close()

# print odd-numbered lines
for i in range(len(lines)):
    if (i%2 == 1):
        # strip escape character
        print lines[i].strip('\n')
