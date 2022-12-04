import csv

def seasonCalculator(season):
    filename = ('FinalPremierLeagueData.csv')
    with open(filename, encoding = "UTF-8") as MyFile: 
        csv_reader =csv.reader(MyFile)
        line_count=0
        Data=[]
        for row in csv_reader:
          if line_count==0:
            Header=row
          else:
            Data.append(row)
          line_count=line_count+1


    numOfPlayers = 0
    totalAge = 0
    totalGoals = 0

    ## col[0] col[3] col[11]
    for j in range(0, len(Data)):
        if Data[j][1] == season:
           numOfPlayers += 1
           totalAge += int(Data[j][3])
           totalGoals += int(Data[j][11])
    
    averageAge = round(totalAge / numOfPlayers, 2)
    
#     print(f"Number of Players is {numOfPlayers}")
#     print(f"Total age is {totalAge}")
#     print(f"Total goals is {totalGoals}")
#     print(f"Average age is {averageAge}")
    
    lst = [numOfPlayers, totalGoals, totalAge, averageAge]
    return lst
    
 
user_entry = input("Please enter the football season: ")
data_from_function = seasonCalculator(user_entry)

numOfPlayers = data_from_function[0]
totalGoals = data_from_function[1]
totalAge = data_from_function[2]
averageAge = data_from_function[3]

print(f"Number of Players is {numOfPlayers}")
print(f"Total age is {totalAge}")
print(f"Total goals is {totalGoals}")
print(f"Average age is {averageAge}")

