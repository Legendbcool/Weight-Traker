import sys
print('What is your height?')
while True:
    feet=int(input('Feet:'))

    if feet ==5:
        print('')
        break
            
    else:
           print(feet, 'Feet is',  'Not Avaliable!')
           sys.exit()
          


inches= int(input('Inches:'))
print(' What is your weight?')
weight= int(input(' Weight:'))
     
if inches ==0:
    if weight in range(97,127):
        print('healthy weight !')
if inches == 0:
 if weight <97:
        print('under weight !')

if inches == 0:
 if weight > 127:
        print('over weight !')
        sys.exit()


elif inches== 1:
          if weight in range(100, 132):
              print('healthy weight!')

          if inches ==1:
            if weight <100:
                print('under weight !')
          if inches ==1:
            if weight >132:
                print('over weight !')
                sys.exit()

elif inches ==2:
    if weight in range(104, 136):
        print('healthy weight !')

    if inches ==2:
      if weight < 104:
          print('under weight !')
    if inches ==2:
      if weight > 136:
          print('over weight!')
          sys.exit()


elif inches ==3:
    if weight in range(107,140):
        print('healthy weight !')

    if inches==3:
      if weight <107:
          print('under weight !')
    if inches ==3:
      if weight > 140:
          print('over weight !')
          sys.exit()

elif inches ==4:
    if weight in range(110,145):
        print('healthy weight !')

    if inches ==4:
        if weight <110:
            print('under weight!')
    if inches ==4:
        if weight > 145:
            print('over weight !')
            sys.exit()

elif inches ==5:
    if weight in range(114,149):
        print('healthy weight !')

    if inches ==5:
        if weight <114:
            print('under weight!')
    if inches ==5:
        if weight > 149:
            print('over weight !')
            sys.exit()


            
elif inches ==6:
    if weight in range(118,154):
        print('healthy weight !')


    if inches ==6:
        if weight <118:
            print('under weight!')
    if inches ==6:
        if weight > 154:
            print('over weight !')
            sys.exit()



elif inches ==7:
    if weight in range(121,159):
        print('healthy weight !')

    if inches ==7:
        if weight <121:
            print('under weight!')
    if inches ==7:
        if weight > 159:
            print('over weight !')
            sys.exit()



elif inches ==8:
    if weight in range(125,164):
        print('healthy weight !')

    if inches ==8:
        if weight <125:
            print('under weight!')
    if inches ==8:
        if weight > 164:
            print('over weight !')
            sys.exit()



elif inches ==9:
    if weight in range(128,168):
        print('healthy weight !')

    if inches ==9:
        if weight <128:
            print('under weight!')
    if inches ==9:
        if weight > 168:
            print('over weight !')
            sys.exit()




elif inches ==10:
    if weight in range(132,173):
        print('healthy weight !')

    if inches ==10:
        if weight <132:
            print('under weight!')
    if inches ==10:
        if weight > 173:
            print('over weight !')
            sys.exit()
else:
    print('Calculation Not Is Avaliable!')
    sys.exit




         
            








    
         
