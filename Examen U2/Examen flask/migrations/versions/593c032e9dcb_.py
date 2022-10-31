"""empty message

Revision ID: 593c032e9dcb
Revises: 
Create Date: 2022-10-31 11:31:48.983596

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '593c032e9dcb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('artista',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('disciplina',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('escuela',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('museo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('obra',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('obra')
    op.drop_table('museo')
    op.drop_table('escuela')
    op.drop_table('disciplina')
    op.drop_table('artista')
    # ### end Alembic commands ###