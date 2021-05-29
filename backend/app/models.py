from fastapi.params import File
from pydantic import BaseModel

class Profile(BaseModel):
    email:str
    user_name:str
    description : str
    birth_date : str
    name : str
    wallet_amt : int
    rating : int
    total_debates_attended : int
    
class Report(BaseModel):
    reportForUser1 : str
    reportForUser2 : str


class SessionDetails(BaseModel):
    session_id : int
    anonymous_name_1 : str
    anonymous_name_2 : str
    user_1_email : str
    user_2_email : str
    report : Report
    




