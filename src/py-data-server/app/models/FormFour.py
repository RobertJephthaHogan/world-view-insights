import datetime
from typing import Dict, Optional, Any, Union
from fastapi import File, UploadFile
from beanie import Document
from pydantic import BaseModel, EmailStr, Field


class FormFour(Document):
    id: Optional[str] = Field(...)
    cikAccessionId: Optional[str] = Field(...)
    schemaVersion: str = Field(...)
    documentType: str = Field(...)
    periodOfReport: str = Field(...)
    notSubjectToSection16: bool = Field(...)
    issuerName: str = Field(...)
    issuerCik: str = Field(...)
    issuerTradingSymbol: str = Field(...)
    issuerStockQuote: Union[str, int, float] = Field(...)
    issuerMarketCap: Union[str, int, float] = Field(...)
    rptOwnerCik: str = Field(...)
    rptOwnerName: str = Field(...)
    isDirector: bool = Field(...)
    isOfficer: bool = Field(...)
    isTenPercentOwner: bool = Field(...)
    isOther: bool = Field(...)
    officerTitle: str = Field(...)
    otherTitle: str = Field(...)
    link: str = Field(...)
    totalTransactionShares: Union[str, int, float] = Field(...)
    transactionPrice: Union[str, int, float] = Field(...)
    totalTransactionSize: Union[str, int, float] = Field(...)
    transactionType: str = Field(...)
    securityTitle: str = Field(...)
    nonDerivativeTable: Dict[Any, Any] = Field(...)
    derivativeTable: Dict[Any, Any] = Field(...)
    
    
    class Settings:
        name = "FormFour"

    class Config:
        json_schema_extra = {
            "example": {
                "id": "6382e2abc07256ef099af572",
                "cikAccessionId": "123456-123123123123123123123",
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
                "link": "https://example.com",
                "totalTransactionShares": "",
                "transactionPrice": "",
                "totalTransactionSize": "",
                "transactionType": "P",
                "securityTitle": "Common Stock",
                "nonDerivativeTable": {},
                "derivativeTable": {},
            }
        }


class UpdateFormFourModel(BaseModel):
    id: Optional[str]
    cikAccessionId: Optional[str]
    schemaVersion: Optional[str]
    documentType: Optional[str]
    periodOfReport: Optional[str]
    notSubjectToSection16: Optional[bool]
    issuerName: Optional[str]
    issuerCik: Optional[str]
    issuerTradingSymbol: Optional[str]
    issuerStockQuote: Optional[Union[str, int, float]]
    issuerMarketCap: Optional[Union[str, int, float]]
    rptOwnerCik: Optional[str]
    rptOwnerName: str = Field(...)
    isDirector: Optional[bool]
    isOfficer: Optional[bool]
    isTenPercentOwner: Optional[bool]
    isOther: Optional[bool]
    link: Optional[str]
    totalTransactionShares: Optional[Union[str, int, float]]
    transactionPrice: Optional[Union[str, int, float]]
    totalTransactionSize: Optional[Union[str, int, float]]
    officerTitle: Optional[str]
    otherTitle: Optional[str]
    transactionType: Optional[str]
    securityTitle: Optional[str]
    nonDerivativeTable: Optional[Dict[Any, Any]]
    derivativeTable: Optional[Dict[Any, Any]]
    
    

    class Config:
        json_schema_extra = {
            "example": {
                "id": "6382e2abc07256ef099af572",
                "cikAccessionId": "123456-123123123123123123123",
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
                "link": "https://example.com",
                "totalTransactionShares": "",
                "transactionPrice": "",
                "totalTransactionSize": "",
                "otherTitle": "title",
                "transactionType": "P",
                "securityTitle": "Common Stock",
                "nonDerivativeTable": {},
                "derivativeTable": {},
            }
        }

