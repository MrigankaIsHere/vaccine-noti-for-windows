#This useless piece of code is written by Mriganka Shekhar Chakravarty. Please swear me at https://www.linkedin.com/in/mriganka82624/
# Jai Hind <3
import requests, datetime, json, time, smtplib, os, sys, base64, re
from cryptography.fernet import Fernet
from getmac import get_mac_address as gma
workdir = ""
twofaauth= ""
email =""
target=""
rng = ""
state_id=""
age = ""
states = [{"state_id":1,"state_name":"Andaman and Nicobar Islands"},{"state_id":2,"state_name":"Andhra Pradesh"},{"state_id":3,"state_name":"Arunachal Pradesh"},{"state_id":4,"state_name":"Assam"},{"state_id":5,"state_name":"Bihar"},{"state_id":6,"state_name":"Chandigarh"},{"state_id":7,"state_name":"Chhattisgarh"},{"state_id":8,"state_name":"Dadra and Nagar Haveli"},{"state_id":37,"state_name":"Daman and Diu"},{"state_id":9,"state_name":"Delhi"},{"state_id":10,"state_name":"Goa"},{"state_id":11,"state_name":"Gujarat"},{"state_id":12,"state_name":"Haryana"},{"state_id":13,"state_name":"Himachal Pradesh"},{"state_id":14,"state_name":"Jammu and Kashmir"},{"state_id":15,"state_name":"Jharkhand"},{"state_id":16,"state_name":"Karnataka"},{"state_id":17,"state_name":"Kerala"},{"state_id":18,"state_name":"Ladakh"},{"state_id":19,"state_name":"Lakshadweep"},{"state_id":20,"state_name":"Madhya Pradesh"},{"state_id":21,"state_name":"Maharashtra"},{"state_id":22,"state_name":"Manipur"},{"state_id":23,"state_name":"Meghalaya"},{"state_id":24,"state_name":"Mizoram"},{"state_id":25,"state_name":"Nagaland"},{"state_id":26,"state_name":"Odisha"},{"state_id":27,"state_name":"Puducherry"},{"state_id":28,"state_name":"Punjab"},{"state_id":29,"state_name":"Rajasthan"},{"state_id":30,"state_name":"Sikkim"},{"state_id":31,"state_name":"Tamil Nadu"},{"state_id":32,"state_name":"Telangana"},{"state_id":33,"state_name":"Tripura"},{"state_id":34,"state_name":"Uttar Pradesh"},{"state_id":35,"state_name":"Uttarakhand"},{"state_id":36,"state_name":"West Bengal"}]

def check_invalid(email):
    regex = '^[a-z0-9]+[\._]?[ a-z0-9]+[@]\w+[. ]\w{2,3}$'
    if(re.search(regex,email)):
        return False
    else:
        return True

headers = headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

if len(sys.argv)>0:
    if sys.argv[1]=='1':
        workdir = sys.argv[2]
        content = "CreateObject(\"Wscript.Shell\").Run \"" + os.getcwd()+"\\proxycall.bat\", 0, True"
        f = open("invis.vbs","w")
        f.write(content)
        f.close()
        f = open("proxycall.bat","w")
        f.write("set V="+workdir+"\npython "+os.getcwd()+"\\main.py %V%")
        f.close()
        os.system("REG ADD HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run /v runner /t REG_SZ /d "+workdir+"\\invis.vbs")
        for i in range(len(states)):
            print(str(states[i]["state_id"]) + " : " + states[i]["state_name"])

        state_id = None
        while True:
            try:
                state_id = int(input())
                ok = False
                for i in states:
                    if i.get("state_id")==state_id:
                        ok = True
                if ok:
                    break
                else:
                    print("please enter a valid state id...\n")
            except:
                print("Please enter a number for god's sake!")
        response = requests.get("https://cdn-api.co-vin.in/api/v2/admin/location/districts/"+str(state_id), headers= headers)
        json_data = json.loads(response.text)
        data = json_data["districts"]
        for i in range(len(data)):
            print(str(data[i]["district_id"]) + " : " + data[i]["district_name"])

        target = None
        while True:
            try:
                target = int(input())
                ok = False
                for i in data:
                    if i.get("district_id")==target:
                        ok = True
                if ok:
                    break
                else:
                    print("please enter a district id...\n")
            except:
                print("Please enter a number for god's sake!")


        rng=None
        age = None
        while True:
            try:
                rng = int(input("Enter the number days into the future, to search for vaccines, starting today."))
                if rng<30:
                    break
                else:
                    print("Needs to be less than 30, for DoS prot.")
            except:
                print("enter a number for god's sake")
        while True:
            try:
                age = int(input("Enter age:"))
                if age>44:
                    age = 45
                elif age >17:
                    age = 18
                else:
                    print("vaccination not yet started yet for this age")
                    exit(0)
                break
            except:
                print("enter a number for god's sake")
        email = ""
        while check_invalid(email):
            email = input("Please enter your email id\n")
        print("1) Please enable 2-Factor authentication at https://myaccount.google.com/security\n2) Then generate an application password at (https://myaccount.google.com/apppasswords)")
        twofaauth = input("Enter password...")
        tfa = twofaauth
        key = gma()
        key = key*(32//len(key)) + key[:32%len(key)]
        key = base64.urlsafe_b64encode(key.encode())
        f = Fernet(key)
        enc = f.encrypt(tfa.encode())
        enc = enc.decode()
        f = open("user_details.txt","w")
        f.write(email+"\n")
        f.write(enc+"\n")
        f.write(str(age)+"\n")
        f.write(str(rng)+ "\n")
        f.write(str(target)+"\n")
        f.close()
        input("Your PC will restart now. Please save any unsaved work and then press any key. To stop receiving notifications, please run the STOPNOTIF.bat file.")
        os.system("shutdown -r -t 0")
    else:
        workdir = sys.argv[1]
        f = open(workdir+"\\user_details.txt")
        readdata= f.readlines()
        email =  readdata[0][:-1]
        twofaauth = readdata[1][:-1]
        twofaauth = twofaauth.encode()
        key = gma()
        key = key*(32//len(key)) + key[:32%len(key)]
        key = base64.urlsafe_b64encode(key.encode())
        f = Fernet(key)
        twofaauth = f.decrypt(twofaauth).decode()
        age = int(readdata[2][:-1])
        rng = int(readdata[3][:-1])
        target = int(readdata[4][:-1])




date_list = [datetime.datetime.today() + datetime.timedelta(days=x) for x in range(rng)]
date_str = [x.strftime("%d-%m-%Y") for x in date_list]
cnt=0
while True:
    try:
        # cnt+=1
        s = ""
        for INP_DATE in date_str:
            URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={}&date={}".format(target, INP_DATE)
            response = requests.get(URL, headers= headers)
            
            if response.ok:
                resp_json = response.json()
                
                if resp_json["centers"]:
                    for center in resp_json["centers"]:
                        for session in center["sessions"]:
                            if session["min_age_limit"] <= age and session["available_capacity"]>0:
                                s += "\t " + center["name"]
                                s +="\t " + center["block_name"]
                                s +="\t Price: " + center["fee_type"]
                                s +="\t Available Capacity: " + str(session["available_capacity"])
                                if(session["vaccine"] != ''):
                                    s+="\t Vaccine: " + session["vaccine"]
                                s += "\t" + session["date"] + "\n\n"

                               
        if s!="":
            # print(s) 
            with smtplib.SMTP('smtp.gmail.com',587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()
                smtp.login(email, twofaauth)
                smtp.sendmail(email, email, 'Subject: Vaccine Notification\n\n'+s)
        time.sleep(1800)
        # print(cnt)
    except:
        pass