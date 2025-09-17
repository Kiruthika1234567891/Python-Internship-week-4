#______---------------NumPy & Panda / INTRO TO DATA HANDLING-----------------_______________

# _____CREATE NumPy ARRAY OF NUMBERS FROM 1 to 10 & PRINT theirs SQUARES______
# import numpy as np
# arr = np.arange(1,11)
# print("Numbers:",arr)
# print("Squares:",arr**2)

# ___________CREATE A 2D NumPy ARRAY(3*3) & PRINT SUM OF ROWS&COLUMN______
# import numpy as np
# arr = np.array([[1,2,3],
#                 [4,5,6],
#                 [7,8,9]])
# print("Array:\n",arr)
# row_sum = np.sum(arr,axis=1)
# column_sum = np.sum(arr,axis=0)
# print("Sum of each rows:",row_sum)
# print("Sum of each column:",column_sum)

# ___________CREATE Pandas DATAFRAME FOR STUDENTS NAME & MARKS______
# import pandas as pd
# data = {
#     'Name':['Charlie','Jolly','Bob','Jhonny'],
#     'Marks':[94,86,72,66]
# } 
# df = pd.DataFrame(data)
# print("Student's Dataframe:\n",df)

# ___________READ A CSV FILE USING Pandas & PRINT FIRST & LAST 5 ROWS_________
# ✅ Step 1: Create and save a CSV file
# import pandas as pd
# data = {
#     'Name':['Ram','Paari','Gautham','Aadi','Sachin','Arjune'],
#     'Age':[19,22,25,21,26,23]
# }
# df = pd.DataFrame(data)
# df.to_csv("Characters.csv",index=False)
# print("CSV file 'Characters.CSV' file created successfully.")
# ✅ Step 2: Read the CSV file and print first & last 5 rows
# df_read = pd.read_csv("Characters.csv")
# print("First 5 rows of CSV file:\n",df_read.head())
# print("Last 5 rows of CSV file:\n",df_read.tail())

# _________FIND THE AVERAGE MARKS OF STUDENTS USING PANDAS_______
# import pandas as pd
# data = {
#     'Name':['Charlie','Jolly','Bob','Jhonny'],
#     'Marks':[94,86,72,66]
# }
# df = pd.DataFrame(data)
# average_marks = df['Marks'].mean()
# print("Average marks of students:",average_marks)







