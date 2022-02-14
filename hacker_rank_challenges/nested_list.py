if __name__ == '__main__':

    student_scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_scores.append((name, score))

    # -------------
    # Ref: Example 3 | https://www.programiz.com/python-programming/methods/list/sort
    # use sorted(), if you don't want to change original list
    def takeSecond(elem):
        return elem[1]
    student_scores.sort(key=takeSecond)
    # -------------

    s = student_scores.pop(0)

    second_lowest = []

    while len(student_scores) > 0:
        if student_scores[0][1] != s[1]:
            for i in range(len(student_scores)):
                second_lowest.append(
                    student_scores[i][0])
                if i+1 < len(student_scores):
                    if student_scores[i][1] != student_scores[i+1][1]:
                        break
            break

        else:
            s = student_scores.pop(0)

    if len(second_lowest) > 1:
        second_lowest.sort()

    for i in second_lowest:
        print(i)
