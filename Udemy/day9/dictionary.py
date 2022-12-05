student_stcor={
    "ravi" : 80,
    "pathu": 75,
    "kishan": 85,
    "karu" :95,
    "other" :65,
}
student_status={}
for student in student_stcor:
    score=student_stcor[student]
    if score > 90:
        student_status[student]="oustanding"
    elif score >80:
        student_status[student]='expectations'
    elif score > 70:
        student_status[student]="acceptable"
    else:
        student_status[student]="fail"

print(student_status)