from datetime import datetime
from fastapi import FastAPI, Query, status, HTTPException
from .data import sessions_db
from uuid import UUID
from .models import ChargingPreferences, ChargingPreferencesResponse, ProfileType

# This is the SENDER INTERFACE: Typically implemented by market roles like: CPO.
app = FastAPI()


@app.get("/sessions", tags=["Sessions"], status_code=status.HTTP_200_OK)
async def get_all_sessions(*, date_from: datetime, date_to: datetime = Query(None), offset: int = Query(0, ge=0), limit: int = Query(0, ge=0)):
    if offset >= len(sessions_db):
        return {"data": {}, "status_code": 2001, "status_message": f"Offset value {offset} must be less than {len(sessions_db)}.", "timestamp": datetime.now()}
    if limit > len(sessions_db):
        return {"data": {}, "status_code": 2001, "status_message": f"Limit value {limit} must be less than or equal to {len(sessions_db)}.", "timestamp": datetime.now()}
    # return <limit> number of sessions, offset by <offset> if applicable
    counter = 0
    matching_sessions = []
    # assign date_to to the current date/time if it does not exist
    date_to = datetime.now() if date_to == None else date_to
    # if no limit is specified, we retrieve all possible matching sessions in the db
    limit = len(sessions_db) if limit == 0 else limit
    for i in range(offset, len(sessions_db)):
        session = sessions_db[i]
        if session.last_updated >= date_from and session.last_updated < date_to:
            matching_sessions.append(session)
            counter += 1
        # break if we reach the <limit> value
        if counter == limit:
            break
    return {"data": matching_sessions, "status_code": 1000, "status_message": "Successful operation.", "timestamp": datetime.now() }



@app.put("/sessions/{session_id}/charging_preferences", tags=["Sessions"], status_code=status.HTTP_200_OK)
async def update_session(session_id: UUID, charging_preferences: ChargingPreferences):
    # check if sessions_id exists in the db
    for session in sessions_db:
        if session.id == session_id:
            # implement some dummy checks to send appropriate ChargingPreferencesResponse
            if charging_preferences.profile_type is ProfileType.CHEAP:
                response = ChargingPreferencesResponse.NOT_POSSIBLE
            elif charging_preferences.profile_type is ProfileType.FAST:
                response = ChargingPreferencesResponse.PROFILE_TYPE_NOT_SUPPORTED
            elif charging_preferences.profile_type is ProfileType.GREEN:
                response = ChargingPreferencesResponse.ACCEPTED
            else:
                response = ChargingPreferencesResponse.ACCEPTED
            return {"data": response, "status_code": 1000, "status_message": f"Charging Preferences for Session with ID {session_id} has been updated.", "timestamp": datetime.now()}
    # if no id with session_id is found, raise an HttpException
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Session with ID {session_id} was not found.")