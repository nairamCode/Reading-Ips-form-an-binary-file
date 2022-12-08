#u open the file u want to decode (open("[FILENAME]", "rb")
file_handler = open("ips", "rb")

#start a counter to count the ips
count = 0

#make a loop
while True:

    #u read the first byte
    byteone = file_handler.read(1)
    b1 = int.from_bytes(byteone, "big", signed=False)
    #if the first byte is 0 it will stop the script: Because an IP-Adress can't be 0 in the first digit it will stop when the list reach the bottom
    if b1 == 0:
        break
    #print
    print(str(b1) + ".", end='')

    #u read the second byte
    bytetwo = file_handler.read(1)
    b2 = int.from_bytes(bytetwo, "big", signed=False)
    #print
    print(str(b2) + ".", end='')

    #u read the third byte
    bytethree = file_handler.read(1)
    b3 = int.from_bytes(bytethree, "big", signed=False)
    #print
    print(str(b3) + ".", end='')

    #u read the fourht byte
    bytefour = file_handler.read(1)
    b4 = int.from_bytes(bytefour, "big", signed=False)
    #print
    print(str(b4) + ":", end='')

    #u read the last to bytes to get the port
    bytefive = file_handler.read(2)
    b5 = int.from_bytes(bytefive, "big", signed=False)
    #print
    print(str(b5))

    #sets the ip counter 1 up
    count = count + 1


print("\n", end='')
#print how many ips you have scanned
print("You scanned " + str(count) + " ips.")