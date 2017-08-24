from sqlalchemy import Table, MetaData, Column, Integer, String
from tokenbox import TokenBox

metadata = MetaData()

table_definitions = {
    "login_token": Table("login_token", metadata,
        Column("login_token_pk", Integer, primary_key=True),
        Column('access_token', String(45), nullable=False),
        Column('expires_in', Integer, nullable=False),
        Column('refresh_token', String(45), nullable=False),
        Column('token_type', String(45), nullable=False),
        Column('expiry', Integer, nullable=False),
    ),
    "access_token": Table("access_token", metadata,
        Column("access_token_pk", Integer, primary_key=True),
        Column('rest_token', String(45), nullable=False),
        Column('rest_url', String(60), nullable=False)
    )
}

use_sqlite = True

tokenbox = TokenBox('db_user', 'db_pass', 'tokenbox_test', use_sqlite, metadata, **table_definitions)
tokenbox.create_database()
tokenbox.update_token('login_token', access_token="12341234123asdfasdf4", expires_in=300,
                      refresh_token="asdfkk23784987123khjga", token_type="login", expiry=12312312)
tokenbox.update_token('access_token', rest_token="12341234123asdfasdf4", rest_url="asdfkk23784987123khjga")
print(tokenbox.get_token('login_token'))
print(tokenbox.get_token('access_token'))

tokenbox.destroy_database()