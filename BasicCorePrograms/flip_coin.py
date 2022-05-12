#importing libraries
import random

print(" Flip Coin Problem ")
# defining function for flipping coin
def flipCoin():
    heads=0
    tails=0
    numberOfFlips = int(input("How many times you want to flip a coin? \n"))
    for flip in range(numberOfFlips):
        flipValue = random.random()
        print("Flip Value", flip+1, ":", flipValue)
        if flipValue<0.50:
            tails = tails + 1
        else:
            heads = heads + 1
    print("Heads:", heads , "Tails:", tails)
    # printing percentages of heads and tails
    headPercent = (heads/numberOfFlips)*100
    tailPercent = (tails/ numberOfFlips)*100
    print("Head Percentage:",headPercent, "Tails Percentages: ",tailPercent)


if __name__ == "__main__":
        flipCoin()