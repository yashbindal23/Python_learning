question=[
    ['How many sides are there in square?\nA. 4\tB. 3\nC. 5\tD. 10\nEnter your option: ', 'A', 1000],
    ['How many sides are there in triangle?\nA. 4\tB. 3\nC. 5\tD. 10\nEnter your option: ', 'B', 1000],
    ['How many sides are there in pentagon?\nA. 4\tB. 3\nC. 5\tD. 10\nEnter your option: ', 'C', 2000],
    ['How many sides are there in decagon?\nA. 4\tB. 3\nC. 5\tD. 10\nEnter your option: ', 'D', 4000],
    ['National bird of India?\nA. pigeon\tB. cock\nC. peacock\tD. eagle\nEnter your option: ', 'C', 8000],
    ['National animal of India?\nA. pigeon\tB. cock\nC. peacock\tD. eagle\nEnter your option: ', 'C', 8000],
    ['capital of India?\nA. pigeon\tB. cock\nC. peacock\tD. eagle\nEnter your option: ', 'C', 8000],
    ['National fruit of India?\nA. pigeon\tB. cock\nC. peacock\tD. eagle\nEnter your option: ', 'C', 8000],
    ['PM of India?\nA. pigeon\tB. cock\nC. peacock\tD. eagle\nEnter your option: ', 'C', 8000]
]

money = 0

for i in range(0,len(question)):
    q = question[i]
    print(q[0])
    s = input('')
    if s == q[1]:
        print(f'you entered right answer\n you won {q[2]} for this question\n\n')
        if i==2:
            money = 10000
        elif i==9:
            money = 100000
        elif i==14:
            money = 10000000
        elif i==17:
            money = 70000000
    else:
        print('wrong answer')
        break
print('money you won:',money)
