import subprocess
import sys

def run_git_command(command):
    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Lỗi khi chạy lệnh {' '.join(command)}: {e.stderr}", file=sys.stderr)

def main():
    print("=== Mô phỏng Git Reset và Revert ===")
    print("1. Trường hợp 1: Git Reset (Sửa đổi cục bộ, giữ lại thay đổi)")
    print("Lệnh sử dụng: git reset --mixed HEAD~")
    
    print("\n2. Trường hợp 2: Git Revert (Sửa đổi công cộng, tạo commit đối lập)")
    print("Lệnh sử dụng: git revert <commit-hash>")
    
    print("\nHoàn thành mô phỏng logic bài tập Git.")

if __name__ == "__main__":
    main()