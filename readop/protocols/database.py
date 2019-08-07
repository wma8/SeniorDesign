import mysql.connector as sql

from readop.models.credentials import Credentials


class DatabaseException(Exception):
    pass


class Database:
    def __init__(
            self,
            host: str = 'localhost',
            credentials: Credentials = Credentials('root', 'sdcTeam21!'),
            database_name: str = 'ReadOp'
    ):
        self.host = host
        self.credentials = credentials
        self.database_name = database_name
        self.connection = ''
    
    def connect(self):
        try:
            self.connection = sql.connect(
                host=self.host,
                db=self.database_name,
                user=self.credentials.username,
                password=self.credentials.password
            )
        except Exception as e:
            raise DatabaseException('failed to connect to database: ' + str(e))
    
    def disconnect(self):
        self.connection.close()
    
    @property
    def host(self):
        return self.__host
    
    @property
    def credentials(self):
        return self.__credentials
    
    @property
    def database_name(self):
        return self.__database_name
    
    @host.setter
    def host(self, host):
        if not isinstance(host, str):
            raise TypeError('host must be instance of type str')
        elif not host:
            raise ValueError('host must not be empty')
        else:
            self.__host = host
    
    @credentials.setter
    def credentials(self, credentials):
        if not isinstance(credentials, Credentials):
            raise TypeError('credentials must be instance of type Credentials')
        else:
            self.__credentials = credentials
    
    @database_name.setter
    def database_name(self, database_name):
        if not isinstance(database_name, str):
            raise TypeError('database_name must be instance of type str')
        elif not database_name:
            raise ValueError('database_name must not be empty')
        else:
            self.__database_name = database_name
