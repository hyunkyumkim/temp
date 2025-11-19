import re
import sys

# PATTERN_ONE = re.compile(r"b'\$abcdefghijklmnopqrstuvwxyz%\\r\\n'")
PATTERN_ONE = re.compile(r"b'\$abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789%\\r\\n'")
PATTERN_TWO = re.compile(r"b'([^']*)'")

def one(file: str):
    total = 0
    passed = 0
    failed_lines = []
    with open(file, "r") as f:
        for line_number, line in enumerate(f, start=1):
            total += 1

            if PATTERN_ONE.search(line):
                passed += 1
            else:
                failed_lines.append((line_number, line))

    print("===== RESULT =====")
    print(f"Total lines: {total}")
    print(f"Passed lines: {passed}")
    print(f"Failed lines: {len(failed_lines)}")
    print(f"Pass rate: {passed / total * 100:.2f}%")
    if failed_lines:
        print("===== FAILED LINES =====")
        for line_number, line in failed_lines:
            print(f"Line {line_number}: {line!r}")
    else:
        print("No failed lines.")

def two(file: str):
    total = 0
    passed = 0
    failed_lines = []
    buffer = None
    with open(file, "r") as f:
        for line_number, line in enumerate(f, start=1):
            total += 1
            match = PATTERN_TWO.search(line)
            if not match:
                failed_lines.append((line_number, line))
                continue
            content = match.group(1)
            wrapped_content = f"b'{content}'"
            if PATTERN_ONE.fullmatch(wrapped_content):
                passed += 1
                if buffer is not None:
                    failed_lines.append((buffer[0], f"b'{buffer[1]}'"))
                buffer = None
                continue
            if buffer is None:
                buffer = (line_number, content)
                continue
            prev_line_number, prev_content = buffer
            combined_content = prev_content + content
            wrapped_combined = f"b'{combined_content}'"
            if PATTERN_ONE.fullmatch(wrapped_combined):
                passed += 2
            else:
                failed_lines.append((prev_line_number, f"b'{prev_content}'"))
                failed_lines.append((line_number, content))
            buffer = None
    if buffer is not None:
        prev_line_number, prev_content = buffer
        failed_lines.append((prev_line_number, f"b'{prev_content}'"))

    print("===== RESULT =====")
    print(f"Total lines: {total}")
    print(f"Passed lines: {passed}")
    print(f"Failed lines: {len(failed_lines)}")
    print(f"Pass rate: {passed / total * 100:.2f}%")
    if failed_lines:
        print("===== FAILED LINES =====")
        for line_number, line in failed_lines:
            print(f"Line {line_number}: {line!r}")
    else:
        print("No failed lines.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python test.py <input_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    two(input_file)
