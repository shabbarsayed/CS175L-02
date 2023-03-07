#Shabbar Sayed
#CS 175L 02
#Average and Grade Assignment

def main():
    scores = []
    for n in range (5):
        print('Enter score', n+1, ': ', end= '')
        x = int(input())
        scores.append(x)
        repeat
    return(scores)

def determine_grade(num):
    if 90 <= num <= 100:
        letter_grade = 'A'
    elif 80 <= num <= 89:
        letter_grade = 'B'
    elif 70 <= num <= 79:
        letter_grade = 'C'
    elif 60 <= num <= 69:
        letter_grade = 'D'
    else:
        letter_grade = 'F'
    return letter_grade

def calc_average (grades):
    avg = sum(grades)/len(grades)
    grade = determine_grade(avg)
    print("Average score: {:.1f} {}". format(avg, grade))

def show_letters(num, c, letter_grade):
    print("Score", c, ":" "{:.1f}     {}\n". format(num, letter_grade))


        
first = main()
print('')
print('Score      Numeric Grade    Letter Grade')
print('--------------------------------------------')
c = 0
for n in first:
    c = c+1
    show_letters(n, c, determine_grade(n))
calc_average(first)

