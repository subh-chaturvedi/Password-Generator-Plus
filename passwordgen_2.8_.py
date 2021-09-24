# project random pass gen v2.7.0


# importing the required modules
import random
import os
import string

# defining the required lists

lst_all=list(string.printable)
[lst_all.pop(-1) for _ in "______"] # last 6 characters are not printable, they are removed.

lst_let=list(string.ascii_letters) # uppercase and lowercase alphabets
lst_let_up=list(string.ascii_uppercase) # uppercase alphabets
lst_let_low=list(string.ascii_lowercase) # lowercase alphabets
lst_num=['1','2','3','4','5','6','7','8','9','0']  # 0-9 numbers

lst_letnum=list(string.ascii_letters)# special characters excluded
lst_letnum.extend(lst_num)

# the quit counter
quiter=0

# defining a default value of passwords incase the user does not enter input
pass_no=1

# defining the tasks counter
counter_tasks=0

# defining the clipborad check test.false at default 
clip_copy=0

# the main function loop which runs till the program is made to quite with an input of '-q'
while quiter==0:
    
    # resetting the clipboard copy check to false for each cycle
    clip_copy=0
    
    #taking the main input
    main_inp=input("$- ")
    
    '''
    SYNTAX=>    
        -h: help
        alphanum(-,-) [-] -
        readable - -up/low
        fullran -
        -verbose for output to command line
        -q for quit
        -clip for clipbard copy(only if no. of passwords is 1)
    '''

    #checking for quit condition
    if main_inp.find("-q")!=-1:
        quiter=1
        print("quiting this turn")
        
        # printing the no. of tasks done
        print("tasks completed =>",counter_tasks)

    #checking for help condition
    if main_inp=='-h':
        # printing the synatx help
        print('-h: help')
        print('alphanum(<no. of digits>,<no. of alphabets>) [<no. of passwords>] ')
        print('readable -<total length> [<no. of passwords>] -<up/low>')
        print('fullran -<total length> [<no. of passwords>]')
        print('-verbose for output to command line')
        print('-clip for clipbard copy(only if no. of passwords is 1)')

    # initialising the verbose counter and putting it in the loop so as to reset it every cycle
    verbose=0

    # check for verbose condition
    if main_inp.find("-verbose")!=-1:
        verbose=1

    # check for the alphanum command
    if main_inp.find("alphanum")!= -1:
        
        
        # reading the no. of passwords if specified
        if main_inp.find("[")!=-1:
            pass_no =  int(main_inp[main_inp.find('[')+1])

        # opening the output file for writing
        file1 = open(r"C:\\passwords.txt","w+")
        
        # reading number of alphabets,numbers and using their sum for the length
        no_num =  int(main_inp[9])
        no_alpha =  int(main_inp[11])
        pass_l= no_alpha+no_num
        
        # checking for suiting conditions if clipboard copying is requested
        if main_inp.find("clip")!=-1 and pass_no==1:
            clip_copy=1
            
        # initialising a pair of hard coded variables so as to have the original number of alphabets and numbers available
        hard_no_num=no_num
        hard_no_alpha=no_alpha

        # writing a descriptive text to the file
        file1.write("passwords => \n")
        
        # loop to repeat the generation of  password as required
        for k in range(0,pass_no):
            # password is cleared every cycle
            password=''
            
            #reassigning the values of flexible number counters to their original values
            no_alpha=hard_no_alpha
            no_num=hard_no_num
            
            hardcode=2
            
            # generation loop for the password
            for i in range(0,pass_l):
                #the initial decider whether the character should be a number or an alphabet
                ifnum=random.choice([0,1])
                
                #the generating code
                if (ifnum==0 and no_num!=0) or hardcode==1:
                    newnum=random.randint(0,9)
                    password=password+str(newnum)
                    no_num=no_num-1
                    if no_num==0:
                        hardcode=0
                        if no_alpha==0:
                            hardcode=2
                if (ifnum==1 and no_alpha!=0) or hardcode==0:
                    newnum=random.choice(string.ascii_letters)
                    password=password+str(newnum)    
                    no_alpha=no_alpha-1
                    if no_alpha==0:
                        hardcode=1
                        if no_num==0:
                            hardcode=2      
            
            # copying to clipboard if required
            if clip_copy==1:
                os.system('echo ' + password + '| clip')
                            
            #append the password to the output file
            file1.write(password+"\n")
            
            #check for verbose condition. If true,then prints to the terminal
            if verbose==1:
                print(password)
         
        #print the task counter_tasks done. statement
        counter_tasks=counter_tasks+1
        print("task ", counter_tasks," done.")
        
        # close the file
        file1.close()
        
      
    # check for the readable command  
    elif main_inp.find("readable")!= -1:
        
        # opening the output file for writing
        file1 = open(r"E:\passwords.txt","w+")
        
        # defining the list from which the characters have to be choosed
        main_rand=lst_let
        
        #check for the -up/-lower command argument
        if  main_inp.find("up")!= -1:
             main_rand=lst_let_up
        if  main_inp.find("low")!= -1:
             main_rand=lst_let_low
             
        # reading number of passwords needed if needed and lenght
        if main_inp.find("[")!=-1:
            pass_no=""
            counternum=0
            checknum=0
            while checknum==0:               
                if main_inp[main_inp.find('[')+counternum+1].isnumeric():
                    pass_no=pass_no+(main_inp[main_inp.find('[')+counternum+1])
                    counternum=counternum+1
                else:
                    checknum=1
            pass_no =  int(pass_no)
            
        pass_l = int(main_inp[main_inp.find('-')+1])
        
        # checking for suiting conditions if clipboard copying is requested
        if main_inp.find("clip")!=-1 and pass_no==1:
            clip_copy=1
        
        # writing a descriptive text to the file
        file1.write("passwords => \n")
        
        # generation loop for the password
        for k in range(0,pass_no):
            password=''
            for m in range(0,pass_l):
                newnum=random.choice(main_rand)
                password=password+newnum
                
            #appending the generated password to the output file    
            file1.write(password+"\n")
            
            #check for verbose condition
            if verbose==1:
                print(password)
                
        #print the done statement   
        counter_tasks=counter_tasks+1
        print("task ", counter_tasks," done.")
        
        # copying to clipboard if required
        if clip_copy==1:
                os.system('echo ' + password + '| clip')
        
        # close the file
        file1.close()
        

    # check for the fullran command
    elif main_inp.find("fullran")!= -1:
        
        # opening the output file for writing
        file1 = open(r"E:\passwords.txt","w+")
        
        # defining the list from which the characters have to be choosed
        main_rand=lst_all
        
        # reading number of passwords needed if specified and lenght
        if main_inp.find("[")!=-1:
            pass_no =  int(main_inp[main_inp.find('[')+1])
        pass_l = int(main_inp[main_inp.find('-')+1])
        
        # checking for suiting conditions if clipboard copying is requested
        if main_inp.find("clip")!=-1 and pass_no==1:
            clip_copy=1
        
        # writing a descriptive text to the file
        file1.write("passwords => \n")
        
        # generation loop for the password
        for k in range(0,pass_no):
            password=''
            for m in range(0,pass_l):
                newnum=random.choice(main_rand)
                password=password+newnum
                
            #appending to output file 
            file1.write(password+"\n")
            
            # copying to clipboard if required
            if clip_copy==1:
                    os.system('echo ' + password + '| clip')
            
            #check for verbose condition. If true,then prints to the terminal
            if verbose==1:
                print(password)
                
        #print the done statement        
        counter_tasks=counter_tasks+1
        print("task ", counter_tasks," done.")
        
        # close the file
        file1.close()

    # condition to check if the command entered is wrong
    elif main_inp!="-q" and main_inp!="-h":
        print("synatax error")


#
