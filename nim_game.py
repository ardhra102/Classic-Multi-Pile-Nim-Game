#                     ----Classic Multi-Pile Nim Game-----


def works(pile,ch,turn):
    if ch>3 or ch<=0:
        print(f"\nRules Violated!!\nRemoving the no. of objects should not exceed 3...")
        return None
    elif ch>len(pile):
        print(f"\nInsufficient Objects\nYou have only {len(pile)} objects ")
        return None
    else:

        l1=len(pile)-ch
        pile=pile[0:l1]
        if pile=="":
            pile="❌"
        return pile

print("\n"," "*23,"🎮 Classic Multi-Pile Nim Game\n")
print(" "*20,"Welcome to the Classic Multi-Pile Nim Game!\n")
print("Rules:\n\n1.There are multiple piles of objects.\n2.Two players take turns playing.\n3.On your turn, choose only one pile.\n4.You may remove 1, 2, or 3 objects only from the selected pile.")
print("5.You cannot remove more than 3 objects in a single turn.\n6.You cannot remove more objects than are available in the selected pile.\n7.You cannot choose an empty pile.\n8.The player who removes the last remaining object wins the game.")

num_piles={"PileA":"👑"*5,"PileB":"👑"*7,"PileC":"👑"*4}
turn=1
for i,j in num_piles.items():
    print(f"\n{i} - {j}")

print("\n🚀--GAME STARTED--🚀")
n=num_piles.values()
while list(n)!=["❌","❌","❌"]:
    print(f"\n** Player{turn}'s Turn **\n")
    p=input("Enter pile:")
    if p not in num_piles:
        print(f"Invalid Pile!!\nChoose Valid Pile..")
        continue
    elif num_piles[p]=="❌":
        print("\nIt's Empty!!\nChoose Another Pile..")
        continue
    no=int(input("Enter no. of objects to remove:"))
    rs=works(num_piles[p],no,turn)
    if rs is not None:
        num_piles[p]=rs
        print(f"\n---Remaining---")
        for i, j in num_piles.items():
            print(f"\n{i} - {j}")
        winner=turn
        if turn==1:
            turn=2
        else:
            turn=1
print(f"\nAll Piles becomes Empty!!!")
print(f"\n✦✦✦GAME ENDED✦✦✦")
print(f"\nWINNER 🏆 : PLAYER{winner} ")






