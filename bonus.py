salary = int(input("enter the your salary"))
year=int(input("enter your year of services provided"))
if (year > 5) :
    a=(0.05 * salary)
    print (f"net bonus amount provided for your more than 5 year services is {a}")
    print (f"final salary {salary +a}")    
else:
    print("as your year of service is less than 5 , no bonus")
    print(''' 
        _____  ___      ______            _______     ______    _____  ___   ____  ____   ________  
        (\"   \|"  \    /    " \          |   _  "\   /    " \  (\"   \|"  \ ("  _||_ " | /"       ) 
        |.\\   \    |  // ____  \         (. |_)  :) // ____  \ |.\\   \    ||   (  ) : |(:   \___/  
        |: \.   \\  | /  /    ) :)        |:     \/ /  /    ) :)|: \.   \\  |(:  |  | . ) \___  \    
        |.  \    \. |(: (____/ //         (|  _  \\(: (____/ // |.  \    \. | \\ \__/ //   __/  \\   
        |    \    \ | \        /          |: |_)  :)\        /  |    \    \ | /\\ __ //\  /" \   :)  
        \___|\____\)  \"_____/           (_______/  \"_____/    \___|\____\)(__________)(_______/   
                                                                                                    ''')