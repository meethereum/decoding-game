import random
print('Welcome to Mastermind. This is a game where your intuition and logic '
	'will be tested on the basis of a simple decoding came which '
	'involves cracking of a 4 digit secret code. \n You will be given '
	'10 chances to guess the code but there will be indicators '
	'telling you to what extent your guess is correct: \n :) means '
	'one of your guesses is correct and also correctly placed. \n :| '
	'means one of your guesses is correct but it is incorrectly '
	'placed \n :( means one of your guesses is completely wrong \n'
	'You will get 4 indicators for every guess. Try not to repeat '
	'numbers. Cheers! \n')
	


wrongList=[]
correctList=[]
partially_correctList=[]
correct=0
wrong=0
partially_correct=0
codeList=['']
test_list=[]
code=str(random.randint(1000,9999))
number = code
while len(number)!= len(set(number)):
    number=list(set(number))
        
    n = 4 - len(number)
    extra_digits=str(random.randrange(10*(n-1),10*n))
    extra_digitsList=list(extra_digits)
        
    for item in extra_digitsList:
            number.append(item)
    code=str(number)   
        
i = 0
while i<10:
    i+=1
    if test_list== codeList:
        print("CONGRATULATIONS. YOU CRACKED THE CODE TO BECOME THE MASTERMIND!")
        break
    
    user_guess=input('Enter your guess to crack the code: ')
    user_guessList=list(user_guess)
    test_list=list(user_guess)

    res = ''  
    for idx in range(len(test_list)-1):
        res = res + test_list[idx] 
    if len(test_list) > 0:
            res = res + test_list[-1]
    res = [res]
    user_guess=list(res)
    codeList=list(code)

    for guess,codes in zip(user_guessList, codeList):

           
            
            if guess not in code:
               wrongList.append(guess)
               
    for guess,codes in zip(test_list, codeList):
        
            if guess in code and test_list.index(guess) != codeList.index(guess): 
                partially_correctList.append(guess)
                
                

            if guess in code and test_list.index(guess) == codeList.index(guess):
                correctList.append(guess)
                
                
    print( ':) ' * len(correctList),':| ' *  len(partially_correctList) , ':( ' * len(wrongList), i)
    wrongList=[]
    correctList=[]
    partially_correctList=[]
    if i==10 and test_list!= codeList:
        print('GAME OVER!')
    
             
       
        
           
          
  
print('The correct secret code is ' + code)
        
