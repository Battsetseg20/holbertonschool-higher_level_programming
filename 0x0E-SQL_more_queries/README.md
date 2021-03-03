<p align="center">
  <img width="409" height="128" src="https://www.holbertonschool.com/holberton-logo.png">
<p>


### Memo
#### Useful commands for Task 8
To Insert values into table
```
echo 'INSERT INTO cities (id, state_id, name) VALUES (2, 1, "San Jose");' | mysql -hlocalhost -uroot -p hbtn_0d_usa

```

#### Useful commands for from Task 10 to 18

- To start mysql
```
$ mysql -hlocalhost -uroot -p
Password: 

```

- To import a SQL dump
```
$ mysql> use database_name;
$ mysql> source file.sql;
```
OR
```
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 

```
- To see databases in server
```
mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| hbtn_0c_0          |
| hbtn_0d_2          |
| hbtn_0d_tvshows    |
| hbtn_0d_usa        |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
8 rows in set (0.00 sec)
```
OR
```
SHOW DATABASES | mysql -hlocalhost -uroot -p
Enter password: 
```
- To see the list of tables in particular database
```
mysql> SHOW TABLES FROM hbtn_0d_tvshows;
+---------------------------+
| Tables_in_hbtn_0d_tvshows |
+---------------------------+
| tv_genres                 |
| tv_show_genres            |
| tv_shows                  |
+---------------------------+
3 rows in set (0.00 sec)
```
OR
```
$ SHOW TABLES | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
```

- To see the content of a particular table (table `tv_genres`from `hbtn_0d_tvshows`)
```
mysql> USE hbtn_0d_tvshows ;
       Reading table information for completion of table and column names
       You can turn off this feature to get a quicker startup with -A

       Database changed

mysql> SELECT * FROM tv_genres;
+----+-----------+
| id | name      |
+----+-----------+
|  1 | Drama     |
|  2 | Mystery   |
|  3 | Adventure |
|  4 | Fantasy   |
|  5 | Comedy    |
|  6 | Crime     |
|  7 | Suspense  |
|  8 | Thriller  |
+----+-----------+
8 rows in set (0.00 sec)
```
ÒR
```
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
```
```
$ echo 'SELECT * FROM tv_shows;' | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
$ Enter password: 
id    title
1     House
2     Game of Thrones
3     The Big Bang Theory
4     New Girl
5     Silicon Valley
6     Breaking Bad
7     Better Call Saul
8     Dexter
9     Homeland
10    The Last Man on Earth
```
```
$ echo 'SELECT * FROM tv_show_genres;' | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
$ Enter password: 
show_id		genre_id
1			1
1			2
2			3
2			1
2			4
3			5
4			5
5			5
6			6
6			1
6			7
6			8
8			6
8			1
8			2
8			7
8			8
10			5
10			1
```
#### Useful commands for from Task 19 to 20
```
mysql> SHOW DATABASES;
+----------------------+
| Database             |
+----------------------+
| information_schema   |
| hbtn_0c_0            |
| hbtn_0d_2            |
| hbtn_0d_tvshows      |
| hbtn_0d_tvshows_rate |
| hbtn_0d_usa          |
| mysql                |
| performance_schema   |
| sys                  |
+----------------------+
9 rows in set (0.00 sec)
```
```
mysql> SHOW TABLES FROM hbtn_0d_tvshows_rate;
+--------------------------------+
| Tables_in_hbtn_0d_tvshows_rate |
+--------------------------------+
| tv_genres                      |
| tv_show_genres                 |
| tv_show_ratings                |
| tv_shows                       |
+--------------------------------+
4 rows in set (0.00 sec)
```
```
mysql> USE hbtn_0d_tvshows_rate;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> SELECT * FROM tv_genres;
+----+-----------+
| id | name      |
+----+-----------+
|  1 | Drama     |
|  2 | Mystery   |
|  3 | Adventure |
|  4 | Fantasy   |
|  5 | Comedy    |
|  6 | Crime     |
|  7 | Suspense  |
|  8 | Thriller  |
+----+-----------+
8 rows in set (0.00 sec)
```
mysql> SELECT * FROM tv_show_genres;
+---------+----------+
| show_id | genre_id |
+---------+----------+
|       2 |        1 |
|       2 |        2 |
|       3 |        3 |
|       3 |        1 |
|       3 |        4 |
|       4 |        5 |
|       5 |        5 |
|       6 |        5 |
|       7 |        6 |
|       7 |        1 |
|       7 |        7 |
|       7 |        8 |
|       9 |        6 |
|       9 |        1 |
|       9 |        2 |
|       9 |        7 |
|       9 |        8 |
|      11 |        5 |
|      11 |        1 |
+---------+----------+
19 rows in set (0.00 sec)
```
```

mysql> SELECT * FROM tv_show_ratings;
+---------+------+
| show_id | rate |
+---------+------+
|       2 |    0 |
|       2 |    1 |
|       2 |    2 |
|       2 |    3 |
|       2 |    4 |
|       2 |    5 |
|       2 |    6 |
|       3 |    0 |
|       3 |    1 |
|       3 |    2 |
|       3 |    0 |
|       3 |    0 |
|       3 |    1 |
|       3 |    2 |
|       3 |    0 |
|       3 |    0 |
|       3 |    1 |
|       3 |    2 |
|       3 |    3 |
|       3 |    4 |
|       3 |    0 |
|       3 |    1 |
|       3 |    2 |
|       3 |    3 |
|       3 |    4 |
|       3 |    5 |
|       3 |    6 |
|       3 |    7 |
|       3 |    8 |
|       3 |    0 |
|       3 |    1 |
|       3 |    2 |
|       3 |    0 |
|       3 |    1 |
|       3 |    2 |
|       3 |    3 |
|       3 |    4 |
|       3 |    5 |
|       3 |    6 |
|       3 |    0 |
|       3 |    1 |
|       3 |    2 |
|       4 |    0 |
|       5 |    0 |
|       6 |    0 |
|       6 |    0 |
|       6 |    1 |
|       6 |    2 |
|       6 |    3 |
|       6 |    4 |
|       6 |    0 |
|       6 |    0 |
|       6 |    1 |
|       6 |    2 |
|       6 |    3 |
|       6 |    4 |
|       6 |    5 |
|       6 |    6 |
|       6 |    7 |
|       6 |    8 |
|       6 |    0 |
|       6 |    1 |
|       6 |    2 |
|       6 |    3 |
|       6 |    4 |
|       6 |    5 |
|       6 |    6 |
|       6 |    7 |
|       6 |    8 |
|       7 |    0 |
|       7 |    1 |
|       7 |    2 |
|       7 |    0 |
|       7 |    1 |
|       7 |    2 |
|       7 |    3 |
|       7 |    4 |
|       7 |    0 |
|       7 |    1 |
|       7 |    2 |
|       8 |    0 |
|       8 |    1 |
|       8 |    2 |
|       8 |    3 |
|       8 |    4 |
|       8 |    5 |
|       8 |    6 |
|       8 |    0 |
|       8 |    1 |
|       8 |    2 |
|       8 |    3 |
|       8 |    4 |
|       8 |    5 |
|       8 |    6 |
|       8 |    0 |
|       8 |    1 |
|       8 |    2 |
|       8 |    3 |
|       8 |    4 |
|       8 |    5 |
|       8 |    6 |
|       8 |    7 |
|       8 |    8 |
|       8 |    0 |
|       8 |    1 |
|       8 |    2 |
|       8 |    0 |
|       8 |    1 |
|       8 |    2 |
|       8 |    3 |
|       8 |    4 |
|       8 |    5 |
|       8 |    6 |
|       8 |    7 |
|       8 |    8 |
|       8 |    0 |
|       8 |    1 |
|       8 |    2 |
|       8 |    3 |
|       8 |    4 |
|       8 |    0 |
|       8 |    1 |
|       8 |    2 |
|       8 |    3 |
|       8 |    4 |
|       8 |    5 |
|       8 |    6 |
|       8 |    7 |
|       8 |    8 |
|       9 |    0 |
|       9 |    1 |
|       9 |    2 |
|       9 |    0 |
|       9 |    1 |
|       9 |    2 |
|       9 |    3 |
|       9 |    4 |
|       9 |    5 |
|       9 |    6 |
|       9 |    0 |
|      10 |    0 |
|      10 |    0 |
|      10 |    1 |
|      10 |    2 |
|      10 |    3 |
|      10 |    4 |
|      10 |    5 |
|      10 |    6 |
|      10 |    7 |
|      10 |    8 |
|      10 |    0 |
|      10 |    1 |
|      10 |    2 |
|      10 |    3 |
|      10 |    4 |
|      10 |    5 |
|      10 |    6 |
|      10 |    0 |
|      10 |    0 |
|      10 |    1 |
|      10 |    2 |
|      10 |    0 |
|      10 |    1 |
|      10 |    2 |
|      10 |    3 |
|      10 |    4 |
|      10 |    5 |
|      10 |    6 |
|      10 |    7 |
|      10 |    8 |
|      10 |    0 |
|      10 |    1 |
|      10 |    2 |
|      10 |    3 |
|      10 |    4 |
|      10 |    0 |
|      10 |    1 |
|      10 |    2 |
|      10 |    3 |
|      10 |    4 |
|      10 |    5 |
|      10 |    6 |
|      10 |    7 |
|      10 |    8 |
|      10 |    0 |
|      10 |    1 |
|      10 |    2 |
|      11 |    0 |
|      11 |    1 |
|      11 |    2 |
|      11 |    3 |
|      11 |    4 |
+---------+------+
192 rows in set (0.00 sec)
```
```
mysql>  SELECT * FROM  tv_shows;
+----+-----------------------+
| id | title                 |
+----+-----------------------+
|  2 | House                 |
|  3 | Game of Thrones       |
|  4 | The Big Bang Theory   |
|  5 | New Girl              |
|  6 | Silicon Valley        |
|  7 | Breaking Bad          |
|  8 | Better Call Saul      |
|  9 | Dexter                |
| 10 | Homeland              |
| 11 | The Last Man on Earth |
+----+-----------------------+
10 rows in set (0.00 sec)

mysql> 
```
$ mysql> use database_name;
