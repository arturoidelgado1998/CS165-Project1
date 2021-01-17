import os 
import multiprocessing
def subfunction(textfile, directory):
    os.chdir("c:/Users/artur/OneDrive/Documents/GitHub/CS165-project1/"+ directory)
    
    f = open(textfile, "r")
    for l in f:
        print(l.strip())
    
    f.close()




def listn(directory):
     for every in os.listdir("c:/Users/artur/OneDrive/Documents/GitHub/CS165-project1/" + directory ):
        subfunction(every,directory)
        os.remove("c:/Users/artur/OneDrive/Documents/GitHub/CS165-project1/"+directory+"/"+every)
    


if __name__ == '__main__':

    process1 = multiprocessing.Process(target= listn, args =("testprocess",))
    process2 = multiprocessing.Process(target= listn, args =("testprocess2",))
    process1.start()
    process2.start()
    
    
