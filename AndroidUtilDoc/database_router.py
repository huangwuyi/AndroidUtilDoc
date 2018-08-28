class MssqlDatabaseRouter:

    def db_for_read(self, model, **hints):
        if model.Meta.app_label == 'MSSQL':
            return 'mssql'
        return None

    def db_for_write(self, model, **hints):
        if model.Meta.app_label == 'MSSQL':
            return 'mssql'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth app is involved.
        """
        if obj1._meta.app_label == 'auth' or \
                obj2._meta.app_label == 'auth':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'MSSQL':
            return db == 'mssql'
        return None
