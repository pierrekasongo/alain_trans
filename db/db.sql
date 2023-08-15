-- Table: public.colis

-- DROP TABLE IF EXISTS public.colis;

CREATE TABLE IF NOT EXISTS public.colis
(
    id uuid NOT NULL DEFAULT uuid_generate_v4(),
    created_at timestamp with time zone DEFAULT now(),
    updated_at timestamp with time zone DEFAULT now(),
    date_retrait timestamp with time zone,
    designation character varying COLLATE pg_catalog."default",
    poids character varying COLLATE pg_catalog."default",
    code character varying COLLATE pg_catalog."default",
    prix numeric,
    retire_par character varying COLLATE pg_catalog."default",
    telephone character varying COLLATE pg_catalog."default",
    CONSTRAINT colis_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.colis
    OWNER to alain;
    
-- Table: public.depart

-- DROP TABLE IF EXISTS public.depart;

CREATE TABLE IF NOT EXISTS public.depart
(
    id uuid NOT NULL DEFAULT uuid_generate_v4(),
    created_at timestamp with time zone DEFAULT now(),
    updated_at timestamp with time zone DEFAULT now(),
    date_heure timestamp with time zone,
    destination_fk uuid,
    vehicule_fk uuid,
    CONSTRAINT depart_pkey PRIMARY KEY (id),
    CONSTRAINT depart_destination_fk_fkey FOREIGN KEY (destination_fk)
        REFERENCES public.destination (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT depart_vehicule_fk_fkey FOREIGN KEY (vehicule_fk)
        REFERENCES public.vehicule (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.depart
    OWNER to alain;
    

-- Table: public.destination

-- DROP TABLE IF EXISTS public.destination;

CREATE TABLE IF NOT EXISTS public.destination
(
    id uuid NOT NULL DEFAULT uuid_generate_v4(),
    created_at timestamp with time zone DEFAULT now(),
    updated_at timestamp with time zone DEFAULT now(),
    nom character varying COLLATE pg_catalog."default",
    prix integer,
    devise character varying COLLATE pg_catalog."default",
    prix_promo integer,
    en_promo boolean,
    CONSTRAINT destination_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.destination
    OWNER to alain;
    
    
-- Table: public.utilisateur

-- DROP TABLE IF EXISTS public.utilisateur;

CREATE TABLE IF NOT EXISTS public.utilisateur
(
    id uuid NOT NULL DEFAULT uuid_generate_v4(),
    created_at timestamp with time zone DEFAULT now(),
    updated_at timestamp with time zone DEFAULT now(),
    nom character varying COLLATE pg_catalog."default",
    login character varying COLLATE pg_catalog."default",
    mot_de_passe character varying COLLATE pg_catalog."default",
    role character varying COLLATE pg_catalog."default",
    etat character varying COLLATE pg_catalog."default",
    token character varying COLLATE pg_catalog."default",
    CONSTRAINT utilisateur_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.utilisateur
    OWNER to alain;
    
-- Table: public.vehicule

-- DROP TABLE IF EXISTS public.vehicule;

CREATE TABLE IF NOT EXISTS public.vehicule
(
    id uuid NOT NULL DEFAULT uuid_generate_v4(),
    created_at timestamp with time zone DEFAULT now(),
    updated_at timestamp with time zone DEFAULT now(),
    plaque character varying COLLATE pg_catalog."default",
    nbre_place integer,
    designation character varying COLLATE pg_catalog."default",
    partenaire boolean,
    CONSTRAINT vehicule_pkey PRIMARY KEY (id),
    CONSTRAINT vehicule_plaque_key UNIQUE (plaque)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.vehicule
    OWNER to alain;
    
-- Table: public.ticket

-- DROP TABLE IF EXISTS public.ticket;

CREATE TABLE IF NOT EXISTS public.ticket
(
    id uuid NOT NULL DEFAULT uuid_generate_v4(),
    created_at timestamp with time zone DEFAULT now(),
    updated_at timestamp with time zone DEFAULT now(),
    code character varying COLLATE pg_catalog."default",
    passager character varying COLLATE pg_catalog."default",
    telephone character varying COLLATE pg_catalog."default",
    etat character varying COLLATE pg_catalog."default",
    utilisateur_fk uuid,
    depart_fk uuid,
    CONSTRAINT ticket_pkey PRIMARY KEY (id),
    CONSTRAINT ticket_depart_fk_fkey FOREIGN KEY (depart_fk)
        REFERENCES public.depart (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT ticket_utilisateur_fk_fkey FOREIGN KEY (utilisateur_fk)
        REFERENCES public.utilisateur (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.ticket
    OWNER to alain;
