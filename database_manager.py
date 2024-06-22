"""
SqlAlchemyを使用したデータベース操作を簡略化するモジュール

Examples:
    PostgreSQLに接続してテーブル全件取得してコンソールに出力

    >>> import database_manager
    >>> posgresql = database_manager
    >>> connect_db = database_manager.ConnectPostgreSQL(
    ...     USER_NAME, PASSWORD, HOST, DATABASE_NAME
    ... )
    >>> sql = "SELECT * FROM hoge"
    >>> result = connect_db.execute_sql(sql, get_result=True)
    >>> print(result)
        [[hoge1, hoge2], [hoge3, hoge4]...]
"""
from sqlalchemy import create_engine, text


# PostgreSQLに接続
class ConnectPostgreSQL:
    """
    PostgreSQLに接続するクラス

    Args:
        user_name (str): ユーザー名
        password (str): パスワード
        host (str): ホスト
        database_name (str): データベース名

    Methods:
        execute_sql: SQL文を直接実行
    """
    def __init__(
          self, user_name: str, password: str,
          host: str, database_name: str
    ):
        # DB接続に必要なエンジンを作成
        self.engine = create_engine(
            f"postgresql://{user_name}:{password}@{host}/{database_name}"
        )

    def execute_sql(self, sql: str, get_result: bool = False) -> list:
        """
        SQL文を直接実行

        Args :
            sql (str): SQL文
            return_result (bool): 結果を返すかどうかのフラグ
        """
        with self.engine.begin() as connection:
            input_sql = text(sql)
            result = connection.execute(input_sql)
            if get_result is True:
                sql_result = []
                for row in result:
                    sql_result.append(list(row))
                return sql_result


# sqlite3に接続
class ConnectSqlite3:
    """
    Sqlite3に接続するクラス

    Args:
        database_name (str): データベース名

    Methods:
        execute_sql: SQL文を直接実行

    Return:
        1行ずつリストを返す
    """
    def __init__(self, database_name: str):
        # DB接続に必要なエンジンを作成
        self.engine = create_engine(
            f"sqlite:///{database_name}", echo=True
        )

    def execute_sql(self, sql: str, get_result: bool = False) -> list:
        """
        SQL文を直接実行

        Args :
            sql (str): SQL文
            return_result (bool): 結果を返すかどうかのフラグ
        """
        with self.engine.begin() as connection:
            input_sql = text(sql)
            result = connection.execute(input_sql)
            if get_result is True:
                sql_result = [list(row) for row in result]
            return sql_result

    def execute_sql_file(
        self,
        file_path: str,
        get_result: bool = False,
        encoding: str = "utf-8"
    ) -> list:
        """
        SQLファイルを実行

        Args :
            file_path (str): sqlファイルパス
            return_result (bool): 結果を返すかどうかのフラグ
            encoding (str): 文字コード
        """
        with open(file_path, "r", encoding=encoding) as f:
            sql = f.read()
        with self.engine.begin() as connection:
            result = connection.execute(text(sql))
            if get_result is True:
                sql_result = [list(row) for row in result]
            return sql_result
