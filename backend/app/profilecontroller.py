from fastapi import APIRouter
import json
from bson import json_util
# from ..configs.mongoconnect import connectMongoClient
from .models import Profile,MeetingDto
from .configs.mongoconnect import connectMongoClient

router = APIRouter(prefix="/profiles")  

db = connectMongoClient()
collection = db['test']

@router.get('/')
def getProfiles():
    
    """Gets all profile details

    Parameters:
    None

    Returns:
    Json with Profiles"""
    
    profile_list = []
    profile_results = collection.find()

    for profiles in profile_results:
        profile_list.append(json.loads(json_util.dumps(profiles)))
    
    return profile_list


@router.get('/{profile_email}')
def getProfileByProfileId(profile_email : str):
    """Gets all profile details of user with given profile_email

    Parameters:
    str: profile_email

    Returns:
    Json with Profile details """

    profile_result = collection.find_one({"email":profile_email})

    profile = json.loads(json_util.dumps(profile_result))
    
    return profile

@router.post('/')
def postNewProfile(profile : Profile):
    
    """Gets all profile details of user with given profile_email

    Parameters:
    str: profile_email

    Returns:
    Json with Profile details """
    
    profile_email = profile.email
    profile_query = collection.find({"email":profile_email})
    profile_query = [item for item in profile_query]

    if not profile_query : 
        collection.save(dict(profile))
        return True

    return False


@router.post("/add_meeting")
def add_meeting(meetingDto : MeetingDto):
    email = meetingDto.profile_email
    meeting_id = meetingDto.meeting_id
    collection.update({"email":email},{"$push":{"meeting_id_list":meeting_id}})
    
    return True
    


@router.delete('/{profile_email}',status_code=200)
def deleteProfileById(profile_email : str):
    """Deletes all profile details of user with given profile_email

    Parameters:
    str: profile_email

    Returns:
    Bool: Success of deletion """
    
    result = collection.delete_one({"email":profile_email})
    
    return result.acknowledged
