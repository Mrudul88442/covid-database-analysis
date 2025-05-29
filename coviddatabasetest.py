import pandas as pd
import numpy as np
import sqlalchemy
import matplotlib.pyplot as plt 
df = pd.DataFrame()
# Global data frame variable and file path
a=(r"C:\Users\Mrudul\Desktop\covid data csv.csv")
def read_csv_file():
    df=pd.read_csv(a)
    print(df)
a=(r"C:\Users\Mrudul\Desktop\covid data csv.csv")
df =pd.read_csv(a)
print(df)
print(df.index)
def clear():
    for i in range(10):
        print()
def data_analysis_menu():
    df = pd.read_csv(a)
    while True:
        print('\n\nData Analysis MENU ')
        print('_'*100)
        print('1. Show Whole DataFrame\n')
        print('2. Show Columns\n')
        print('3. Show Top Rows\n')
        print('4. Show Bottom Rows\n')
        print('5. Show Specific Column\n')
        print('6. Add a New Record\n')
        print('7. Add a New Column\n')
        print('8. Delete a Column\n')
        print('9. Delete a Record\n')
        print('10. Data Summary\n')
        print('11. Exit (Back to Main Menu)\n')
        ch = int(input('Enter your choice:'))
        if ch == 1:
            print(df)
            wait = input()
        elif ch == 2:
            print(df.columns)
            wait = input()
        elif ch == 3:
            n = int(input('Enter Total rows you want to show :'))
            print(df.head(n))
            wait = input()
        elif ch == 4:
            n = int(input('Enter Total rows you want to show :'))
            print(df.tail(n))
            wait = input()
        elif ch == 5:
            print(df.columns)
            col_name = input('Enter Column Name that You want to print : ')
            print(df[col_name])
            wait = input()
        elif ch==6:
            State=input("enter the name of State/UT")
            Month=input("enter the months")
            ConfirmedCases=input("enter the confirmed cases")
            activeCases=input("enter the number of active cases")
            Cured=input("enter the number of peole get discharge/cured")
            Death=input("enter the number of death cases")
            df.loc[len(df)]=[State,Month,ConfirmedCases,activeCases,Cured, Death]
            print(df)
        elif ch==7:
            col_name = input('Enter new column name :')
            col_value = eval(input('Enter default column value :'))
            df[col_name]=col_value
            print(df)
            print('\n\n Press any key to continue....')
            wait=input()
        elif ch==8:
            print(df.columns)
            col_name =input('Enter column Name to delete :')
            del df[col_name]
            print(df)
            wait=input()
        elif ch==9:
            print("Choose row index that you want to delete")
            index_no =int(input('Enter the Index Number hat You want to delete :'))
            df = df.drop(index_no)
            print(df)
            print('\n\n Press any key to continue....')
            wait=input()
            print(df)
        elif ch==10:
            print(df.describe)
            print("\n\n Press any key to continue....")
            wait=input()
        elif ch==11:
            break
def graph():
    while True:
        print('1. Whole Data LINE Graph\n')
        print('2. Bar Graph Displaying no. of cured and discharge\n')
        print('3. Bar Graph Displaying deaths \n')
        print('4. pie chart displaying affected states \n')
        print('5. exit\n')
        ch = int(input('Enter your choice:' ))
        if ch==1:
            df=pd.read_csv(a)
            x = df['state']
            y = df['Confirmed Cases']
            plt.xticks(rotation='vertical')
            plt.xlabel("state")
            plt.ylabel("ConfirmedCase")
            plt.title('line graph displaying number of confirmed cases state wise ')
            plt.grid(True)
            plt.plot(x,y,linewidth=3)
            plt.show()
        elif ch==2:
            df=pd.read_csv(a)
            x=df['state']
            y=df['Cured/Discharged']
            plt.bar(x,y ,color='g')
            plt.xticks(rotation='vertical')
            plt.grid(True)
            plt.title(" Bar Graph Displaying no of cured and discharge cases state wise")
            plt.xlabel('states')
            plt.ylabel('number of cured cases')
            plt.show()
            wait= input()     
        elif ch==3:
            df=pd.read_csv(a)
            x=df['state']
            y=df['Death']
            plt.bar(x,y,color='g')
            plt.xticks(rotation='vertical')
            plt.grid(True)
            plt.title(" Bar Graph Displaying no of deaths")
            plt.xlabel('states')
            plt.ylabel('number of deaths')
            plt.show()
            wait= input()
        elif ch==4:
            df=pd.read_csv(a)
            col=df['state']
            affected=df['Active Cases']
            plt.pie(affected,labels=col,radius=1.5,autopct='%0.3f%%')
            plt.show()
            wait= input()
        elif ch ==5:
            break
def export_menu():
    while True:
        print()
        print("Export Menu\n\n")
        print("1. Export Data into a CSV File\n")
        print("2. Export Data into a MySQL Table\n")
        print("3.exit\n")
        ch=input("Enter your Choice: ")
        if ch=='1':
            print()
            name_given=input("Enter the name of Your CSV File: ")
            df.to_csv(name_given+".csv")
            print("\nCreating the File...")
            print("\nCheck Your File in the Current Folder!!")
        elif ch=='2':
            print()
            user_name=input("Enter the User Id of MySQL: ")
            passs=input("Enter the Password of MySQL: ")
            db_name=input("Enter the DataBase Name: ")
            file_name=input("Enter the Table Name to be Given: ")
            engine=sqlalchemy.create_engine("mysql+pymysql://"+user_name+":"+passs+"@localhost/"+db_name)
            df.to_sql(name=file_name, con=engine, index=False, if_exists='replace')
            print("Your MySQL table at desired database is being Created...")
            print("\n\n Please Check your Database for the Table!!")
        elif ch=='3':
            break
def main_menu():
    while True:
        clear()
        print("MAIN MENU")
        print('_'*100)
        print('1. Read File')
        print('2. Analysis Menu')
        print('3. Graph Menu')
        print('4. Export Data')
        print('5. Exit')
        choice = int(input('Enter your choice: '))
        if choice == 1:
            read_csv_file()
        elif choice == 2:
            data_analysis_menu()
        elif choice == 3:
            graph()
        elif choice == 4:
            export_menu()
        elif choice == 5:
            print("Exiting the program...")
            break
        input('\nPress Enter to continue...')

# Run the main menu
main_menu()
        
        
 
        
    
