print("enter your card")

print("language")
print("press 1 for english")
print("press 2 for hindi")
print("press 3 for gujarati")
language=int(input("select your language:"))

if language==1:
    print("english")
    pincode=int(input("enter your pincord:"))

    if pincode==8423:
        amount=int(input("enter amount:"))
        balance=50000
        print("checking your balance")
        if amount<=50000:
            print("please collect your cash")
            print("cheking your remaning balance?")
            print("press 1 for yes")
            print("press 2 for no")
            remaningbalance=int(input("select your option yes or no:"))
            if remaningbalance==1:
                remaningbalance=balance-amount
                print(remaningbalance)
            elif remaningbalance==2:
                print("thank you")
        else:
            print("your account is null")
    else:
        print("your pincord is rong")
elif language==2:
    print("hindi")
    pincode=int(input("अपना पिनकॉर्ड दर्ज करें:"))

    if pincode==8423:
        amount=int(input("राशि दर्ज करें:"))
        balance=50000
        print("अपने संतुलन की जाँच करें")
        if amount<=50000:
            print("कृपया अपनी नकदी इकट्ठा करें")
            print("अपने रीमैनिंग बैलेंस को चेकिंग?")
            print("1 से हाँ करने के लिए")
            print("2 से लेकर नं.")
            remaningbalance=int(input("अपने विकल्प हाँ या नहीं का चयन करें:"))
            if 1:
                remaningbalance=balance-amount
                print(remaningbalance)
            elif 2:
                print("धन्यवाद")
        else:
            print("आपका खाता अमान्य है")
    else:
        print("अपने पिनकॉर्ड रोंग है")
elif language==3:
    print("gujarati")
    pincode=int(input("તમારું પિનકોર્ડ દાખલ કરો:"))

    if pincode==8423:
        amount=int(input("રકમ દાખલ કરો:"))
        balance=50000
        print("તમારી સંતુલન ચકાસી રહ્યા છીએ ")
        if amount<=50000:
            print("કૃપા કરીને તમારી રોકડ એકત્રિત કરો")
            print("તમારા રિમેનિંગ બેલેન્સને ચેન્ક કરવું છે?")
            print("હા માટે 1 પર ક્લિક કરો")
            print("ના માટે ૨ પર ક્લિક કરો")
            remaningbalance=int(input("તમારો વિકલ્પ 'હા' કે 'ના' પસંદ કરો:"))
            if 1:
                remaningbalance=balance-amount
                print(remaningbalance)
            elif 2:
                print("આભાર")
        else:
            print("તમારું ખાતું ખલી છે")
    else:
        print("તમારું પિનકોર્ડ રોંગ છે")
else:
    print("not found")


