import sqlalchemy

USER_NAME: str = ""
PASSWORD: str = ""
HOST: str = ""
DATABASE_NAME: str = ""


def main():
    con_psg = ConnectPostgreDatabase(USER_NAME, PASSWORD, HOST, DATABASE_NAME)
    sql = "SELECT * FROM test_users"
    result = con_psg.excecute_sql(sql, get_result=True)
    print(result)
    print(type(result))


class ConnectPostgreDatabase:
    """ PostgreSQLに接続するクラス

    Args:
        user_name: ユーザー名,
        password: パスワード,
        admin_flg: ホスト,
        database_name: データベース名
    Methods:
        excecute_sql: SQL文を直接実行,
        select_all: テーブル名指定して全行取得
    """
    def __init__(
          self, user_name: str, password: str,
          host: str, database_name: str
    ):
        # DB接続に必要なエンジンを作成
        self.engin = sqlalchemy.create_engine(
            f"postgresql://{user_name}:{password}@{host}/{database_name}"
        )

    ##############
    # ORMなし
    ##############
    # SQL文を直接入力して実行
    def excecute_sql(self, sql: int, get_result: bool = False) -> list:
        """ SQL文を直接実行
        Args:
            sql: SQL文
            return_result (bool): 結果を返すかどうかのフラグ。デフォルトはFalse。
        """
        with self.engin.begin() as connection:
            input_sql = sqlalchemy.text(f"{sql}")
            result = connection.execute(input_sql)
            if get_result is True:
                sql_result = []
                for row in result:
                    sql_result.append(list(row))
            return sql_result


if __name__ == "__main__":
    main()
