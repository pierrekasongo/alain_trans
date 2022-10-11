from sqlalchemy import Column, DateTime, ForeignKey, Integer, Numeric, String, UniqueConstraint,Text, text
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class Bus(Base):
    __tablename__ = 'bus'

    id = Column(UUID, primary_key=True, server_default=text("uuid_generate_v4()"))
    created_at = Column(DateTime(True), server_default=text("now()"))
    updated_at = Column(DateTime(True), server_default=text("now()"))
    plaque = Column(String, unique=True)
    nbre_place = Column(Integer)
    prix_place = Column(Numeric)

class Depart(Base):
    __tablename__ = 'depart'

    id = Column(UUID, primary_key=True, server_default=text("uuid_generate_v4()"))
    created_at = Column(DateTime(True), server_default=text("now()"))
    updated_at = Column(DateTime(True), server_default=text("now()"))
    date_heure = Column(DateTime(True))
    destination_fk = Column(ForeignKey("destination.id"))

    destination = relationship("Destination")

class Ticket(Base):
    __tablename__ = 'ticket'

    id = Column(UUID, primary_key=True, server_default=text("uuid_generate_v4()"))
    created_at = Column(DateTime(True), server_default=text("now()"))
    updated_at = Column(DateTime(True), server_default=text("now()"))
    passager = Column(String)
    telephone = Column(String)
    destination = Column(String)
    etat = Column(String)
    bus_fk = Column(ForeignKey('bus.id'))
    utilisateur_fk = Column(ForeignKey('utilisateur.id'))
    depart_fk = Column(ForeignKey('depart.id'))

    bus = relationship("Bus")
    utilisateur = relationship("Utilisateur")
    depart = relationship("Depart")

class Destination(Base):
    __tablename__ = 'destination'

    id = Column(UUID, primary_key=True, server_default=text("uuid_generate_v4()"))
    created_at = Column(DateTime(True), server_default=text("now()"))
    updated_at = Column(DateTime(True), server_default=text("now()"))
    nom = Column(String)


class Utilisateur(Base):
    __tablename__ = 'utilisateur'

    id = Column(UUID, primary_key=True, server_default=text("uuid_generate_v4()"))
    created_at = Column(DateTime(True), server_default=text("now()"))
    updated_at = Column(DateTime(True), server_default=text("now()"))
    nom = Column(String)
    login = Column(String)
    mot_de_passe = Column(String)
    role = Column(String)
    etat = Column(String)
    