require "pry"
# 重複のない文字列：ある文字列が、全て固有である（重複する文字がない）かどうかを判定するアルゴリズムを実装する。また、この実装では新たなデータ構造が使えない場合どうすればいいか。

def is_unique?(string)
  hash_table = {}

  string.each_char do |char|
    if hash_table[char]
      puts "Duplication found!!"
      return false
    else
      hash_table[char] = true
    end
  end

  puts "No duplication found..."
  true
end

arg1 = ARGV[0]

if arg1.nil?
  binding.pry  
  puts "Usage: ruby script_name.rb <input_string>"
else
  is_unique?(arg1)
end
