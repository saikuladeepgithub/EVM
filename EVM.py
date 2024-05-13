class EVM:
    def __init__(self,numofcandidates):
        self.numofcandidates=numofcandidates
        self.votes=[0]*numofcandidates
        self.total_votes=0
        self.ycp=0
        self.tdp=0
        self.nota=0
    def castevote(self,serialno):
        if(serialno>=1 and serialno<=self.numofcandidates):
            if(self.votes[serialno-1]==0):
                self.votes[serialno-1]=1
                self.total_votes+=1
                v=int(input("Enter 1 for ycp,2 for tdp : "))
                if(v==1):
                    self.ycp=self.ycp+1
                elif(v==2):
                    self.tdp=self.tdp+1
                else:
                    self.nota=self.nota+1
                print(f"The serial number {serialno} is voted")
            else:
                print("You already casted vote.... Vote in next elections")
        else:
            print("Invalid voter serial number ")
    def display(self):
        print("The total number of votes casted are ",self.total_votes)
    def pollrate(self):
        per=(self.total_votes/self.numofcandidates)*100
        print("The voters percntage who casted their vote is :",per)
    def results(self):
        print("The tdp votes are :",self.tdp)
        print("The ycp votes are :",self.ycp)
        if(self.ycp>self.tdp):
            print("Ycp won by majority",self.ycp-self.tdp)
        elif(self.ycp<self.tdp):
            print("The tdp won by majority :",self.tdp-self.ycp)
        else:
            print("The both parties got same votes ")
evm=EVM(4)
print("The polling has started....")
while evm.total_votes<=evm.numofcandidates:
    sno=int(input("Enter voter id serial number :"))
    evm.castevote(sno)
    if(evm.total_votes==evm.numofcandidates):
        break
    else:
        b=input("Enter 'c' to continue or '0' to stop :")
        if(b=='0'):
            break
        else:
            continue
    
evm.pollrate()
evm.display()
evm.results()