"""insert metadata

Revision ID: c08099dcee2c
Revises: e9c1c0e4463a
Create Date: 2023-08-15 14:40:27.874168

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c08099dcee2c'
down_revision = 'e9c1c0e4463a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # insert destination
    op.execute("INSERT INTO destination (nom,prix,devise) VALUES('Libreville – Lebamba',17000,'FCFA');");
    op.execute("INSERT INTO destination (nom,prix,devise) VALUES('Libreville – Yombi',12000,'FCFA');");
    op.execute("INSERT INTO destination (nom,prix,devise) VALUES('Libreville – Guidouma',13000,'FCFA');");
    op.execute("INSERT INTO destination (nom,prix,devise) VALUES('Libreville – Lambarene',7000,'FCFA');");
    op.execute("INSERT INTO destination (nom,prix,devise) VALUES('Libreville – Ndende',15000,'FCFA');");
    op.execute("INSERT INTO destination (nom,prix,devise) VALUES('Libreville – Mouila',14500,'FCFA');");
    op.execute("INSERT INTO destination (nom,prix,devise) VALUES('Libreville – Oyenano',10000,'FCFA');");
    #insert admin user. mot_de_passe = 12345
    op.execute("INSERT INTO utilisateur (nom,login,mot_de_passe, role, etat) VALUES('admin','admin','$2b$12$TpXFEh4nzjEtIuNXNlthr.qAlnZbbzd0lS5KuzjsRtVlbXMlB5mRm','ADMIN', 'actif');");


def downgrade() -> None:
    
    op.execute("TRUNCATE TABLE destination CASCADE;");
    op.execute("TRUNCATE TABLE utilisateur CASCADE;");
