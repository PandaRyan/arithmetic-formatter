def arithmetic_arranger(problems, show_answers=False):
    oriproblems = problems
    topproblem = ''
    bottomproblem = ''
    line = ''
    answerline = ''
    error = False
    done = False
    temperror = False
    if len(problems) <= 5:
        while not error and not done:
            totalcount = 0
            for x in problems:
                temptop = '  '
                tempbottom = ''
                tempanswer = ''
                problemone = True
                problemtwo = False
                problemonecount = 0
                problemtwocount = 0
                for y in x:
                    if y == '+' or y == '-':
                        problemone = False
                        problemtwo = True
                        addition = True

                        if y == "-":
                            addition = False

                    else:
                        try:
                            int(y)

                        except:
                            if y == "*" or y == "/":
                                problems = "Error: Operator must be '+' or '-'."
                                error = True
                            elif y == '"':
                                error = True
                            elif y == ' ':
                                temperror = True
                            else:
                                problems = 'Error: Numbers must only contain digits.'
                                error = True

                        if not error and not temperror:
                            if problemone:
                                temptop = temptop+y
                                problemonecount = problemonecount+1
                                if problemonecount > 4:
                                    problems = 'Error: Numbers cannot be more than four digits.'
                                    error = True
                            else:
                                tempbottom = tempbottom+y
                                problemtwocount = problemtwocount+1
                                if problemtwocount >4:
                                    problems = 'Error: Numbers cannot be more than four digits.'
                                    error = True

                        temperror = False

                if show_answers:
                    if addition:
                        answer = int(temptop)+int(tempbottom)
                    else:
                        answer = int(temptop)-int(tempbottom)

                    answer = str(answer)
                

                if not error:
                    if problemonecount >= problemtwocount:
                        if problemonecount == problemtwocount:
                            if addition:
                                temp = "+ "
                            else:
                                temp = "- "
                        else:
                            tempp = problemonecount-problemtwocount
                            if addition:
                                temp = "+ "
                            else:
                                temp = "- "

                            for z in range(tempp):
                                temp = temp+" "

                        tempbottom = temp+tempbottom
                    else:
                        tempp = problemtwocount-problemonecount
                        if addition:
                            temp = "+ "
                        else:
                            temp = "- "

                        tempbottom = temp+tempbottom
                        temp = ""

                        for x in range(tempp):
                            temp = temp+" "

                        temptop = temp+temptop
                                    
                    if len(temptop) >= len(tempbottom):
                        for x in range(len(temptop)):
                            line = line+"-"

                    if show_answers:
                        xx = len(temptop)-len(answer)
                        for a in range(xx):
                            tempanswer = tempanswer+" "
                        tempanswer = tempanswer+answer

                totalcount = totalcount+1
                
                if totalcount != len(oriproblems):
                    topproblem = topproblem + temptop + "    "
                    bottomproblem = bottomproblem + tempbottom + "    "
                    line = line + "    "
                    if show_answers: 
                        answerline = answerline+tempanswer+ "    "
                else:
                    topproblem = topproblem + temptop
                    bottomproblem = bottomproblem + tempbottom
                    if show_answers: 
                        answerline = answerline+tempanswer

                if not error:
                    problems = topproblem+"\n"+bottomproblem+"\n"+line
                    if show_answers:
                        problems = problems+"\n"+answerline


            done = True
                    
    else:
        problems = 'Error: Too many problems.'


    return problems

