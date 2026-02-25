# Configure PyMySQL as MySQLdb for Django
try:
    import pymysql
    pymysql.version_info = (2, 2, 2, "final", 0)
    pymysql.install_as_MySQLdb()
except Exception:
    # If PyMySQL isn't available, Django will attempt to use mysqlclient; the error will explain what's missing.
    pass
