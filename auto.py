from chat_downloader import ChatDownloader
import pyautogui
import threading
import time

# 🎯 NHẬP LINK LIVESTREAM YOUTUBE CỦA BẠN TẠI ĐÂY:
YOUTUBE_URL = 'https://www.youtube.com/watch?v=YOUR_LIVE_ID'

# 🔁 Hàm giữ phím trong vài giây rồi tự thả
def hold_key_for_seconds(key, seconds):
    def do_hold():
        pyautogui.keyDown(key)
        print(f"[HOLD] Giữ phím '{key}' trong {seconds}s")
        time.sleep(seconds)
        pyautogui.keyUp(key)
        print(f"[HOLD] Thả phím '{key}' sau {seconds}s")
    threading.Thread(target=do_hold).start()

# 🧠 Xử lý lệnh từ bình luận
def handle_command(text):
    text = text.strip().lower()

    if text.startswith("/mx "):
        try:
            dx = int(text.split("/mx ")[1])
            pyautogui.moveRel(dx, 0, duration=0.1)
            print(f"[MX] Di chuyển X: {dx}px")
        except:
            print("[LỖI] /mx không hợp lệ")

    elif text.startswith("/my "):
        try:
            dy = int(text.split("/my ")[1])
            pyautogui.moveRel(0, dy, duration=0.1)
            print(f"[MY] Di chuyển Y: {dy}px")
        except:
            print("[LỖI] /my không hợp lệ")

    elif text.startswith("/ml "):
        value = text.split("/ml ")[1].strip()
        if value == "true":
            pyautogui.mouseDown(button='left')
            print("[ML] Giữ chuột trái")
        elif value == "false":
            pyautogui.mouseUp(button='left')
            print("[ML] Thả chuột trái")
        else:
            print("[LỖI] /ml chỉ nhận true/false")

    elif text.startswith("/mr "):
        value = text.split("/mr ")[1].strip()
        if value == "true":
            pyautogui.mouseDown(button='right')
            print("[MR] Giữ chuột phải")
        elif value == "false":
            pyautogui.mouseUp(button='right')
            print("[MR] Thả chuột phải")
        else:
            print("[LỖI] /mr chỉ nhận true/false")

    elif text.startswith("/k "):
        key = text[3:].strip()
        if key in pyautogui.KEYBOARD_KEYS:
            pyautogui.press(key)
            print(f"[K] Bấm phím: {key}")
        else:
            print(f"[LỖI] Phím không hợp lệ: {key}")

    elif text.startswith("/kd "):
        key = text[4:].strip()
        if key in pyautogui.KEYBOARD_KEYS:
            pyautogui.keyDown(key)
            print(f"[KD] Giữ phím: {key}")
        else:
            print(f"[LỖI] Phím không hợp lệ: {key}")

    elif text.startswith("/ku "):
        key = text[4:].strip()
        if key in pyautogui.KEYBOARD_KEYS:
            pyautogui.keyUp(key)
            print(f"[KU] Thả phím: {key}")
        else:
            print(f"[LỖI] Phím không hợp lệ: {key}")

    elif text.startswith("/mw "):
        try:
            seconds = float(text.split("/mw ")[1])
            hold_key_for_seconds("w", seconds)
        except:
            print("[LỖI] /mw sai cú pháp")

    elif text.startswith("/ma "):
        try:
            seconds = float(text.split("/ma ")[1])
            hold_key_for_seconds("a", seconds)
        except:
            print("[LỖI] /ma sai cú pháp")

    elif text.startswith("/ms "):
        try:
            seconds = float(text.split("/ms ")[1])
            hold_key_for_seconds("s", seconds)
        except:
            print("[LỖI] /ms sai cú pháp")

    elif text.startswith("/md "):
        try:
            seconds = float(text.split("/md ")[1])
            hold_key_for_seconds("d", seconds)
        except:
            print("[LỖI] /md sai cú pháp")

    elif text == "/e":
        hold_key_for_seconds("e", 4)

# ▶️ Bắt đầu theo dõi chat YouTube
def start_listening():
    print("=== KẾT NỐI CHAT YOUTUBE ===")
    try:
        chat = ChatDownloader().get_chat(YOUTUBE_URL)
        for message in chat:
            user = message.get("author", "Unknown")
            content = message.get("message", "")
            print(f"{user}: {content}")
            handle_command(content)
    except Exception as e:
        print(f"[LỖI] Không thể đọc chat: {e}")

# 🔰 Chạy chính
if __name__ == "__main__":
    start_listening()
