# normal version                     # shorter version

##score= int(input("Score: "))       ## score= int(input("Score: "))      

##if score >= 90 and score <= 100:   ## if 90 <= score <= 100: #
##    print("Grade: A")              ##    print("Grade: A")
##elif score >= 80 and score < 90:   ## elif 80 <= score < 90:
##    print("Grade: B")              ##    print("Grade: B")
##elif score >= 70 and score < 80:   ## elif 70 <= score < 80:
##    print("Grade: C")              ##    print("Grade: C")
##elif score >= 60 and score < 70:   ## elif 60 <= score < 70:#
##    print("Grade: D")              ##    print("Grade: D")
##else:                              ## else:
##    print("Grade: F")              ##    print("Grade: F") 

#more shorter version

score= int(input("Score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
