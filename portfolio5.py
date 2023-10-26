temp = []
for i in range(5):
    string = input(" enter temp in celsius along with C:")
    if string[-1] == "C":
      celsius = float(string[:-1])
      temp.append(celsius)
    else:
        print("invalid input")
        exit(1)
high = max(temp)
low = min(temp)
mean = sum(temp) / len(temp)
print("max temp :", high)
print("min temp:", low)
print("mean temp: ", mean)