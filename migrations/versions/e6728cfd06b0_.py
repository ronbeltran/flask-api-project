"""empty message

Revision ID: e6728cfd06b0
Revises: d62b3b7ba046
Create Date: 2016-07-13 16:09:44.019460

"""

# revision identifiers, used by Alembic.
revision = 'e6728cfd06b0'
down_revision = 'd62b3b7ba046'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_active', sa.Boolean(), nullable=True))
    op.add_column('user', sa.Column('is_staff', sa.Boolean(), nullable=True))
    op.add_column('user', sa.Column('is_superuser', sa.Boolean(), nullable=True))
    op.create_index(op.f('ix_user_is_active'), 'user', ['is_active'], unique=False)
    op.create_index(op.f('ix_user_is_staff'), 'user', ['is_staff'], unique=False)
    op.create_index(op.f('ix_user_is_superuser'), 'user', ['is_superuser'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_is_superuser'), table_name='user')
    op.drop_index(op.f('ix_user_is_staff'), table_name='user')
    op.drop_index(op.f('ix_user_is_active'), table_name='user')
    op.drop_column('user', 'is_superuser')
    op.drop_column('user', 'is_staff')
    op.drop_column('user', 'is_active')
    ### end Alembic commands ###