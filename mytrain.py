import requests
class Train:
    def __init__(self):
        user_input=int(input("""
            -> Press 1 To Check Live Train Status
            -> Press 2 To Check PNR
            -> Press 3 To Check Train Schedule 
            -> Press Anykey For Exit.
                          
        """))
        if user_input==1:
            print("Live Status")
        elif user_input==2:
            print("PNR Inquiry")
        elif user_input==3:
            self.train_schedule()
        else:
            return None
        
    def train_schedule(self):
        train_no=int(input("Enter The Train No"))
        self.fetch_data(train_no)
    
    def fetch_data(self,train_no):
        data=requests.get("https://indianrailapi.com/api/v2/TrainSchedule/apikey/4fb7dc5d1ccaf37bbf9b4d62d8d55e89/TrainNumber/{}".format(train_no))

        data=data.json()

        # print(data["Route"])

        count=1
        for i in data["Route"]:
            print(count,i["StationName"].center(15,"_"),"|","Arrival_Time",i["ArrivalTime"].center(15,"_"),"|","Departure_Time",i["DepartureTime"].center(15,"_"))
            count+=1

obj=Train()
