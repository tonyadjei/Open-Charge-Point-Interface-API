from .models import Session, AuthMethod, TokenType, CdrToken, Price
from typing import List
from uuid import uuid4, UUID
from datetime import datetime


# Dummy list of Session objects for testing purposes
sessions_db: List[Session] = [
    Session(
        country_code="FR",
        party_id="331",
        id=UUID("b8f41d84-ccab-4b65-957d-793826193e78"),
        start_date_time=datetime.now(),
        end_date_time=datetime.now(),
        kwh=156.77,
        cdr_token=CdrToken(
            country_code="FR",
            party_id="331",
            uid=uuid4(),
            type=TokenType.RFID,
            contract_id=uuid4()
        ),
        auth_method=AuthMethod.COMMAND,
        authorization_reference="XRAUTHREF",
        location_id=uuid4(),
        currency="EUR",
        total_cost= Price(
            excl_vat=16.99,
            incl_vat=22.99
        ),        
        last_updated=datetime.now()
    ),
    Session(
        country_code="BE",
        party_id="541",
        id=UUID("b8f32d84-ccab-4b65-677d-399826193e54"),
        start_date_time=datetime.now(),
        end_date_time=datetime.now(),
        kwh=232.11,
        cdr_token=CdrToken(
            country_code="BE",
            party_id="541",
            uid=uuid4(),
            type=TokenType.RFID,
            contract_id=uuid4()
        ),
        auth_method=AuthMethod.COMMAND,
        authorization_reference="XFFAUTHREF",
        location_id=uuid4(),
        currency="EUR",
        total_cost= Price(
            excl_vat=3.99,
            incl_vat=5.99
        ),        
        last_updated=datetime.now()
    ),
    Session(
        country_code="DE",
        party_id="684",
        id=UUID("b6f32d84-ccab-4b65-229d-599826193e54"),
        start_date_time=datetime.now(),
        end_date_time=datetime.now(),
        kwh=134.52,
        cdr_token=CdrToken(
            country_code="DE",
            party_id="684",
            uid=uuid4(),
            type=TokenType.RFID,
            contract_id=uuid4()
        ),
        auth_method=AuthMethod.COMMAND,
        authorization_reference="XVAUTHSPE",
        location_id=uuid4(),
        currency="EUR",
        total_cost= Price(
            excl_vat=1.99,
            incl_vat=2.99
        ),        
        last_updated=datetime.now()
    ),
    Session(
        country_code="PL",
        party_id="223",
        id=UUID("b8f32d84-ccab-4b65-433d-699826193a21"),
        start_date_time=datetime.now(),
        end_date_time=datetime.now(),
        kwh=200.99,
        cdr_token=CdrToken(
            country_code="PL",
            party_id="223",
            uid=uuid4(),
            type=TokenType.RFID,
            contract_id=uuid4()
        ),
        auth_method=AuthMethod.COMMAND,
        authorization_reference="ESCXAUTH",
        location_id=uuid4(),
        currency="EUR",
        total_cost= Price(
            excl_vat=19.99,
            incl_vat=20.99
        ),        
        last_updated=datetime.now()
    )
]