import sqlite3

# connecting to database file
mycurs = sqlite3.connect('CricketFantasyLeague.db')  
curs = mycurs.cursor()

#CREATING MATCH TABLE
curs.execute('''CREATE TABLE IF NOT EXISTS match
(Player TEXT NOT NULL,Scored INTEGER,Faced INTEGER,Fours INTEGER,Sixes INTEGER,Bowled INTEGER,Maiden INTEGER,Given INTEGER,Wkts INTEGER,Catches INTEGER,Stumping INTEGER,RunOut INTEGER);''')



#CREATING STATS TABLE
curs.execute('''CREATE TABLE IF NOT EXISTS stats (Player PRIMARY KEY,Matches INTEGER,Runs INTEGER,Hundreds INTEGER,Fifties INTEGER,Value INTEGER,Ctg TEXT NOT NULL);''')


#CREATING TEAMS TABLE
curs.execute('''CREATE TABLE IF NOT EXISTS teams (Name TEXT NOT NULL,Players TEXT NOT NULL,Value INTEGER);''')



#DISPLAY DATA IF EXISTS IN DATABASE
sql="select * from match"
curs.execute(sql)
result=curs.fetchall()
if(result):
    for i in result:
        
    
        print(i)
    opt=input("\n Add more players details ? (Y/N) : ")
else:
    print("No any players data found ")

    opt=input("\n Add players data (Y/N) :")
#ADDING DATA FROM USER TO MATCH TABLE
while(opt=='y' or opt=='Y'):
    
    row=[input("Player name :")]
    row.append(int(input("Score:")))
    row.append(int(input("Faced: ")))
    row.append(int(input("Fours: ")))
    row.append(int(input("Sixes: ")))
    row.append(int(input("Bowled: ")))
    row.append(int(input("Maiden: ")))
    row.append(int(input("Given: ")))
    row.append(int(input("Wkts: ")))
    row.append(int(input("Catches: ")))
    row.append(int(input("Stumping: ")))
    row.append(int(input("RunOut: ")))
    
    
    try:
        curs.execute("INSERT INTO match (Player,Scored, Faced, Fours,Sixes,Bowled,Maiden,Given,Wkts,Catches,Stumping,RunOut) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", #adding data to database
                          (row[0],row[1], row[2], row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]))
        mycurs.commit()

        print("Records added successfully match table.")
    except:    # except block to handle exceptions
        print("Error in operation.")
        mycurs.rollback()
   

        
   #ADDING DATA TO STATS TABLE FROM USER 
    print("player information for State table ")
    row.append(int(input("Total matches: ")))
    row.append(int(input("Total runs: ")))
    row.append(int(input("100s: ")))
    row.append(int(input("50s: ")))
    row.append(int(input("Value: ")))
    row.append(input("Category as (BAT,BWL,AR,WK): "))
    
    try:       #try block to catch exceptions
    
        curs.execute("INSERT INTO stats (Player,Matches,Runs, Hundreds, Fifties,Value,Ctg) VALUES (?,?,?,?,?,?,?)", #adding data to database
                          (row[0],row[12], row[13], row[14],row[15],row[16],row[17]))
        mycurs.commit()

        print("Records added successfully for stats table.")
    except:    # except block to handle exceptions
        print("Error in operation.")
        mycurs.rollback()
        
    opt=input("Adding more player ? (Y/N) : ")

   
        
        

        
print("Bye!!!")   
curs.close()

#closing database

    
    
    
    
    
    

    
    

    
    
    
    
    
 
                          
        

        
     
        
        
    
    
    
        

    
    
    
    
    

    
    
         
    
    
                          
        

    
    
        
        
        
    
    
        

    

