poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
'''

# w for writing
f = open('poem.txt', 'w')
# write the poem
f.write(poem)
# close the file
f.close()

# r for read
f = open('poem.txt')
while True:
    line = f.readline()
    # 0 - eof
    if len(line) == 0:
        break
    print(line, end='')
f.close()
