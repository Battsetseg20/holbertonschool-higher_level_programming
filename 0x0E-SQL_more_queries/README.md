<p align="center">
  <img width="409" height="128" src="https://www.holbertonschool.com/holberton-logo.png">
<p>


### Memo
#### Useful commands for Task 8
To Insert values into table
```
echo 'INSERT INTO cities (id, state_id, name) VALUES (2, 1, "San Jose");' | mysql -hlocalhost -uroot -p hbtn_0d_usa

```

#### Useful commands for from Task 10 to 16

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
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure

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

- To see the content a particular table (table `tv_genres`from `hbtn_0d_tvshows`)
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

