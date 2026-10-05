# Bài 5: Khôi phục trạng thái và Đảo ngược commit (Reset vs Revert)

## Giới thiệu
Bài tập này thực hành hai cơ chế quan trọng trong Git để xử lý các commit bị lỗi:
1. **Git Reset (Trường hợp 1)**: Dùng `git reset --mixed` (hoặc mặc định) để lùi lịch sử về commit trước đó nhưng vẫn giữ lại các thay đổi trong Working Directory dưới dạng Modified.
2. **Git Revert (Trường hợp 2)**: Dùng `git revert` để tạo một commit mới đảo ngược các thay đổi của commit lỗi, đảm bảo an toàn khi làm việc nhóm trên remote repository.

## Hướng dẫn chạy chương trình
Chạy tệp Python mô phỏng:
```bash
python main.py
```