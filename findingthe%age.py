if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    summ, avg = 0, 0
    for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    marks = student_marks[query_name]
    for i in marks:
        summ += float(i)
    avg = summ/len(marks)
    print(f'{avg:0.2f}')