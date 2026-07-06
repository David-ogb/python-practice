import time

timer = int(input("How long will you like to set the timer to: "))

for x in range(timer, 0, -1):
    seconds = x % 60
    print(f"00:00:{seconds}")
    time.sleep(1)

print("Time's UP!")