## Development environment java

## test

```bash
// インスペクション
% docker-compose exec java bash

// コンパイル
root@5b7be900c329:/usr/src# javac Main.java

// 実行
root@5b7be900c329:/usr/src# java Main
Hello World!
```

## debug
- https://docs.oracle.com/javase/jp/6/technotes/tools/windows/jdb.html

```java
// compile
javac -g Study01.java
// excute
jdb Study01 t
```

## reference
- https://qiita.com/A-Kira/items/0dda255e00771f556e2a

## memo
- The name of a Java class cannot start with a digit (0-9). So, 01_study is not a valid class name. Class names in Java should start with a letter (a-z or A-Z) or an underscore (_), followed by letters, digits, or underscores.
