class TeamLeader(TeamMember,Worker):
    def __init__(self,name,uid,pay,jobtitle,exp):
        self.exp=exp
        TeamMember.__init__(self,name,uid)
        Worker.__init__self(self,pay,jobtitle)
        print("Name:{},Pay:{},Exp:{}".format(self.name,self.pay.self.exp))
T=TeamLeader('jake',10001,25000,'ScrumMaster',5)
print(TeamLeader.mro())
