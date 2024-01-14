// 重複のない文字列：ある文字列が、全て固有である（重複する文字がない）かどうかを判定するアルゴリズムを実装する。また、この実装では新たなデータ構造が使えない場合どうすればいいか。
// Assuming character set is ASCII (128 characters)

public class Study01 {
  public static boolean isUniqueChars(String str) {
    if (str.length() > 128) {
      return false;
    }
    boolean[] char_set = new boolean[128];
		for (int i = 0; i < str.length(); i++) {
			int val = str.charAt(i);
			if (char_set[val]) {
        System.out.println("Duplication found!!");
        return false;
      }
			char_set[val] = true;
		}
    System.out.println("No duplication found...");
		return true;
	}

  public static void main(String[] args) {
    for (String str : args) {
      isUniqueChars(str);
      // System.out.println(word + ": " + isUniqueChars(word));
    }
  }
}
