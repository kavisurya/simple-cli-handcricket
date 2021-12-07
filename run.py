import random

score_B = 0
score_A = 0
user_input = 0
ready = 0

print("\n\n\n\n\n\n----     Y O U R    B A T T I N G    -----")
while True:
    comp_val = random.randint(1, 6)
    user_input = int(input("[+]  BATTING : "))
    if user_input == comp_val:
        print("\n\n\n\n[-]  Outttttttttttttttttttttttttttttttttt")
        print("Your Score is : ",score_A,"\t","Bowler : ",comp_val,"\tYour Taget : ",score_A+1)
        target = score_A+1
        ready = 1
        break

    else:
        score_A = score_A + user_input
        print("[+]  Your score : ",score_A,"\t","Bowler : ",comp_val)

if ready == 1:
    print("\n\n\n\n\n\n----     Y O U R    B O W L I N G    -----")
    ready_input = input("Are you ready : yes/no : ")
    if("yes" == ready_input):
        while True:
            comp_val = random.randint(1, 6)
            user_input = int(input("[+]  BOWLING: "))
            if user_input == comp_val:
                print("\n\n\n\n[-]  Outttttttttttttttttttttttttttttttttt")
                print("[+]  Opponent Score is : ", score_B, "\t", "Bowler : ",user_input,"\tOpponent : ",comp_val, "\tOpponent Taget : ", score_B + 1,"\tTargrt : ",target)
                if target < score_B:
                    print("[+]  OPPONENT WINS THE MATCH")
                elif target == score_B:
                    print("[+]  MATCH DRAW")
                elif target > score_B:
                    print("[+]  YOUR WINS THE MATCH ")
                else:
                    print("[+]  CONTACT THIRD UMPIRE :)")
                break

            else:
                score_B = score_B + comp_val
                print("[+]  Opponent score : ", score_B, "\t", "Your Bowling : ", user_input,"\tOpponent : ",comp_val,"\tTarget : ",target)
                if score_B > target:
                    print("[+]  Opponent wins the match")
                    break
                elif target == score_B:
                    print("[+]  MATCH DRAW")
    else:
        print("[+]  wait some times !!!")
