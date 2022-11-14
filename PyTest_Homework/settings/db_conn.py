def GetConnectionString():
    DRIVER_NAME = 'SQL SERVER'
    SERVER_NAME = 'VDUS2DEVWIN2772\MSSQLSERVER1'
    DATABASE_NAME = 'AdventureWorks2012'
    USER_NAME = 'TestLogin'
    PASSWORD = 'TestLogin'

    connectionString = f"""
        DRIVER={{{DRIVER_NAME}}};
        SERVER={SERVER_NAME};
        DATABASE={DATABASE_NAME};
        Trust_Connection=yes;
        uid={USER_NAME};
        pwd={PASSWORD};
    """
    return connectionString
