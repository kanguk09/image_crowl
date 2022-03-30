import os
 
def changeName(path, cName):
    i = 1
    for filename in os.listdir(path):
        print(path+filename, '=>', path+str(cName)+str(i)+'.pdf')
        os.rename(path+filename, path+str(cName)+str(i)+'.pdf')
        i += 1
 
changeName('C:/Users/kangu/Desktop/취업준비/반도체 강의자료/download/','반도체 제조 공정 part1_')


