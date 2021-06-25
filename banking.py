import uuid
import csv

class CreatesavingAcc:
    def Persondata(self):
        id=str(uuid.uuid1())
        print(id)

        name = input("enter your name")
        age = int(input("age"))
        if age >= 18:
            agevar = age
        else:
            print("not eligible")

        gender = input("Enter your gender:\n M for male \n F for female ,\n O for n others Genders")

        adharnum = int(input("PUT 12 DIGIT OF YOUR AADHAAR "))
        a_n = str(adharnum)
        print(len(a_n))
        if len(a_n) == 12:
            adhar = adharnum
        else:
            print("Adhaar not valid please check it again")

        pan_card = input("YOUR PANCARD NUMBER")
        pan = len(pan_card)
        if pan == 10:
            pan_cardvar = pan_card
        else:
            print("check your pan card details")
        country = input("YOur Country")
        state = input("Your state")
        district = input("Your District")
        c_v = input("your city or village or town")

        addr = input("colony and house number")
        # param={"id":id,"name":name ,"age":agevar,"gender":gender,"aadhaar":adhar,
        #        "pan_card":pan_cardvar,"country":country,
        #        "state":state,"district":district,"c_v":c_v}
        # print(param)
        param1=[[id,name,agevar,gender,adhar,pan_cardvar,country,state,district,c_v,addr]]
        print(param1[0])

        fields = ['Id','Name', 'age', 'gender', 'aadhaar','Pan card','Country','State','District','City']

        # data rows of csv file


        # name of csv file
        filename = "university_records.csv"

        # writing to csv file
        with open('abhay.csv', 'w') as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile)

            # writing the fields
            csvwriter.writerow(fields)

            # writing the data rows
            csvwriter.writerows(param1[0])



obj1=CreatesavingAcc()
obj1.Persondata()