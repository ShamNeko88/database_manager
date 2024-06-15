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
    >>> result = con_psg.execute_sql(sql, get_result=True)
    >>> print(result)
        [[hoge1, hoge2], [hoge3, hoge4]...]
"""

from sqlalchemy import create_engine, text


class ConnectPostgreSQL:
    """
    PostgreSQLに接続するクラス

    Args:
        user_name (str): ユーザー名
        password (str): パスワード
        admin_flg (str): ホスト
        database_name (str): データベース名

    Methods:
        execute_sql: SQL文を直接実行
        select_all: テーブル名指定して全行取得
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
            return_result (bool): 結果を返すかどうかのフラグ。デフォルトはFalse
        """
        with self.engine.begin() as connection:
            input_sql = text(f"{sql}")
            result = connection.execute(input_sql)
            if get_result is True:
                sql_result = []
                for row in result:
                    sql_result.append(list(row))
            return sql_result
