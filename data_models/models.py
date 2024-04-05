from sqlalchemy import  Column, String, DateTime, Boolean, Integer, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class AlertsConfigModel(Base):
    __tablename__ = "bot_agility_alerts_config"

    id = Column(Integer(), primary_key=True, index=True)
    tittle = Column(String(length=255))
    description = Column(Text())
    url_webhook = Column(String(length=255))
    team = Column(String(length=255))
    group_id = Column(String(length=255))
    created_at = Column(DateTime())
    updated_at = Column(DateTime())
    type_incident_notification = Column(String(length=255))
    days_incident_notification = Column(String(length=255))
    hour_incident_notification = Column(String(length=255))
    status = Column(Boolean()) 

    def __init__(
        self, tittle:str, description:str, url_webhook, team, group_id, created_at, updated_at, type_incident_notification, days_incident_notification, hour_incident_notification, status
    ):
        self.tittle = tittle
        self.description = description
        self.url_webhook = url_webhook
        self.team = team
        self.group_id = group_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.type_incident_notification = type_incident_notification
        self.days_incident_notification = days_incident_notification
        self.hour_incident_notification = hour_incident_notification
        self.status = status