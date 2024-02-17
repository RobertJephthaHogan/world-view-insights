import datetime
from typing import Dict, Optional, Any, Union
from fastapi import File, UploadFile
from beanie import Document
from pydantic import BaseModel, EmailStr, Field


class FormFour(Document):
    id: Optional[str] = Field(...)
    schemaVersion: str = Field(...)
    documentType: str = Field(...)
    periodOfReport: str = Field(...)
    notSubjectToSection16: bool = Field(...)
    issuerName: str = Field(...)
    issuerCik: str = Field(...)
    issuerTradingSymbol: str = Field(...)
    issuerStockQuote: str = Field(...)
    issuerMarketCap: str = Field(...)
    rptOwnerCik: str = Field(...)
    rptOwnerName: str = Field(...)
    isDirector: bool = Field(...)
    isOfficer: bool = Field(...)
    isTenPercentOwner: bool = Field(...)
    isOther: bool = Field(...)
    officerTitle: str = Field(...)
    otherTitle: str = Field(...)
    nonDerivativeTable: Dict[Any, Any] = Field(...)
    derivativeTable: Dict[Any, Any] = Field(...)
    
    
    class Settings:
        name = "FormFour"

    class Config:
        schema_extra = {
            "example": {
                "id": "6382e2abc07256ef099af572",
                "schemaVersion": "version",
                "documentType": "4",
                "periodOfReport": "period",
                "notSubjectToSection16": False,
                "issuerName": "name",
                "issuerCik": "123456",
                "issuerTradingSymbol": "AAAA",
                "issuerStockQuote": "123.42",
                "issuerMarketCap": "123.42B",
                "rptOwnerCik": "123456",
                "rptOwnerName": "name",
                "isDirector": True,
                "isOfficer": True,
                "isTenPercentOwner": True,
                "isOther": True,
                "officerTitle": "title",
                "otherTitle": "title",
                "nonDerivativeTable": {},
                "derivativeTable": {},
            }
        }


class UpdateFormFourModel(BaseModel):
    id: Optional[str]
    schemaVersion: Optional[str]
    documentType: Optional[str]
    periodOfReport: Optional[str]
    notSubjectToSection16: Optional[bool]
    issuerName: Optional[str]
    issuerCik: Optional[str]
    issuerTradingSymbol: Optional[str]
    issuerStockQuote: Optional[str]
    issuerMarketCap: Optional[str]
    rptOwnerCik: Optional[str]
    rptOwnerName: str = Field(...)
    isDirector: Optional[bool]
    isOfficer: Optional[bool]
    isTenPercentOwner: Optional[bool]
    isOther: Optional[bool]
    officerTitle: Optional[str]
    otherTitle: Optional[str]
    nonDerivativeTable: Optional[Dict[Any, Any]]
    derivativeTable: Optional[Dict[Any, Any]]
    
    

    class Config:
        schema_extra = {
            "example": {
                "id": "6382e2abc07256ef099af572",
                "schemaVersion": "version",
                "documentType": "4",
                "periodOfReport": "period",
                "notSubjectToSection16": False,
                "issuerName": "name",
                "issuerCik": "123456",
                "issuerTradingSymbol": "AAAA",
                "issuerStockQuote": "123.42",
                "issuerMarketCap": "123.42B",
                "rptOwnerCik": "123456",
                "rptOwnerName": "name",
                "isDirector": True,
                "isOfficer": True,
                "isTenPercentOwner": True,
                "isOther": True,
                "officerTitle": "title",
                "otherTitle": "title",
                "nonDerivativeTable": {},
                "derivativeTable": {},
            }
        }

