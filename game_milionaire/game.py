#!/usr/bin/python3
import random
def get_content(fname):
    with open(fname) as f:
        cnt = f.readlines()
    return cnt
def content_write(fname, name, correct_answer):
    cnt = get_content(fname)
    with open(fname, "a") as f:
        f.write(name + ":")
        f.write(str(correct_answer) + "\n")


def meets_the_new_player():
    print("Hello what is your name?")
    gamer_name = input("My name is: ")
    print()
    print(f"{gamer_name}, welcome to the game 'Who wants to become a millionaire'".upper())
    print(f" Are you ready to become a millionaire? ".upper())
    answ = input("Enter yes or no: ")
    return gamer_name,answ


def milioner_game():
    gamer_name = ""
    answ = ""
    question_count = 0
    questions_been_asked = []
    questions_list = [i.strip() for i in get_content("question.txt")]

    def make_the_random_el(q_list):
        return random.shuffle(q_list)

    for el in range(len(questions_list)):
        if gamer_name == "":
            gamer_name,answ = meets_the_new_player()


        if answ.lower() == "yes":

            make_the_random_el(questions_list)
            questions = questions_list[el].split(",")
            if questions[0] in questions_been_asked:
                continue
            else:
                print(questions[0])
                answer_list = questions[1:]
                make_the_random_el(answer_list)
                print("  ".join(answer_list).lower())
                answer = input("Enter your answer: ")
                if answer.lower() == questions[1].lower():
                    print("This is a correct answer: ")
                    question_count += 1
                    questions_been_asked.append(questions[0])
                    if question_count == 10:
                        print("you won and you are now a virtual millionaire".upper())
                        break
                else:
                    print("Your answer is wrong")
                    print("you lose")
                    print(f"You have a {question_count} correct answer")
                    break

        elif answ.lower() == "no":
                print("OK! bye bye loser :D ")
                break
        else:
            print()
            print("please enter yes or no".upper())
            answ = input("ENTER YES OR NO!: ")
    content_write("gamers.txt", gamer_name, question_count)
milioner_game()
