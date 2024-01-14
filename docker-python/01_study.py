# 重複のない文字列：ある文字列が、全て固有である（重複する文字がない）かどうかを判定するアルゴリズムを実装する。また、この実装では新たなデータ構造が使えない場合どうすればいいか。

def is_unique_chars_algorithmic(string):
  # Assuming character set is ASCII (128 characters)
  if len(string) > 128:
      return False

  # this is a pythonic and faster way to initialize an array with a fixed value.
  #  careful though it won't work for a doubly nested array
  char_set = [False] * 128
  for char in string:
    val = ord(char)
    if char_set[val]:
      # Char already found in string
      print("Duplication found!!")
      return False
    char_set[val] = True

  print("No duplication found...")
  return True

import sys

# breakpoint()
if len(sys.argv) < 2:
  # https://qiita.com/taashi/items/07bf75201a074e208ae5
  # (args[0])は、実行ファイル名になる
  # print(sys.argv[0])
  print("Usage: python3 01_study.py <input string>")
  sys.exit(1)
else:
  arg1 = sys.argv[1]
  is_unique_chars_algorithmic(arg1)
