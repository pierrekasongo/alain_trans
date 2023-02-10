from sqlalchemy import Column, DateTime, ForeignKey, Integer, Numeric,Boolean,String, UniqueConstraint,Text, text
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class Vehicule(Base):
    __tablename__ = 'vehicule'

    id = Column(UUID, primary_key=True, server_default=text("uuid_generate_v4()"))
    created_at = Column(DateTime(True), server_default=text("now()"))
    updated_at = Column(DateTime(True), server_default=text("now()"))
    plaque = Column(String, unique=True)
    nbre_place = Column(Integer)
    designation = Column(String)
    partenaire = Column(Boolean, unique=False, default=False)

    def __repr__(self):
        return f'<Vehicule {self.id} ({self.plaque} {self.nbre_place})>'


class Depart(Base):
    __tablename__ = 'depart'

    id = Column(UUID, primary_key=True, server_default=text("uuid_generate_v4()"))
    created_at = Column(DateTime(True), server_default=text("now()"))
    updated_at = Column(DateTime(True), server_default=text("now()"))
    date_heure = Column(DateTime(True))
    destination_fk = Column(ForeignKey("destination.id"))
    vehicule_fk = Column(ForeignKey("vehicule.id"))

    vehicule = relationship("Vehicule")
    destination = relationship("Destination")


class Ticket(Base):
    __tablename__ = 'ticket'

    id = Column(UUID, primary_key=True, server_default=text("uuid_generate_v4()"))
    created_at = Column(DateTime(True), server_default=text("now()"))
    updated_at = Column(DateTime(True), server_default=text("now()"))
    code = Column(String)
    passager = Column(String)
    telephone = Column(String)
    etat = Column(String)
    utilisateur_fk = Column(ForeignKey('utilisateur.id'))
    depart_fk = Column(ForeignKey('depart.id'))
    
    utilisateur = relationship("Utilisateur")
    depart = relationship("Depart")

class Colis(Base):
    __tablename__ = 'colis'
    id = Column(UUID, primary_key=True, server_default=text("uuid_generate_v4()"))
    created_at = Column(DateTime(True), server_default=text("now()"))
    updated_at = Column(DateTime(True), server_default=text("now()"))
    date_retrait = Column(DateTime(True))
    designation = Column(String)
    poids = Column(String)
    code = Column(String)
    prix = Column(Numeric)
    retire_par = Column(String)
    telephone = Column(String)




class Destination(Base):
    __tablename__ = 'destination'

    id = Column(UUID, primary_key=True, server_default=text("uuid_generate_v4()"))
    created_at = Column(DateTime(True), server_default=text("now()"))
    updated_at = Column(DateTime(True), server_default=text("now()"))
    nom = Column(String)
    prix = Column(Integer)
    prix_promo = Column(Integer)
    en_promo = Column(Boolean)
    devise = Column(String)


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
    token = Column(String)
