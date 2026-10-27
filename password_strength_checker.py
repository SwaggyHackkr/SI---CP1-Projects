#Salesi Ilaoa, Period 1, Password strength checker

#BEGIN
    #ISPLAY "Enter a password"
    #GET password FROM user
    #SET passed_checks to 0

    #IF length of password is at least 8 THEN
        #ADD 1 to passed_checks
    #END IF

    #IF password contains an uppercase letter THEN
        #ADD 1 to passed_checks
    #END IF

    #IF password contains a number THEN
        #ADD 1 to passed_checks
    #END IF

    #IF password contains a special character THEN
        #ADD 1 to passed_checks
    #END IF

    #WHILE passed_checks equals 0
       #DISPLAY "Password too weak, try again"
        #GET password FROM user
        #RE-RUN all the checks
    #END WHILE

    #IF passed_checks equals 1 OR passed_checks equals 2 THEN
        #DISPLAY "MEDIUM"
    #ELSE IF passed_checks equals 3 OR passed_checks equals 4 THEN
        #DISPLAY "STRONG"
    #ELSE
        #DISPLAY "WEAK"
    #END IF
#END