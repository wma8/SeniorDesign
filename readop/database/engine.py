from sqlalchemy import create_engine

import readop.utility.config as config


# connection configuration
_protocol = 'mysql+pymysql'
_echo = config.get_debug_database_engine_echo()

# database configuration
_username = config.get_database_username()
_password = config.get_database_password()
_host = config.get_database_host()
_port = config.get_database_port()
_db_name = config.get_database_name()


Engine = create_engine(
    _protocol + '://' + _username + ':' + _password + '@' + _host + ':' + _port + '/' + _db_name,
    echo=_echo
)
