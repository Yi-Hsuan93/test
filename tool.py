# 檔案：tool.py

def add(a, b):
    return a + b

print("哈囉！我只要被讀取就會印出來。")

# --- 防護罩開始 ---
if __name__ == "__main__":
    print("這段程式碼只有在『直接執行 tool.py』時才會出現！")
    print("讓我來測試一下 add 函數：2 + 3 =", add(2, 3))