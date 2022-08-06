from datetime import datetime,timedelta
from copy import deepcopy

class TokenSchema:
    public_id = str
    exp = datetime
    def __init__(self,_public_id:str="",_exp:datetime =datetime.utcnow() + timedelta(minutes=45)):
        self.public_id =_public_id
        self.exp=_exp
  
    @property
    def serialize(self):
        return {
            "public_id":self.public_id,
            "exp":self.exp
        }
    
    def fromDict(self,dict:dict):
        self.public_id=dict['public_id']
        self.exp=dict['exp']
        return deepcopy(self)

