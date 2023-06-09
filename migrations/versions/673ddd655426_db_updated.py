"""db updated

Revision ID: 673ddd655426
Revises: 4ac26d8147a8
Create Date: 2022-08-09 13:25:06.333901

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '673ddd655426'
down_revision = '4ac26d8147a8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('friends',
    sa.Column('fk_user_from', sa.Integer(), nullable=False),
    sa.Column('fk_user_to', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['fk_user_from'], ['user.userid'], ),
    sa.ForeignKeyConstraint(['fk_user_to'], ['user.userid'], ),
    sa.PrimaryKeyConstraint('fk_user_from', 'fk_user_to')
    )
    op.drop_table('friend')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('friend',
    sa.Column('fk_user_from', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('fk_user_to', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['fk_user_from'], ['user.userid'], name='friend_fk_user_from_fkey'),
    sa.ForeignKeyConstraint(['fk_user_to'], ['user.userid'], name='friend_fk_user_to_fkey')
    )
    op.drop_table('friends')
    # ### end Alembic commands ###
