# def file_read(file_name):
#     file = open(file_name, mode='r', encoding='utf-8')
#     print(file.read())
#     file.close()
#
# def file_n_lines(file_name: str, n: int) -> None:
#     file = open(file_name, mode = 'r',encoding='utf-8')
#     for i in range(n):
#         print(file.readline(), end = '')
#     file.close()
#
#
# def create_file_with_numbers(n):
#     name = f"range_{n}.txt"
#     file =open(name, mode='a', encoding = 'UTF-8')
#     for i in range(1, n+1):
#         file.write(str(i)+'\n')




# from string import punctuation
#
# a = punctuation
#
# def longest_word_in_file(file_name):
#     a = punctuation
#     new = []
#     file = open(file_name, mode='r', encoding = 'UTF-8')
#     file = file.read().split()
#     num = 0
#     max = ''
#     for w in file:
#         w= w.strip(a)
#         if len(w) >= num:
#             num = len(w)
#             max = w
#     else:
#         new.append(max)
#     return str(*new)

# file = open('numbers.txt', mode='r', encoding = 'UTF-8')
# file = file.read().split()
# print(file)
# count = 0
# summ = 0
# for num in file:
#     if len(num) == 3:
#         count+=1
#     if len(num) == 2:
#         summ+=int(num)
# print(count)
# print(summ)


# def find_lines_len_more_6(file_name: str) -> int:
#     with open(file_name, 'r') as f:
#         x = [str(i) for i in f.read().splitlines()]
#         a = 0
#         for i in x:
#             if len(i) > 6:
#                 a += 1
#         return a


# with open('lorem.txt', 'r') as f:
#     x = f.read().split()
#     new = []
#     words = {}
#     for i in x:
#         new.append(i.upper())
#     for i in new:
#         words[i] = new.count(i)




with open('words.txt', 'r', encoding = 'UTF-8') as f:
    x = f.read().split()
    new = set(x)
    new = list(new)
    more = []
    for i in new:
        if i[-2:] == 'ея':
            more.append(i.upper())
    more = set(more)
    more = list(more)
    more.sort(key=lambda item: (len(item), item))
    for i in more:
        print(i)





