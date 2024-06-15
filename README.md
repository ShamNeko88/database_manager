### 概要
SqlAlchemyを使用したデータベース操作を簡略化するモジュール

### Examples
PostgreSQLに接続してテーブル全件取得してコンソールに出力

```python
>>> import database_manager
>>> posgresql = database_manager
>>> v
... v
... v
>>> sql = "SELECT * FROM hoge"
>>> result = con_psg.execute_sql(sql, get_result=True)
>>> print(result)
    [[hoge1, hoge2], [hoge3, hoge4]...]
```