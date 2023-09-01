import mysql.connector as con

mycon = con.connect(host='localhost', user='root', passwd='Aravindhan@2006', database='fsa')
cur = mycon.cursor()

cur.execute("select * from logindetails")
data = cur.fetchall()
lst_uname = []
lst_passwd = []
for i in data:
    lst_uname.append(i[0])
    lst_passwd.append(i[1])


def welcome():
    print("_" * 128)
    print('                Welcome To The FSA FITness Center!!!')


welcome()


# ---------------------------------------------------Login / Sign in ---------------------------------------------------

def Register():
    f = 1
    while f == 1:
        global username
        username = input("\n>>> Enter Your Username: ")
        if username in lst_uname:
            print("\nUsername Already Exists")
            print("\nTry Again!")
            f = 1

        else:
            x1 = "insert into logindetails(username) values(%s)"
            y1 = (username,)
            cur.execute(x1, y1)
            mycon.commit()
            cur.execute("insert into menu(user_name) values(%s)", (username,))
            mycon.commit()
            cur.execute("insert into subs(user_name) values(%s)", (username,))
            mycon.commit()
            cur.execute("insert into pack(user_name) values(%s)", (username,))
            mycon.commit()
            f += 1

    g = 1

    while g == 1:
        gender = input("\n>>> Enter 'M' For Male 'F' For Female: ")
        if gender.lower() == "m" or gender.lower() == "f":
            cur.execute("update logindetails set Gender=%s where Username=%s", (gender, username))
            mycon.commit()
            g += 1
        else:
            print("\nInvalid Input. Try Again!")
            g = 1

    h = 1
    while h == 1:
        age = input("\n>>> Enter Your Age: ")
        if age.isdigit():
            age = int(age)
            if age >= 13 and age <= 80:
                cur.execute("update logindetails set Age=%s where Username=%s", (age, username))
                mycon.commit()
                h += 1
            else:
                print("\nThe Age Limit Is Not Satisfied! ")
                h = 1
        else:
            print("\nInvalid Input. Try Again")
            h = 1

    i = 1
    while i == 1:
        mob_num = int(input("\n>>> Enter Your Mobile Number: "))
        if len(str(mob_num)) == 10 and str(mob_num).isdigit():
            cur.execute("update logindetails set Mobile_Number =%s where Username=%s", (mob_num, username))
            mycon.commit()
            i += 1
        else:
            print("\nThe Mobile Number Is Incorrect. Try Again!")
            i = 1

    address = input("\n>>> Enter Your Address: ")
    cur.execute("update logindetails set Address=%s where Username=%s", (address, username))
    mycon.commit()

    j = 1
    while j == 1:
        password = input("\n>>> Enter Your Password [Password Must Contain 6 Characters] : ")
        confirm_password = input("\n>>> Re-Enter The Password: ")
        if password == confirm_password and len(confirm_password) == 6:
            print("\n                   You Are Registered")
            cur.execute("update logindetails set Password=%s where Username=%s", (password, username))
            mycon.commit()
            j += 1
        else:
            print("\nIncorrect Password. Try Again")
            j = 1


def Authorisation():
    k = 1
    while k == 1:
        print("""
+ - - - - - - - - - - - - - - - - - - - - - - - +         
|                   1 -- 'Login'                |
| - - - - - - - - - - - - - - - - - - - - - - - | 
|                   2 -- 'Sign-Up               |
+ - - - - - - - - - - - - - - - - - - - - - - - +
              """)
        choice_1 = input("FSA> ")

        if choice_1 == "2":
            Register()

        elif choice_1 == "1":
            e = 1
            while e == 1:
                global username
                username = input("\n>>> Enter Your Username: ")
                password = input("\n>>> Enter Your Password: ")
                cur.execute("select * from logindetails")
                data = cur.fetchall()
                lst_uname = []
                lst_passwd = []
                for i in data:
                    lst_uname.append(i[0])
                    lst_passwd.append(i[1])

                if username in lst_uname:
                    if password == lst_passwd[lst_uname.index(username)]:
                        print("\n             You're Logged In")
                        e += 1
                        k += 1
                        break
                    else:
                        print("\nInvalid Password. Try Again!")
                        e = 1

                else:
                    print("\nNo Account Found. Sign-Up To Continue")
                    ba = 1
                    while ba == 1:
                        ch_1 = input("\nType '1' To Sign-Up: ")
                        if ch_1 == "1":
                            Register()
                            e += 1
                            ba += 1


                        else:
                            print("\nInvalid Input. Try Again")
                            ba = 1





        else:
            print("\nInvalid Input. Try Again")
            k = 1


Authorisation()


# ---------------------------------------------------Login / Sign in: over ---------------------------------------------------

def fitness_menu():
    a = 1
    while a == 1:
        print(" ")
        print(" ")
        print("\n1.     Profile")
        print("\n2.     Menu")
        print("\n3.     About Us")
        print("\n4.     Exit")

        choice_2 = input("\n>>> ")

        if choice_2 == "1":
            print("_" * 128)
            print("\n                             PROFILE DETAILS            ")

            print("\nName: ", username)
            cur.execute("Select * from logindetails where Username=%s", (username,))
            data = cur.fetchall()
            print("\nAge: ", data[0][3])
            print("\nGender: ", data[0][2])
            print("\nMobile Number: ", data[0][4])
            print("\nAddress: ", data[0][5])
            cur.execute("select * from subs where User_name=%s", (username,))
            data = cur.fetchall()
            if data[0][1] == None:
                print("\nSubscription: None Active ")
            else:
                cur.execute("select EndDate from subs where User_name=%s", (username,))
                data_1 = cur.fetchall()
                print("\nSubscription: ", data[0][1], "Month(s) Membership - Active Till: ", data_1[0][0])

            cur.execute("select * from Pack where User_name=%s", (username,))
            data = cur.fetchall()
            if data[0][1] == None and data[0][2] == None and data[0][3] == None:
                print("\nPackages: None Active")
            else:
                print("\nPackages: ")
                if data[0][1] == None:
                    print("\n Bronze Package - Not Active")
                else:
                    cur.execute("select EndDateBronze from pack where user_name=%s", (username,))
                    data_2 = cur.fetchall()
                    print("\n Bronze Package - Active Till: ", data_2[0][0])

                if data[0][2] == None:
                    print("\n Silver Package - Not Active")
                else:
                    cur.execute("select EndDateSilver from pack where user_name=%s", (username,))
                    data_2 = cur.fetchall()
                    print("\n Silver Package - Active Till: ", data_2[0][0])

                if data[0][3] == None:
                    print("\n Gold Package - Not Active")
                else:
                    cur.execute("select EndDateGold from pack where user_name=%s", (username,))
                    data_2 = cur.fetchall()
                    print("\n Gold Package - Active Till: ", data_2[0][0])

            s = 1
            while s == 1:
                print("\nEnter 'E' To Edit Your Profile: ")
                print("\nEnter 'B' To Go Back")
                choice_3 = input("\n>>> ")
                if choice_3.lower() == 'e':
                    print("  ")
                    print("_" * 128)
                    print("\nYou Have Chosen To Edit Your Profile")
                    l = 1
                    while l == 1:
                        password = input("\n>>> Enter Your Password: ")
                        cur.execute("select * from logindetails")
                        data = cur.fetchall()
                        lst_uname = []
                        lst_passwd = []
                        for i in data:
                            lst_uname.append(i[0])
                            lst_passwd.append(i[1])
                        if password == lst_passwd[lst_uname.index(username)]:
                            print("\nVerification Successful")
                            l += 1
                        else:
                            print("\nInvalid Password")
                            print("     Try Again!")
                            l = 1
                    print("\nNote: Username Cannot Be Changed ")
                    c = 1
                    while c == 1:
                        print("\n1. Age")
                        print("\n2. Mobile Number")
                        print("\n3. Address")
                        print("\nEnter 'B' To Go Back")
                        choice_4 = input("\n>>> ")

                        if choice_4 == '1':
                            ab = 1
                            while ab == 1:
                                choice_5_1 = input("\n>>> Enter Age To Be Changed: ")
                                if choice_5_1.isdigit() and int(choice_5_1) >= 13 and int(choice_5_1) <= 80:
                                    choice_5 = int(choice_5_1)
                                    cur.execute("update logindetails set Age=%s where username=%s",
                                                (choice_5, username))
                                    mycon.commit()
                                    print("\nProfile Updated")
                                    d = 1
                                    while d == 1:
                                        choice_6 = input("\n>>> Enter 'B' To Go Back: ")
                                        if choice_6.lower() == 'b':
                                            print("\nYou Have Chosen To Go Back")
                                            c = 1
                                            d += 1
                                            ab += 1
                                        else:
                                            print("\nInvalid Input. Try Again!")
                                            d = 1
                                else:
                                    print("\nInvalid Input. Try Again!")
                                    ab = 1

                        elif choice_4 == '2':
                            y = 1
                            while y == 1:
                                choice_5 = int(input("\n>>> Enter Mobile Number To Be Changed: "))
                                if len(str(choice_5)) == 10:
                                    cur.execute("update logindetails set Mobile_Number=%s where username=%s",
                                                (choice_5, username))
                                    mycon.commit()
                                    print("\nProfile Updated")
                                    d = 1
                                    while d == 1:
                                        choice_6 = input("\n>>> Enter 'B' To Go Back: ")
                                        if choice_6.lower() == 'b':
                                            print("\nYou Have Chosen To Go Back")
                                            c = 1
                                            d += 1
                                            y += 1
                                        else:
                                            print("\nInvalid Input. Try Again!")
                                            d = 1
                                else:
                                    print("\nInvalid Input. Try Again!")
                                    y = 1


                        elif choice_4 == '3':
                            choice_5 = input("\n>>> Enter Address To Be Changed: ")
                            cur.execute("update logindetails set Address=%s where username=%s", (choice_5, username))
                            mycon.commit()
                            print("\nProfile Updated")
                            d = 1
                            while d == 1:
                                choice_6 = input("\n>>> Enter 'B' To Go Back: ")
                                if choice_6.lower() == 'b':
                                    print("\nYou Have Chosen To Go Back")
                                    c = 1
                                    d += 1
                                else:
                                    print("\nInvalid Input. Try Again!")
                                    d = 1
                        elif choice_4 == 'b' or choice_4 == 'B':
                            print("\nYou Have Chosen To Go Back")
                            c += 1
                            s += 1
                            a = 1

                        else:
                            print("\nInvalid Input. Try Again!.")
                            c = 1


                elif choice_3.lower() == 'b':
                    print("\nYou Have Chosen To Go Back")
                    a = 1
                    s += 1

                else:
                    print("\nInvalid Input. Try Again!")
                    s = 1


        elif choice_2 == "2":
            m = 1
            while m == 1:
                print("   ")
                print("_" * 128)
                print(
                    "\n                                           MENU                                                           ")
                print("\n Kindly Enter Your Choice From The Options Below - ")
                print("\nSubscriptions -- 1")
                print("\nSupplements -- 2")
                print("\nPackages -- 3")
                print("\nBack -- 4")

                choice_menu = input("\n>>> ")

                if choice_menu == "1":
                    print("""
Subscriptions Available:

{1} 1 Month Membership
        -- Access To Trainer
        -- Weekdays / Weekends
        -- Rs. 1,999

{2} 3 Month Membership
        -- Access To Branches All Over Tamil Nadu
        -- Access To Trainer
        -- Meal Plan Provided
        -- Weekdays / Weekends
        -- Rs. 4,999

{3} 6 Month Membership
        -- Access To Branches All Over Tamil Nadu
        -- Access To Trainer
        -- Meal Plan Provided
        -- Access To All Equipment
        -- Weekdays / Weekends
        -- Rs. 10,999

{4} 12 Month Membership
        -- Access To Branches All Over Tamil Nadu
        -- Access To Trainer
        -- Meal Plan Provided
        -- Access To All Equipment
        -- Weekdays And Weekends
        -- Rs. 22,999

{5} 18 Month Membership
        -- Access To Branches All Over Tamil Nadu
        -- Access To Trainer
        -- Meal Plan Provided
        -- Access To All Equipment
        -- Weekdays And Weekends
        -- Rs. 33,999

{6} 24 Month Membership
        -- Access To Branches All Over Tamil Nadu
        -- Access To Trainer
        -- Meal Plan Provided
        -- Access To All Equipment
        -- Weekdays And Weekends
        -- Rs. 42,999


""")

                    r = 1
                    while r == 1:
                        choice_9 = input("\n>>> Enter The Subscription Pack Needed [ Or Enter 'B' To Go Back ] : ")
                        if (
                                choice_9 == '1' or choice_9 == '2' or choice_9 == '3' or choice_9 == '4' or choice_9 == '5' or choice_9 == '6') and choice_9.isdigit():
                            ac = 1
                            while ac == 1:
                                print("\nChoose Your Mode Of Payment: ")
                                print("\n1 -- Debit Card")
                                print("\n2 -- Credit Card")
                                choice_13 = input("\n>>> ")
                                if choice_13 == '1' or choice_13 == '2':
                                    ad = 1
                                    while ad == 1:
                                        choice_14 = input("\n>>> Enter Your Card Number: ")
                                        choice_15 = input("\n>>> Enter Your Pin: ")
                                        if len(choice_14) == 16 and len(choice_15) == 4:
                                            ac += 1
                                            ad += 1
                                        else:
                                            print("\nInvalid Card Number Or Pin. Try Again!")
                                            ad = 1
                                else:
                                    print("\nInvalid Input. Try Again!")
                                    ac = 1

                            p = 1
                            while p == 1:
                                print("\nEnter 'Y' To Confirm Payment: ")
                                print("\nEnter 'N' To Deny Payment: ")
                                choice_10 = input("\n>>> ")
                                if choice_10.lower() == 'y':
                                    if choice_9 == '1':
                                        cur.execute("Select sub_val from subs where user_name=%s", (username,))
                                        data1 = cur.fetchall()
                                        if data1[0][0] == None:
                                            cur.execute("update subs set sub_val=1 where user_name=%s", (username,))
                                            mycon.commit()
                                            cur.execute("update subs set paid=1999 where user_name=%s", (username,))
                                            mycon.commit()
                                            print("\nPayment Successful")
                                            cur.execute("update subs set EndDate=curdate() where user_name=%s",
                                                        (username,))
                                            mycon.commit()
                                            cur.execute(
                                                "update subs set EndDate=date_add(EndDate, interval 1 month) where user_name=%s",
                                                (username,))
                                            mycon.commit()
                                        else:
                                            print("\nSubscription Already Exists")
                                            print("     Payment Cancelled")

                                        d = 1
                                        while d == 1:
                                            choice_6 = input("\n>>> Enter 'B' To Go Back: ")
                                            if choice_6.lower() == 'b':
                                                print("\nYou Have Chosen To Go Back")
                                                m = 1
                                                d += 1
                                                p += 1
                                                r += 1
                                            else:
                                                print("\nInvalid Input. Try Again!")
                                                d = 1

                                    elif choice_9 == '2':

                                        cur.execute("Select sub_val from subs where user_name=%s", (username,))
                                        data1 = cur.fetchall()
                                        if data1[0][0] == None:
                                            cur.execute("update subs set sub_val=3 where user_name=%s", (username,))
                                            mycon.commit()
                                            cur.execute("update subs set paid=4999 where user_name=%s", (username,))
                                            mycon.commit()
                                            print("\nPayment Successful")
                                            cur.execute("update subs set EndDate=curdate() where user_name=%s",
                                                        (username,))
                                            mycon.commit()
                                            cur.execute(
                                                "update subs set EndDate=date_add(EndDate, interval 3 month) where user_name=%s",
                                                (username,))
                                            mycon.commit()
                                        else:
                                            print("\nSubscription Already Exists")
                                            print("     Payment Cancelled")

                                        d = 1
                                        while d == 1:
                                            choice_6 = input("\n>>> Enter 'B' To Go Back: ")
                                            if choice_6.lower() == 'b':
                                                print("\nYou Have Chosen To Go Back")
                                                m = 1
                                                d += 1
                                                p += 1
                                                r += 1
                                            else:
                                                print("\nInvalid Input. Try Again!")
                                                d = 1

                                    elif choice_9 == '3':
                                        cur.execute("Select sub_val from subs where user_name=%s", (username,))
                                        data1 = cur.fetchall()
                                        cur.execute("Select sub_val from subs where user_name=%s", (username,))
                                        data1 = cur.fetchall()
                                        if data1[0][0] == None:
                                            cur.execute("update subs set sub_val=6 where user_name=%s", (username,))
                                            mycon.commit()
                                            cur.execute("update subs set paid=10999 where user_name=%s", (username,))
                                            mycon.commit()
                                            print("\nPayment Successful")
                                            cur.execute("update subs set EndDate=curdate() where user_name=%s",
                                                        (username,))
                                            mycon.commit()
                                            cur.execute(
                                                "update subs set EndDate=date_add(EndDate, interval 6 month) where user_name=%s",
                                                (username,))
                                            mycon.commit()
                                        else:
                                            print("\nSubscription Already Exists")
                                            print("     Payment Cancelled")

                                        d = 1
                                        while d == 1:
                                            choice_6 = input("\n>>> Enter 'B' To Go Back: ")
                                            if choice_6.lower() == 'b':
                                                print("\nYou Have Chosen To Go Back")
                                                m = 1
                                                d += 1
                                                p += 1
                                                r += 1
                                            else:
                                                print("\nInvalid Input. Try Again!")
                                                d = 1

                                    elif choice_9 == '4':
                                        cur.execute("Select sub_val from subs where user_name=%s", (username,))
                                        data1 = cur.fetchall()
                                        if data1[0][0] == None:
                                            cur.execute("update subs set sub_val=12 where user_name=%s", (username,))
                                            mycon.commit()
                                            cur.execute("update subs set paid=22999 where user_name=%s", (username,))
                                            mycon.commit()
                                            print("\nPayment Successful")
                                            cur.execute("update subs set EndDate=curdate() where user_name=%s",
                                                        (username,))
                                            mycon.commit()
                                            cur.execute(
                                                "update subs set EndDate=date_add(EndDate, interval 12 month) where user_name=%s",
                                                (username,))
                                            mycon.commit()
                                        else:
                                            print("\nSubscription Already Exists")
                                            print("     Payment Cancelled")

                                        d = 1
                                        while d == 1:
                                            choice_6 = input("\n>>> Enter 'B' To Go Back: ")
                                            if choice_6.lower() == 'b':
                                                print("\nYou Have Chosen To Go Back")
                                                m = 1
                                                d += 1
                                                p += 1
                                                r += 1
                                            else:
                                                print("\nInvalid Input. Try Again!")
                                                d = 1

                                    elif choice_9 == '5':
                                        cur.execute("Select sub_val from subs where user_name=%s", (username,))
                                        data1 = cur.fetchall()
                                        if data1[0][0] == None:
                                            cur.execute("update subs set sub_val=18 where user_name=%s", (username,))
                                            mycon.commit()
                                            cur.execute("update subs set paid=33999 where user_name=%s", (username,))
                                            mycon.commit()
                                            print("\nPayment Successful")
                                            cur.execute("update subs set EndDate=curdate() where user_name=%s",
                                                        (username,))
                                            mycon.commit()
                                            cur.execute(
                                                "update subs set EndDate=date_add(EndDate, interval 18 month) where user_name=%s",
                                                (username,))
                                            mycon.commit()
                                        else:
                                            print("\nSubscription Already Exists")
                                            print("     Payment Cancelled")

                                        d = 1
                                        while d == 1:
                                            choice_6 = input("\n>>> Enter 'B' To Go Back: ")
                                            if choice_6.lower() == 'b':
                                                print("\nYou Have Chosen To Go Back")
                                                m = 1
                                                d += 1
                                                p += 1
                                                r += 1
                                            else:
                                                print("\nInvalid Input. Try Again!")
                                                d = 1

                                    elif choice_9 == '6':
                                        cur.execute("Select sub_val from subs where user_name=%s", (username,))
                                        data1 = cur.fetchall()
                                        if data1[0][0] == None:
                                            cur.execute("update subs set sub_val=24 where user_name=%s", (username,))
                                            mycon.commit()
                                            cur.execute("update subs set paid=42999 where user_name=%s", (username,))
                                            mycon.commit()
                                            print("\nPayment Successful")
                                            cur.execute("update subs set EndDate=curdate() where user_name=%s",
                                                        (username,))
                                            mycon.commit()
                                            cur.execute(
                                                "update subs set EndDate=date_add(EndDate, interval 24 month) where user_name=%s",
                                                (username,))
                                            mycon.commit()
                                        else:
                                            print("\nSubscription Already Exists")
                                            print("     Payment Cancelled")

                                        d = 1
                                        while d == 1:
                                            choice_6 = input("\n>>> Enter 'B' To Go Back: ")
                                            if choice_6.lower() == 'b':
                                                print("\nYou Have Chosen To Go Back")
                                                m = 1
                                                d += 1
                                                p += 1
                                                r += 1
                                            else:
                                                print("\nInvalid Input. Try Again!")
                                                d = 1
                                    else:
                                        print("\nInvalid Input. Try Again!")
                                        p += 1
                                        r = 1

                                elif choice_10.lower() == 'n':
                                    print("\nPayment Cancelled")
                                    d = 1
                                    while d == 1:
                                        choice_6 = input("\n>>> Enter 'B' To Go Back: ")
                                        if choice_6.lower() == 'b':
                                            print("\nYou Have Chosen To Go Back")
                                            m = 1
                                            d += 1
                                            p += 1
                                            r += 1
                                        else:
                                            print("\nInvalid Input. Try Again!")
                                            d = 1


                                else:
                                    print("\nInvalid Input. Try Again!")
                                    p = 1

                        elif choice_9.lower() == 'b':
                            print("\nYou Have Chosen To Go Back")
                            r += 1
                            m = 1

                        else:
                            print("\nInvalid Input. Try Again!")
                            r = 1



                elif choice_menu == "2":
                    print("  ")
                    print("_" * 128)
                    print(
                        "\n                                         SUPPLEMENTS                                                      ")
                    print('''
1 - Pre-Workout
        Company Name: X-CITE
        Details:
        - “NO CRASH” ENERGY
        - 10 CALORIES PER SERVING
        - TRAIN HARDER FOR BETTER GAINS
        - NO JITTERS. NO UPSET STOMACH
        - Price: Rs.379        

2 - PR-X Max Strength/Energy
        Company Name: PR-X
        Details:
        - Kre-Alkalyn® Creatine 3g
        - D-Ribose 8g
        - NADH 15mg
        - CoQ10 100mg
        - Citrulline Malate 4g
        - 40 Calories
        - 8g Sugars (as D-Ribose)
        - 0mg Caffeine
        - Price: Rs.499


3 - Premium Protein Powder
        Company Name: PRO-30G
        Details:
        - BUILDS LEAN MUSCLE MASS
        - 30G HIGH QUALITY PROTEIN
        - GREAT, SMOOTH TASTE
        - 28 SERVINGS
        - Price: Rs.549


4 - Muscle Recovery
        Company Name: RECONSTRUXION
        Details:
        - SPEEDS UP MUSCLE RECOVERY
        - INCREASES QUALITY SLEEP
        - PROMOTES LEAN MUSCLE MASS
        - ELIMINATES MUSCLE SORENESS
        - Price: Rs.529


5 - Women's All In One Protein
        Company Name: 4 WOMEN
        Details:
        - BUILDS LEAN MUSCLE MASS
        - EASILY DIGESTED, NO BLOATING
        - 20G HIGH QUALITY PROTEIN
        - GREAT, SMOOTH TASTE
        - Price: Rs.459


6 - Omega-3 Fish Oil
        Company Name: DOCTOR C'S
        Details:
        - AIDS IN WEIGHT LOSS
        - BOOSTS MOOD NATURALLY
        - PROMOTES HEALTHY SKIN & HAIR
        - COMBATS INFLAMMATION
        - Price: Rs.499


7 - Joint Recovery
        Company Name: MECHAN-X
        Details:
        - RESTORES JOINT HEALTH
        - REDUCES JOINT PAIN
        - AIDS IN CARTILAGE REPAIR
        - COMBATS INFLAMMATION
        - Price: Rs.499


8 - BCAA's
        Company Name: AALPHA
        Details:
        - ACCELERATES MUSCLE GROWTH
        - DECREASES MUSCLE SORENESS
        - DECREASES WORKOUT FATIGUE
        - PROTECTS LEAN MUSCLE MASS
        - Price: Rs.499
''')
                    n = 1
                    while n == 1:
                        choice_7 = input("\n>>> Enter The Supplement You Wish To Buy [ Or Enter 'B' To Go Back ] : ")
                        if choice_7 == '1' or choice_7 == '2' or choice_7 == '3' or choice_7 == '4' or choice_7 == '5' or choice_7 == '6' or choice_7 == '7' or choice_7 == '8':
                            w = 1
                            while w == 1:
                                choice_8_1 = input("\n>>> Enter The Quantity: ")
                                if int(choice_8_1) >= 1 and int(choice_8_1) <= 10:
                                    if choice_7 == '1' and choice_8_1.isdigit():
                                        choice_8 = int(choice_8_1)
                                        ac = 1
                                        while ac == 1:
                                            print("\nChoose Your Mode Of Payment: ")
                                            print("\n1 -- Debit Card")
                                            print("\n2 -- Credit Card")
                                            choice_13 = input("\n>>> ")
                                            if choice_13 == '1' or choice_13 == '2':
                                                ad = 1
                                                while ad == 1:
                                                    choice_14 = input("\n>>> Enter Your Card Number: ")
                                                    choice_15 = input("\n>>> Enter Your Pin: ")
                                                    if len(choice_14) == 16 and len(choice_15) == 4:
                                                        ac += 1
                                                        ad += 1
                                                    else:
                                                        print("\nInvalid Card Number Or Pin. Try Again!")
                                                        ad = 1
                                            else:
                                                print("\nInvalid Input. Try Again!")
                                                ac = 1
                                        ae = 1
                                        while ae == 1:
                                            print("\nEnter 'Y' To Confirm Payment")
                                            print("\nEnter 'N' To Deny Payment")
                                            choice_16 = input("\n>>> ")
                                            if choice_16.lower() == 'y':

                                                price1 = choice_8 * 379
                                                price = price1
                                                print("     Payment Successful")

                                                cur.execute("update menu set PreW=PreW+%s where User_name=%s",
                                                            (choice_8, username,))
                                                mycon.commit()
                                                cur.execute("update menu set Amount=Amount+%s where User_name=%s",
                                                            (price, username))
                                                mycon.commit()
                                                print("\n               BILL")
                                                print("\nSupplement Purchased: 'Pre-Workout' ")
                                                print("\nQuantity Purchased: ", choice_8)
                                                print("\nAmount Payed: ", price1)
                                                d = 1
                                                while d == 1:
                                                    choice_6 = input("\n>>> Enter 'B' To Go Back: ")
                                                    if choice_6.lower() == 'b':
                                                        print("\nYou Have Chosen To Go Back")
                                                        n += 1
                                                        d += 1
                                                        m = 1
                                                        w += 1
                                                        ae += 1
                                                    else:
                                                        print("\nInvalid Input. Try Again!")
                                                        d = 1
                                            elif choice_16.lower() == 'n':
                                                print("\nPayment Cancelled")
                                                d = 1
                                                while d == 1:
                                                    choice_6 = input("\n>>> Enter 'B' To Go Back: ")
                                                    if choice_6.lower() == 'b':
                                                        print("\nYou Have Chosen To Go Back")
                                                        n += 1
                                                        d += 1
                                                        ae += 1
                                                        w += 1
                                                        m = 1
                                                    else:
                                                        print("\nInvalid Input. Try Again!")
                                                        d = 1

                                            else:
                                                print("\nInvalid Input. Try Again!")
                                                ae = 1

                                    elif choice_7 == '2' and choice_8_1.isdigit():
                                        choice_8 = int(choice_8_1)
                                        ac = 1
                                        while ac == 1:
                                            print("\nChoose Your Mode Of Payment: ")
                                            print("\n1 -- Debit Card")
                                            print("\n2 -- Credit Card")
                                            choice_13 = input("\n>>> ")
                                            if choice_13 == '1' or choice_13 == '2':
                                                ad = 1
                                                while ad == 1:
                                                    choice_14 = input("\n>>> Enter Your Card Number: ")
                                                    choice_15 = input("\n>>> Enter Your Pin: ")
                                                    if len(choice_14) == 16 and len(choice_15) == 4:
                                                        ac += 1
                                                        ad += 1
                                                    else:
                                                        print("\nInvalid Card Number Or Pin. Try Again!")
                                                        ad = 1
                                            else:
                                                print("\nInvalid Input. Try Again!")
                                                ac = 1
                                        ae = 1
                                        while ae == 1:
                                            print("\nEnter 'Y' To Confirm Payment")
                                            print("\nEnter 'N' To Deny Payment")
                                            choice_16 = input("\n>>> ")
                                            if choice_16.lower() == 'y':

                                                price1 = choice_8 * 499
                                                price = price1
                                                print("     Payment Successful")

                                                cur.execute("update menu set PRX=PRX+%s where User_name=%s",
                                                            (choice_8, username,))
                                                mycon.commit()
                                                cur.execute("update menu set Amount=Amount+%s where User_name=%s",
                                                            (price, username))
                                                mycon.commit()
                                                print("\n               BILL")
                                                print("\nSupplement Purchased: 'PR-X Max Strength/Energy' ")
                                                print("\nQuantity Purchased: ", choice_8)
                                                print("\nAmount Payed: ", price1)
                                                d = 1
                                                while d == 1:
                                                    choice_6 = input("\n>>> Enter 'B' To Go Back: ")
                                                    if choice_6.lower() == 'b':
                                                        print("\nYou Have Chosen To Go Back")
                                                        n += 1
                                                        d += 1
                                                        m = 1
                                                        w += 1
                                                        ae += 1
                                                    else:
                                                        print("\nInvalid Input. Try Again!")
                                                        d = 1
                                            elif choice_16.lower() == 'n':
                                                print("\nPayment Cancelled")
                                                d = 1
                                                while d == 1:
                                                    choice_6 = input("\n>>> Enter 'B' To Go Back: ")
                                                    if choice_6.lower() == 'b':
                                                        print("\nYou Have Chosen To Go Back")
                                                        n += 1
                                                        d += 1
                                                        ae += 1
                                                        w += 1
                                                        m = 1
                                                    else:
                                                        print("\nInvalid Input. Try Again!")
                                                        d = 1

                                            else:
                                                print("\nInvalid Input. Try Again!")
                                                ae = 1

                                    elif choice_7 == '3' and choice_8_1.isdigit():
                                        choice_8 = int(choice_8_1)
                                        ac = 1
                                        while ac == 1:
                                            print("\nChoose Your Mode Of Payment: ")
                                            print("\n1 -- Debit Card")
                                            print("\n2 -- Credit Card")
                                            choice_13 = input("\n>>> ")
                                            if choice_13 == '1' or choice_13 == '2':
                                                ad = 1
                                                while ad == 1:
                                                    choice_14 = input("\n>>> Enter Your Card Number: ")
                                                    choice_15 = input("\n>>> Enter Your Pin: ")
                                                    if len(choice_14) == 16 and len(choice_15) == 4:
                                                        ac += 1
                                                        ad += 1
                                                    else:
                                                        print("\nInvalid Card Number Or Pin. Try Again!")
                                                        ad = 1
                                            else:
                                                print("\nInvalid Input. Try Again!")
                                                ac = 1
                                        ae = 1
                                        while ae == 1:
                                            print("\nEnter 'Y' To Confirm Payment")
                                            print("\nEnter 'N' To Deny Payment")
                                            choice_16 = input("\n>>> ")
                                            if choice_16.lower() == 'y':

                                                price1 = choice_8 * 549
                                                price = price1
                                                print("     Payment Successful")

                                                cur.execute("update menu set PPP=PPP+%s where User_name=%s",
                                                            (choice_8, username,))
                                                mycon.commit()
                                                cur.execute("update menu set Amount=Amount+%s where User_name=%s",
                                                            (price, username))
                                                mycon.commit()
                                                print("\n               BILL")
                                                print("\nSupplement Purchased: 'Premium Protein Powder' ")
                                                print("\nQuantity Purchased: ", choice_8)
                                                print("\nAmount Payed: ", price1)
                                                d = 1
                                                while d == 1:
                                                    choice_6 = input("\n>>> Enter 'B' To Go Back: ")
                                                    if choice_6.lower() == 'b':
                                                        print("\nYou Have Chosen To Go Back")
                                                        n += 1
                                                        d += 1
                                                        m = 1
                                                        w += 1
                                                        ae += 1
                                                    else:
                                                        print("\nInvalid Input. Try Again!")
                                                        d = 1
                                            elif choice_16.lower() == 'n':
                                                print("\nPayment Cancelled")
                                                d = 1
                                                while d == 1:
                                                    choice_6 = input("\n>>> Enter 'B' To Go Back: ")
                                                    if choice_6.lower() == 'b':
                                                        print("\nYou Have Chosen To Go Back")
                                                        n += 1
                                                        d += 1
                                                        ae += 1
                                                        w += 1
                                                        m = 1
                                                    else:
                                                        print("\nInvalid Input. Try Again!")
                                                        d = 1

                                            else:
                                                print("\nInvalid Input. Try Again!")
                                                ae = 1


                                    elif choice_7 == '4' and choice_8_1.isdigit():
                                        choice_8 = int(choice_8_1)
                                        ac = 1
                                        while ac == 1:
                                            print("\nChoose Your Mode Of Payment: ")
                                            print("\n1 -- Debit Card")
                                            print("\n2 -- Credit Card")
                                            choice_13 = input("\n>>> ")
                                            if choice_13 == '1' or choice_13 == '2':
                                                ad = 1
                                                while ad == 1:
                                                    choice_14 = input("\n>>> Enter Your Card Number: ")
                                                    choice_15 = input("\n>>> Enter Your Pin: ")
                                                    if len(choice_14) == 16 and len(choice_15) == 4:
                                                        ac += 1
                                                        ad += 1
                                                    else:
                                                        print("\nInvalid Card Number Or Pin. Try Again!")
                                                        ad = 1
                                            else:
                                                print("\nInvalid Input. Try Again!")
                                                ac = 1
                                        ae = 1
                                        while ae == 1:
                                            print("\nEnter 'Y' To Confirm Payment")
                                            print("\nEnter 'N' To Deny Payment")
                                            choice_16 = input("\n>>> ")
                                            if choice_16.lower() == 'y':

                                                price1 = choice_8 * 529
                                                price = price1
                                                print("     Payment Successful")

                                                cur.execute("update menu set MR=MR+%s where User_name=%s",
                                                            (choice_8, username,))
                                                mycon.commit()
                                                cur.execute("update menu set Amount=Amount+%s where User_name=%s",
                                                            (price, username))
                                                mycon.commit()
                                                print("\n               BILL")
                                                print("\nSupplement Purchased: 'Muscle Recovery' ")
                                                print("\nQuantity Purchased: ", choice_8)
                                                print("\nAmount Payed: ", price1)
                                                d = 1
                                                while d == 1:
                                                    choice_6 = input("\n>>> Enter 'B' To Go Back: ")
                                                    if choice_6.lower() == 'b':
                                                        print("\nYou Have Chosen To Go Back")
                                                        n += 1
                                                        d += 1
                                                        m = 1
                                                        w += 1
                                                        ae += 1
                                                    else:
                                                        print("\nInvalid Input. Try Again!")
                                                        d = 1
                                            elif choice_16.lower() == 'n':
                                                print("\nPayment Cancelled")
                                                d = 1
                                                while d == 1:
                                                    choice_6 = input("\n>>> Enter 'B' To Go Back: ")
                                                    if choice_6.lower() == 'b':
                                                        print("\nYou Have Chosen To Go Back")
                                                        n += 1
                                                        d += 1
                                                        ae += 1
                                                        w += 1
                                                        m = 1
                                                    else:
                                                        print("\nInvalid Input. Try Again!")
                                                        d = 1

                                            else:
                                                print("\nInvalid Input. Try Again!")
                                                ae = 1

                                    elif choice_7 == '5' and choice_8_1.isdigit():
                                        choice_8 = int(choice_8_1)
                                        ac = 1
                                        while ac == 1:
                                            print("\nChoose Your Mode Of Payment: ")
                                            print("\n1 -- Debit Card")
                                            print("\n2 -- Credit Card")
                                            choice_13 = input("\n>>> ")
                                            if choice_13 == '1' or choice_13 == '2':
                                                ad = 1
                                                while ad == 1:
                                                    choice_14 = input("\n>>> Enter Your Card Number: ")
                                                    choice_15 = input("\n>>> Enter Your Pin: ")
                                                    if len(choice_14) == 16 and len(choice_15) == 4:
                                                        ac += 1
                                                        ad += 1
                                                    else:
                                                        print("\nInvalid Card Number Or Pin. Try Again!")
                                                        ad = 1
                                            else:
                                                print("\nInvalid Input. Try Again!")
                                                ac = 1
                                        ae = 1
                                        while ae == 1:
                                            print("\nEnter 'Y' To Confirm Payment")
                                            print("\nEnter 'N' To Deny Payment")
                                            choice_16 = input("\n>>> ")
                                            if choice_16.lower() == 'y':

                                                price1 = choice_8 * 459
                                                price = price1
                                                print("     Payment Successful")

                                                cur.execute("update menu set WAIOP=WAIOP+%s where User_name=%s",
                                                            (choice_8, username,))
                                                mycon.commit()
                                                cur.execute("update menu set Amount=Amount+%s where User_name=%s",
                                                            (price, username))
                                                mycon.commit()
                                                print("\n               BILL")
                                                print("\nSupplement Purchased: 'Women's All In One Protein' ")
                                                print("\nQuantity Purchased: ", choice_8)
                                                print("\nAmount Payed: ", price1)
                                                d = 1
                                                while d == 1:
                                                    choice_6 = input("\n>>> Enter 'B' To Go Back: ")
                                                    if choice_6.lower() == 'b':
                                                        print("\nYou Have Chosen To Go Back")
                                                        n += 1
                                                        d += 1
                                                        m = 1
                                                        w += 1
                                                        ae += 1
                                                    else:
                                                        print("\nInvalid Input. Try Again!")
                                                        d = 1
                                            elif choice_16.lower() == 'n':
                                                print("\nPayment Cancelled")
                                                d = 1
                                                while d == 1:
                                                    choice_6 = input("\n>>> Enter 'B' To Go Back: ")
                                                    if choice_6.lower() == 'b':
                                                        print("\nYou Have Chosen To Go Back")
                                                        n += 1
                                                        d += 1
                                                        ae += 1
                                                        w += 1
                                                        m = 1
                                                    else:
                                                        print("\nInvalid Input. Try Again!")
                                                        d = 1

                                            else:
                                                print("\nInvalid Input. Try Again!")
                                                ae = 1

                                    elif choice_7 == '6' and choice_8_1.isdigit():
                                        choice_8 = int(choice_8_1)
                                        ac = 1
                                        while ac == 1:
                                            print("\nChoose Your Mode Of Payment: ")
                                            print("\n1 -- Debit Card")
                                            print("\n2 -- Credit Card")
                                            choice_13 = input("\n>>> ")
                                            if choice_13 == '1' or choice_13 == '2':
                                                ad = 1
                                                while ad == 1:
                                                    choice_14 = input("\n>>> Enter Your Card Number: ")
                                                    choice_15 = input("\n>>> Enter Your Pin: ")
                                                    if len(choice_14) == 16 and len(choice_15) == 4:
                                                        ac += 1
                                                        ad += 1
                                                    else:
                                                        print("\nInvalid Card Number Or Pin. Try Again!")
                                                        ad = 1
                                            else:
                                                print("\nInvalid Input. Try Again!")
                                                ac = 1
                                        ae = 1
                                        while ae == 1:
                                            print("\nEnter 'Y' To Confirm Payment")
                                            print("\nEnter 'N' To Deny Payment")
                                            choice_16 = input("\n>>> ")
                                            if choice_16.lower() == 'y':

                                                price1 = choice_8 * 499
                                                price = price1
                                                print("     Payment Successful")

                                                cur.execute("update menu set OFO=OFO+%s where User_name=%s",
                                                            (choice_8, username,))
                                                mycon.commit()
                                                cur.execute("update menu set Amount=Amount+%s where User_name=%s",
                                                            (price, username))
                                                mycon.commit()
                                                print("\n               BILL")
                                                print("\nSupplement Purchased: 'Omega-3 Fish Oil' ")
                                                print("\nQuantity Purchased: ", choice_8)
                                                print("\nAmount Payed: ", price1)
                                                d = 1
                                                while d == 1:
                                                    choice_6 = input("\n>>> Enter 'B' To Go Back: ")
                                                    if choice_6.lower() == 'b':
                                                        print("\nYou Have Chosen To Go Back")
                                                        n += 1
                                                        d += 1
                                                        m = 1
                                                        w += 1
                                                        ae += 1
                                                    else:
                                                        print("\nInvalid Input. Try Again!")
                                                        d = 1
                                            elif choice_16.lower() == 'n':
                                                print("\nPayment Cancelled")
                                                d = 1
                                                while d == 1:
                                                    choice_6 = input("\n>>> Enter 'B' To Go Back: ")
                                                    if choice_6.lower() == 'b':
                                                        print("\nYou Have Chosen To Go Back")
                                                        n += 1
                                                        d += 1
                                                        ae += 1
                                                        w += 1
                                                        m = 1
                                                    else:
                                                        print("\nInvalid Input. Try Again!")
                                                        d = 1

                                            else:
                                                print("\nInvalid Input. Try Again!")
                                                ae = 1

                                    elif choice_7 == '7' and choice_8_1.isdigit():
                                        choice_8 = int(choice_8_1)
                                        ac = 1
                                        while ac == 1:
                                            print("\nChoose Your Mode Of Payment: ")
                                            print("\n1 -- Debit Card")
                                            print("\n2 -- Credit Card")
                                            choice_13 = input("\n>>> ")
                                            if choice_13 == '1' or choice_13 == '2':
                                                ad = 1
                                                while ad == 1:
                                                    choice_14 = input("\n>>> Enter Your Card Number: ")
                                                    choice_15 = input("\n>>> Enter Your Pin: ")
                                                    if len(choice_14) == 16 and len(choice_15) == 4:
                                                        ac += 1
                                                        ad += 1
                                                    else:
                                                        print("\nInvalid Card Number Or Pin. Try Again!")
                                                        ad = 1
                                            else:
                                                print("\nInvalid Input. Try Again!")
                                                ac = 1
                                        ae = 1
                                        while ae == 1:
                                            print("\nEnter 'Y' To Confirm Payment")
                                            print("\nEnter 'N' To Deny Payment")
                                            choice_16 = input("\n>>> ")
                                            if choice_16.lower() == 'y':

                                                price1 = choice_8 * 499
                                                price = price1
                                                print("     Payment Successful")

                                                cur.execute("update menu set JR=JR+%s where User_name=%s",
                                                            (choice_8, username,))
                                                mycon.commit()
                                                cur.execute("update menu set Amount=Amount+%s where User_name=%s",
                                                            (price, username))
                                                mycon.commit()
                                                print("\n               BILL")
                                                print("\nSupplement Purchased: 'Joint Recovery' ")
                                                print("\nQuantity Purchased: ", choice_8)
                                                print("\nAmount Payed: ", price1)
                                                d = 1
                                                while d == 1:
                                                    choice_6 = input("\n>>> Enter 'B' To Go Back: ")
                                                    if choice_6.lower() == 'b':
                                                        print("\nYou Have Chosen To Go Back")
                                                        n += 1
                                                        d += 1
                                                        m = 1
                                                        w += 1
                                                        ae += 1
                                                    else:
                                                        print("\nInvalid Input. Try Again!")
                                                        d = 1
                                            elif choice_16.lower() == 'n':
                                                print("\nPayment Cancelled")
                                                d = 1
                                                while d == 1:
                                                    choice_6 = input("\n>>> Enter 'B' To Go Back: ")
                                                    if choice_6.lower() == 'b':
                                                        print("\nYou Have Chosen To Go Back")
                                                        n += 1
                                                        d += 1
                                                        ae += 1
                                                        w += 1
                                                        m = 1
                                                    else:
                                                        print("\nInvalid Input. Try Again!")
                                                        d = 1

                                            else:
                                                print("\nInvalid Input. Try Again!")
                                                ae = 1

                                    elif choice_7 == '8' and choice_8_1.isdigit():
                                        choice_8 = int(choice_8_1)
                                        ac = 1
                                        while ac == 1:
                                            print("\nChoose Your Mode Of Payment: ")
                                            print("\n1 -- Debit Card")
                                            print("\n2 -- Credit Card")
                                            choice_13 = input("\n>>> ")
                                            if choice_13 == '1' or choice_13 == '2':
                                                ad = 1
                                                while ad == 1:
                                                    choice_14 = input("\n>>> Enter Your Card Number: ")
                                                    choice_15 = input("\n>>> Enter Your Pin: ")
                                                    if len(choice_14) == 16 and len(choice_15) == 4:
                                                        ac += 1
                                                        ad += 1
                                                    else:
                                                        print("\nInvalid Card Number Or Pin. Try Again!")
                                                        ad = 1
                                            else:
                                                print("\nInvalid Input. Try Again!")
                                                ac = 1
                                        ae = 1
                                        while ae == 1:
                                            print("\nEnter 'Y' To Confirm Payment")
                                            print("\nEnter 'N' To Deny Payment")
                                            choice_16 = input("\n>>> ")
                                            if choice_16.lower() == 'y':

                                                price1 = choice_8 * 499
                                                price = price1
                                                print("     Payment Successful")
                                                
                                                cur.execute("update menu set BCAA=BCAA+%s where User_name=%s",
                                                            (choice_8, username,))
                                                mycon.commit()
                                                cur.execute("update menu set Amount=Amount+%s where User_name=%s",
                                                            (price, username))
                                                mycon.commit()
                                                print("\n               BILL")
                                                print("\nSupplement Purchased: 'BCAA's' ")
                                                print("\nQuantity Purchased: ", choice_8)
                                                print("\nAmount Payed: ", price1)
                                                d = 1
                                                while d == 1:
                                                    choice_6 = input("\n>>> Enter 'B' To Go Back: ")
                                                    if choice_6.lower() == 'b':
                                                        print("\nYou Have Chosen To Go Back")
                                                        n += 1
                                                        d += 1
                                                        m = 1
                                                        w += 1
                                                        ae += 1
                                                    else:
                                                        print("\nInvalid Input. Try Again!")
                                                        d = 1
                                            elif choice_16.lower() == 'n':
                                                print("\nPayment Cancelled")
                                                d = 1
                                                while d == 1:
                                                    choice_6 = input("\n>>> Enter 'B' To Go Back: ")
                                                    if choice_6.lower() == 'b':
                                                        print("\nYou Have Chosen To Go Back")
                                                        n += 1
                                                        d += 1
                                                        ae += 1
                                                        w += 1
                                                        m = 1
                                                    else:
                                                        print("\nInvalid Input. Try Again!")
                                                        d = 1

                                            else:
                                                print("\nInvalid Input. Try Again!")
                                                ae = 1

                                    else:
                                        print("\nInvalid Input. Try Again!")
                                        n = 1
                                        w += 1

                                else:
                                    print("\nMaximum Quantity Is 10 Units")
                                    print("     Try Again!")
                                    w = 1

                        elif choice_7.lower() == 'b':
                            print("\nYou Have Chosen To Go Back")
                            n += 1

                        else:
                            print("\nInvalid Input. Try Again!")
                            n = 1


                elif choice_menu == "3":
                    v = 1
                    while v == 1:
                        print("  ")
                        print("_" * 128)
                        print(
                            "\n                                           PACKAGES                                                       ")
                        print("\n1. Bronze Package")
                        print("\n2. Silver Package")
                        print("\n3. Gold Package")
                        print("\n4. Back")
                        choice_11 = input("\n>>> ")

                        if choice_11 == '1':
                            print('''
                --- Bronze Package ---     
Description:
This Package Is Focused Entirely On The Theme 'Weight Loss [ One Pound At A Time ]'
It Includes Diet Plans And Intense Cardio Workouts
The Trainer Will Alter The Conditions Depending On Your Potential 
This Package Will Be Valid For 6 Months, After Which You Would Have Attained Your Goals
Price - Rs.7,999
''')
                            ac = 1
                            while ac == 1:
                                print("\nChoose Your Mode Of Payment: ")
                                print("\n1 -- Debit Card")
                                print("\n2 -- Credit Card")
                                choice_13 = input("\n>>> ")
                                if choice_13 == '1' or choice_13 == '2':
                                    ad = 1
                                    while ad == 1:
                                        choice_14 = input("\n>>> Enter Your Card Number: ")
                                        choice_15 = input("\n>>> Enter Your Pin: ")
                                        if len(choice_14) == 16 and len(choice_15) == 4:
                                            ac += 1
                                            ad += 1
                                        else:
                                            print("\nInvalid Card Number Or Pin. Try Again!")
                                            ad = 1
                                else:
                                    print("\nInvalid Input. Try Again!")
                                    ac = 1
                            u = 1
                            while u == 1:
                                choice_12 = input("\n>>> Enter 'C' To Confirm Purchase [ Or Enter 'B' To Go Back ]: ")
                                if choice_12.lower() == 'c':
                                    cur.execute("select Bronze from pack where user_name=%s", (username,))
                                    data2 = cur.fetchall()
                                    if data2[0][0] == None:
                                        print("\nYou Have Successfully Purchased The Bronze Package")
                                        cur.execute("update pack set Bronze='Active' where user_name=%s", (username,))
                                        mycon.commit()
                                        cur.execute("update pack set Paid_1=Paid_1+7999 where user_name=%s",
                                                    (username,))
                                        mycon.commit()
                                        cur.execute("update pack set EndDateBronze=curdate() where user_name=%s",
                                                    (username,))
                                        mycon.commit()
                                        cur.execute(
                                            "update pack set EndDateBronze=date_add(EndDateBronze, interval 6 month) where user_name=%s",
                                            (username,))
                                        mycon.commit()
                                    else:
                                        print("\nThis Package Is Already Active")
                                        print("     Payment Cancelled")

                                    d = 1
                                    while d == 1:
                                        choice_6 = input("\n>>> Enter 'B' To Go Back: ")
                                        if choice_6.lower() == 'b':
                                            print("\nYou Have Chosen To Go Back")
                                            u += 1
                                            d += 1
                                            v = 1

                                        else:
                                            print("\nInvalid Input. Try Again!")
                                            d = 1

                                elif choice_12.lower() == 'b':
                                    print("\nYou Have Chosen To Go Back")
                                    u += 1
                                    v = 1

                                else:
                                    print("\nInvalid Input. Try Again!")
                                    u = 1

                        elif choice_11 == '2':
                            print('''
                --- Silver Package ---     
Description:
This Package Is Focused Entirely On The Theme 'Muscle And Size' 
It Includes Diet Plans And Supplement Suggestions From The Trainer
It Involves Intense Resistance Work Outs
A Trainer Will Always Be Supervising You To Ensure Your Safety
This Package Is Valid For 12 Months, After Which You Can See Amazing Results
Price - Rs.15,999
''')
                            ac = 1
                            while ac == 1:
                                print("\nChoose Your Mode Of Payment: ")
                                print("\n1 -- Debit Card")
                                print("\n2 -- Credit Card")
                                choice_13 = input("\n>>> ")
                                if choice_13 == '1' or choice_13 == '2':
                                    ad = 1
                                    while ad == 1:
                                        choice_14 = input("\n>>> Enter Your Card Number: ")
                                        choice_15 = input("\n>>> Enter Your Pin: ")
                                        if len(choice_14) == 16 and len(choice_15) == 4:
                                            ac += 1
                                            ad += 1
                                        else:
                                            print("\nInvalid Card Number Or Pin. Try Again!")
                                            ad = 1
                                else:
                                    print("\nInvalid Input. Try Again!")
                                    ac = 1
                            u = 1
                            while u == 1:
                                choice_12 = input("\n>>> Enter 'C' To Confirm Purchase [ Or Enter 'B' To Go Back ]: ")
                                if choice_12.lower() == 'c':
                                    cur.execute("select Silver from pack where user_name=%s", (username,))
                                    data2 = cur.fetchall()
                                    if data2[0][0] == None:
                                        print("\nYou Have Successfully Purchased The Silver Package")
                                        cur.execute("update pack set Silver='Active' where user_name=%s", (username,))
                                        mycon.commit()
                                        cur.execute("update pack set Paid_1=Paid_1+15999 where user_name=%s",
                                                    (username,))
                                        mycon.commit()
                                        cur.execute("update pack set EndDateSilver=curdate() where user_name=%s",
                                                    (username,))
                                        mycon.commit()
                                        cur.execute(
                                            "update pack set EndDateSilver=date_add(EndDateSilver, interval 12 month) where user_name=%s",
                                            (username,))
                                        mycon.commit()

                                    else:
                                        print("\nThis Package Is Already Active")
                                        print("     Payment Cancelled")

                                    d = 1
                                    while d == 1:
                                        choice_6 = input("\n>>> Enter 'B' To Go Back: ")
                                        if choice_6.lower() == 'b':
                                            print("\nYou Have Chosen To Go Back")
                                            u += 1
                                            d += 1
                                            v = 1

                                        else:
                                            print("\nInvalid Input. Try Again!")
                                            d = 1

                                elif choice_12.lower() == 'b':
                                    print("\nYou Have Chosen To Go Back")
                                    u += 1
                                    v = 1

                                else:
                                    print("\nInvalid Input. Try Again!")
                                    u = 1

                        elif choice_11 == '3':
                            print('''
                --- Gold Package ---      
This Package Is Entirely Focused On The Theme 'Fit For Life'
It Depends Both On Your Physical As Well As Mental Health
We Provide You With Yoga For Your Physical Flexibility
We Also Improve Your Physical Health Depending On Your Present Condition
The Trainer Provides You With Healthy Meal Plans Throughout The Session [ Varies From Person To Person ]
This Package Is Valid For 9 Months, After Which You Can Continue This Session By Renewing The Package
Price - Rs.10,999
''')
                            ac = 1
                            while ac == 1:
                                print("\nChoose Your Mode Of Payment: ")
                                print("\n1 -- Debit Card")
                                print("\n2 -- Credit Card")
                                choice_13 = input("\n>>> ")
                                if choice_13 == '1' or choice_13 == '2':
                                    ad = 1
                                    while ad == 1:
                                        choice_14 = input("\n>>> Enter Your Card Number: ")
                                        choice_15 = input("\n>>> Enter Your Pin: ")
                                        if len(choice_14) == 16 and len(choice_15) == 4:
                                            ac += 1
                                            ad += 1
                                        else:
                                            print("\nInvalid Card Number Or Pin. Try Again!")
                                            ad = 1
                                else:
                                    print("\nInvalid Input. Try Again!")
                                    ac = 1
                            u = 1
                            while u == 1:
                                choice_12 = input("\n>>> Enter 'C' To Confirm Purchase [ Or Enter 'B' To Go Back ]: ")
                                if choice_12.lower() == 'c':
                                    cur.execute("select Gold from pack where user_name=%s", (username,))
                                    data2 = cur.fetchall()
                                    if data2[0][0] == None:
                                        print("\nYou Have Successfully Purchased The Gold Package")
                                        cur.execute("update pack set Gold='Active' where user_name=%s", (username,))
                                        mycon.commit()
                                        cur.execute("update pack set Paid_1=Paid_1+10999 where user_name=%s",
                                                    (username,))
                                        mycon.commit()
                                        cur.execute("update pack set EndDateGold=curdate() where user_name=%s",
                                                    (username,))
                                        mycon.commit()
                                        cur.execute(
                                            "update pack set EndDateGold=date_add(EndDateGold, interval 9 month) where user_name=%s",
                                            (username,))
                                        mycon.commit()

                                    else:
                                        print("\nThis Package Is Already Active")
                                        print("     Payment Cancelled")

                                    d = 1
                                    while d == 1:
                                        choice_6 = input("\n>>> Enter 'B' To Go Back: ")
                                        if choice_6.lower() == 'b':
                                            print("\nYou Have Chosen To Go Back")
                                            u += 1
                                            d += 1
                                            v = 1

                                        else:
                                            print("\nInvalid Input. Try Again!")
                                            d = 1

                                elif choice_12.lower() == 'b':
                                    print("\nYou Have Chosen To Go Back")
                                    u += 1
                                    v = 1

                                else:
                                    print("\nInvalid Input. Try Again!")
                                    u = 1


                        elif choice_11 == '4':
                            print("\nYou Have Chosen To Go Back")
                            v += 1

                        else:
                            print("\nInvalid Input. Try Again!")
                            v = 1

                elif choice_menu == "4":
                    print("\nYou Have Chosen To Go Back")
                    m += 1

                else:
                    print("\nInvalid Input. Try Again!")
                    m = 1

        elif choice_2 == "3":
            print("  ")
            print("_" * 128)
            print(
                "\n                                            ABOUT US                                                      ")
            print('''
A Gym Isn't Just A Place For Exercise,
It's The Place You Go To Unwind, Socialize And Work Out
The Gym Is A Whole Experience. 
Some Of The Most Successful Facilities Have Several Gym Features That Contribute 
To  The Kind Of Member Experience That Drives Retention And Sales.
FSA FITness Center Is The Exact Example For This.

Motivation And Accountability:
    In FSA FITness Center, We Always Provide Members With Trainers Who Motivate 
    You And Hold You Accountable. 

Community And Socializing:
    In FSA FITness Center, Mental Health Is Also Given Importance. 
    Mental Health Is A Huge Topic Right Now, Considering The Lock Down Periods.
    We Create An Environment That Nurtures Human Connection.
    We Encourage Members To Socialize And Develop Their Fitness Community

Clean And Hygienic:
    Cleanliness And Hygiene Have Always Been Important Facotrs When It Comes To
    Investing In A Gym Membership Or Visiting A Fitness Facility.
    In FSA FITness Center, We Disinfect And Sanitize The Whole Gym Everyday To 
    Ensure Your Safety

Equipment And Space:
    In FSA FITness Center, We Create An Environment That Motivates You To Work
    Out And Provide You With The Equipment To Do So.
    We Provide A Perfect Niche For All The Members To Be Comfortable Using The 
    Facilities

Training Ability:
    In FSA FITness Center, We Provide Niches For People With Different Training
    Abilities.
    We Provide The Members With Various Options For Training Abilities, And 
    Create A Welcoming And Accessible Environment

Hours Of Operation And Location:
    Open: Week Days [ 4:00 A.M. - 12:00 P.M. ] 
          Week Ends [ 4:00 A.M. - 11:00 P.M. ]

    Locations: Tirunelveli, Coimbatore, Chennai, Tenkasi, Erode, Madurai,
                          Vellore, Trichy, Thanjavur 

    Contact Us: +91 7339 267 663


''')
            d = 1
            while d == 1:
                choice_6 = input("\n>>> Enter 'B' To Go Back: ")
                if choice_6.lower() == 'b':
                    print("\nYou Have Chosen To Go Back")
                    a = 1
                    d += 1

                else:
                    print("\nInvalid Input. Try Again!")
                    d = 1

        elif choice_2 == '4':
            print("\nThank You For Using FSA FITness Centre!")
            print("\nCome Back Again Soon!")
            a += 1

        else:
            print("\nInvalid Input. Try Again!")
            a = 1


fitness_menu()
