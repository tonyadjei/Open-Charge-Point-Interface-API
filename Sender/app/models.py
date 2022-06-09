from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4
from datetime import datetime
from enum import Enum

# The following classes represent models of the objects in the Sessions module 

class TokenType(str, Enum):
    AD_HOC_USER = "AD_HOC_USER"
    APP_USER = "APP_USER"
    OTHER = "OTHER"
    RFID = "RFID"

class CdrToken(BaseModel):
    country_code: str
    party_id: str
    uid: UUID = uuid4()
    type: TokenType
    contract_id: UUID = uuid4()

class Price(BaseModel):
    excl_vat: float
    incl_vat: float

class AuthMethod(str, Enum):
    AUTH_REQUEST = "AUTH_REQUEST"
    COMMAND = "COMMAND"
    WHITELIST = "WHITELIST"

class ChargingPeriod(BaseModel):
    start_date_time: datetime
    dimensions: str
    tarrif_id: UUID = uuid4()

class SessionStatus(str, Enum):
    ACTIVE = "ACTIVE"
    COMPLETED = "COMPLETED"
    INVALID = "INVALID"
    PENDING = "PENDING"
    RESERVATION = "RESERVATION"


class Session(BaseModel):
    country_code: str
    party_id: str
    id: Optional[UUID] = uuid4()
    start_date_time: datetime
    end_date_time: datetime
    kwh: float
    cdr_token: CdrToken
    auth_method: AuthMethod 
    authorization_reference: str
    location_id: UUID = uuid4()
    evse_uid: UUID = None
    connector_id: UUID = None
    meter_id: Optional[str]
    currency: str
    charging_periods: Optional[List[ChargingPeriod]]
    total_cost: Price
    status: SessionStatus = SessionStatus.PENDING
    last_updated: datetime


class ProfileType(str, Enum):
    CHEAP = "CHEAP"
    FAST = "FAST"
    GREEN = "GREEN"
    REGULAR = "REGULAR"

class ChargingPreferences(BaseModel):
    profile_type: ProfileType
    departure_time: datetime
    energy_need: float
    discharge_allowed: bool = False

class ChargingPreferencesResponse(str, Enum):
    ACCEPTED = "ACCEPTED"
    DEPARTURE_REQUIRED = "DEPARTURE_REQUIRED"
    ENERGY_NEED_REQUIRED = "ENERGY_NEED_REQUIRED"
    NOT_POSSIBLE = "NOT_POSSIBLE"
    PROFILE_TYPE_NOT_SUPPORTED = "PROFILE_TYPE_NOT_SUPPORTED"