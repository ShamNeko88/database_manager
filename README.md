### 概要
SqlAlchemyを使用したデータベース操作を簡略化するモジュール

### Examples
PostgreSQLに接続してテーブル全件取得してコンソールに出力

```python
>>> import database_manager
>>> connect_db = database_manager.ConnectPostgreSQL(
...     USER_NAME, PASSWORD, HOST, DATABASE_NAME
... )
>>> sql = "SELECT * FROM hoge"
>>> result = connect_db.execute_sql(sql, get_result=True)
>>> print(result)
    [[hoge1, hoge2], [hoge3, hoge4]...]
```