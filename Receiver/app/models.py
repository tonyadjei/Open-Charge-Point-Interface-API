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
    id: UUID
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


class UpdateSession(BaseModel):
    country_code: Optional[str]
    party_id: Optional[str]
    start_date_time: Optional[datetime]
    end_date_time: Optional[datetime]
    kwh: Optional[float]
    cdr_token: Optional[CdrToken]
    auth_method: Optional[AuthMethod] 
    authorization_reference: Optional[str]
    location_id: Optional[UUID]
    evse_uid: Optional[UUID]
    connector_id: Optional[UUID] 
    meter_id: Optional[str]
    currency: Optional[str]
    charging_periods: Optional[List[ChargingPeriod]]
    total_cost: Optional[Price]
    status: Optional[SessionStatus]
    # PATCH requests must always have a value for the 'last_updated' field
    last_updated: datetime