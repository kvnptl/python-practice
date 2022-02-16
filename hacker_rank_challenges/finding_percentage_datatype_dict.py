if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        line = input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = list(scores)
    query_name = input()
    
    sum = 0
    for i in student_marks[query_name]:
        sum+=i
    
    avg = sum/len(student_marks[query_name])
    print("{.2f}".format(avg))
