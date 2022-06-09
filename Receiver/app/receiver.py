from datetime import datetime
from uuid import UUID
from fastapi import FastAPI, HTTPException, Path, status
from .models import Session, UpdateSession
from .data import sessions_db


# This is the RECEIVER INTERFACE: Typically implemented by market roles like: eMSP and SCSP.
app = FastAPI()


@app.get("/sessions/{country_code}/{party_id}/{session_id}", tags=["Sessions"], status_code=status.HTTP_200_OK)
async def get_session(*, country_code: str = Path(..., max_length=2, min_length=2), party_id: str = Path(..., max_length=3, min_length=3), session_id: UUID):
    # check if session with id <session_id> exists
    for session in sessions_db:
        if session.id == session_id and session.country_code == country_code and session.party_id == party_id:
            return {
                "data": session,
                "status_code": 1000,
                "status_message": "Successful Operation.",
                "timestamp": datetime.now()
            }
    # if no session was found with the given credentials, raise an HttpException error
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No Session with ID {session_id} | Country code {country_code} | Party ID {party_id} was found.")


@app.put("/sessions/{country_code}/{party_id}/{session_id}", tags=["Sessions"], status_code=status.HTTP_201_CREATED)
async def create_update_session(*, country_code: str = Path(..., max_length=2, min_length=2), party_id: str = Path(..., max_length=3, min_length=3), session_id: UUID, session: Session):
    global sessions_db
    # check if session_id already exists, then update existing session
    for db_session in sessions_db:
        if db_session.id == session_id and db_session.country_code == country_code and db_session.party_id == party_id:
            db_session.country_code = session.country_code
            db_session.party_id = session.party_id
            db_session.id = session.id
            db_session.start_date_time = session.start_date_time
            db_session.end_date_time = session.end_date_time
            db_session.kwh = session.kwh
            db_session.cdr_token = session.cdr_token
            db_session.auth_method = session.auth_method
            db_session.authorization_reference = session.authorization_reference
            db_session.location_id = session.location_id
            db_session.evse_uid = session.evse_uid
            db_session.connector_id = session.connector_id
            db_session.meter_id = session.meter_id
            db_session.currency = session.currency
            db_session.charging_periods = session.charging_periods
            db_session.total_cost = session.total_cost
            db_session.status = session.status
            db_session.last_updated = session.last_updated

            return {
                "data": db_session,
                "status_code": 1000,
                "status_message": f"Succesfully updated session with ID {session_id}.",
                "timestamp": datetime.now()
            }
    # if ID exists but country_code or party_id does not match, raise an error
    for db_session in sessions_db:
        if db_session.id == session_id and (db_session.country_code != country_code or db_session.party_id != party_id):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"The Country Code {country_code} and/or Party ID {party_id} does not match session with ID {session_id}.")
    # if session_id does not exist, then we add it to the db as a new session object
    sessions_db.append(session)
    return {
        "data": session,
        "status_code": 1000,
        "status_message": f"Successfully created session with ID {session_id}.",
        "timestamp": datetime.now()
    }


@app.patch("/sessions/{country_code}/{party_id}/{session_id}", tags=["Sessions"], status_code=status.HTTP_200_OK)
async def patch_session(*, country_code: str = Path(..., max_length=2, min_length=2), party_id: str = Path(..., max_length=3, min_length=3), session_id: UUID, session: UpdateSession):
    global sessions_db
    for db_session in sessions_db:
        if db_session.id == session_id and db_session.country_code == country_code and db_session.party_id == party_id:
            db_session.country_code = session.country_code if session.country_code else db_session.country_code
            db_session.party_id = session.party_id if session.party_id else db_session.party_id
            db_session.start_date_time = session.start_date_time if session.start_date_time else db_session.start_date_time
            db_session.end_date_time = session.end_date_time  if session.end_date_time else db_session.end_date_time
            db_session.kwh = session.kwh if session.kwh else db_session.kwh
            db_session.cdr_token = session.cdr_token if session.cdr_token else db_session.cdr_token
            db_session.auth_method = session.auth_method if session.auth_method else db_session.auth_method
            db_session.authorization_reference = session.authorization_reference if session.authorization_reference else db_session.authorization_reference
            db_session.location_id = session.location_id if session.location_id else db_session.location_id
            db_session.evse_uid = session.evse_uid if session.evse_uid else db_session.evse_uid
            db_session.connector_id = session.connector_id if session.connector_id else db_session.connector_id
            db_session.meter_id = session.meter_id if session.meter_id else db_session.meter_id
            db_session.currency = session.currency if session.currency else db_session.currency
            if session.charging_periods:
                if db_session.charging_periods:
                    for charging_period in session.charging_periods:
                        db_session.charging_periods.append(charging_period)
                else:
                    db_session.charging_periods = session.charging_periods
            db_session.total_cost = session.total_cost if session.total_cost else db_session.total_cost
            db_session.status = session.status if session.status else db_session.status
            db_session.last_updated = session.last_updated if session.last_updated else db_session.last_updated
            return {
                "data": db_session,
                "status_code": 1000,
                "status_message": f"Session with ID {session_id} updated successfully.",
                "timestamp": datetime.now()
            }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No Session with ID {session_id} | Country code {country_code} | Party ID {party_id} was found.")
    