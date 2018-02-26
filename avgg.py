if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

##marks_of_student = list(student_marks[query_name])
result = 0
##for x in marks_of_student:
##    result +=x
##
##print('{:.2f}'.format(result/3))
for x in student_marks[query_name]:
    result +=x

print('{:.2f}'.format(result/len(student_marks[query_name])))
