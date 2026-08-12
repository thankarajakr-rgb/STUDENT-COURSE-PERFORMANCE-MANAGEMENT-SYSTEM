from datetime import datetime

profile=[]



while True:
  try:

    name=input("Enter the Student Name")
    age=int(input("Enter the age"))
    dob=input("Enter date of birth")


    datetime.strptime(dob, "%d-%m-%Y")

    students={
        "Name":name,
        "Age":age,
        "DOB":dob
     }

    profile.append(students)

  except ValueError:
    print("Invalid DOB or Age")
    continue

  choice=input("Do you wannt to add Students (yes/no)")

  if choice.lower()=="no":
    break

print(profile)  


for i in profile:
  print("Name :",i['Name'])
  print("Age :",i['Age'])
  print("DOb:",i['DOB'])

  if i['Age']<18:
    file=open("new.txt",'a')
    file.write(f"Not Eligible to vote\n"
               f"Name:{i['Name']}\n"
               f"Age:{i['Age']}\n"
               f"Name:{i['DOB']}"

    )
    file.close()
    
    

  else:
    file=open("new1.txt",'a')
    file.write(f"Not Eligible to vote\n"
               f"Name:{i['Name']}\n"
               f"Age:{i['Age']}\n"
               f"Name:{i['DOB']}"

    )
    file.close()
    






 
   
















