import zipfile                   
import time

folderpath = input('Path to the file: ')  
folderpath = folderpath.strip()
zipf = zipfile.ZipFile(folderpath)

if not zipf:          
    print('The zipped file/folder is not password protected! You can successfully open it!')  #Notifies if the zipped file/folder is not password encrypted

else:
    starttime = time.time()             
    result = 0                         
    c = 0                               

  
    characters =['0','1','2','3','4','5','6','7','8','9',
                 'a','b','c','d','e','f','g','h','i','j','l','k','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','p','Q','R','S','T','U','V','W','X','Y','Z',
                 '!','@','#','$','%','=',':','?','.','/','|','~','>','*','(',')','<','}','{','^','[',']',' ','+','-','_','&',';','"','?','`',"'",'\\']

    
    print("Brute Force Started...")
    
     
    if(result == 0):
        print("Checking for 4 character password...")
        for i in characters:
            for j in characters:
                for k in characters:
                    for l in characters:
                        guess = str(i) + str(j) + str(k) + str(l)
                        password=guess.encode('utf8').strip()
                        #print(guess)
                        c=c+1
                        try:
                            with zipfile.ZipFile(folderpath,'r') as zf:
                                zf.extractall(pwd=password)
                                print("Success! The password is: "+ guess)
                                endtime = time.time()           
                                result = 1                       
                                break                           
                        except:
                            pass
                    if result == 1:
                        break                          
                if result == 1:
                    break                              
            if result == 1:
                break                                   #If the password is found break from l for loop

    #Finally, if the password is not found even after appying all possile combination of characters upto 4 character length, notify the user as below, else print congratulations
    if(result == 0):
        print("Sorry, password not found. A total of "+str(c)+"+ possible combinations tried in "+str(duration)+" seconds. Password is not of 4 characters.")
    else:
        duration = endtime - starttime
        print('Congratulations!!! Password found after trying '+str(c)+' combinations in '+str(duration)+' seconds')
