"""
Automated Git History Builder (2023 - 2026)
Total commits: ~961 (same as before)
Strategy: Take original 958-commit schedule, shift the last 87 writeup commits
          to 2025-2026 weekly Saturday dates. Total stays ~961.
"""
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
import os
import subprocess
import random

base_dir = os.path.dirname(os.path.abspath(__file__))

# Load original 958-commit schedule
sys.path.append(r"C:\Users\hamra\.gemini\antigravity-ide\brain\3e42362f-152b-4722-bd58-4eb82748b360\scratch")
from test_full_schedule import final_commits as original_schedule

print(f"Original schedule loaded: {len(original_schedule)} commits")

# 87 weekly Saturday dates for 2025-2026 (up to Aug 30 2026)
SATURDAYS_2025_2026 = [
    "2025-01-04", "2025-01-11", "2025-01-18", "2025-01-25",
    "2025-02-01", "2025-02-08", "2025-02-15", "2025-02-22",
    "2025-03-01", "2025-03-08", "2025-03-15", "2025-03-22", "2025-03-29",
    "2025-04-05", "2025-04-12", "2025-04-19", "2025-04-26",
    "2025-05-03", "2025-05-10", "2025-05-17", "2025-05-24", "2025-05-31",
    "2025-06-07", "2025-06-14", "2025-06-21", "2025-06-28",
    "2025-07-05", "2025-07-12", "2025-07-19", "2025-07-26",
    "2025-08-02", "2025-08-09", "2025-08-16", "2025-08-23", "2025-08-30",
    "2025-09-06", "2025-09-13", "2025-09-20", "2025-09-27",
    "2025-10-04", "2025-10-11", "2025-10-18", "2025-10-25",
    "2025-11-01", "2025-11-08", "2025-11-15", "2025-11-22", "2025-11-29",
    "2025-12-06", "2025-12-13", "2025-12-20", "2025-12-27",
    "2026-01-03", "2026-01-10", "2026-01-17", "2026-01-24", "2026-01-31",
    "2026-02-07", "2026-02-14", "2026-02-21", "2026-02-28",
    "2026-03-07", "2026-03-14", "2026-03-21", "2026-03-28",
    "2026-04-04", "2026-04-11", "2026-04-18", "2026-04-25",
    "2026-05-02", "2026-05-09", "2026-05-16", "2026-05-23", "2026-05-30",
    "2026-06-06", "2026-06-13", "2026-06-20", "2026-06-27",
    "2026-07-05", "2026-07-12", "2026-07-19", "2026-07-26",
    "2026-08-01", "2026-08-08", "2026-08-15", "2026-08-22", "2026-08-29",
]

WEEKLY_TIMES = [
    "14:22:17", "15:41:33", "16:08:45", "17:33:12", "18:22:51",
    "19:05:38", "19:47:22", "20:14:09", "20:58:33", "21:11:47",
    "21:44:18", "22:03:29", "22:31:55", "22:47:12", "23:02:41",
]

N_SHIFT = len(SATURDAYS_2025_2026)  # 87 commits move to 2025-2026

# Split the original schedule:
# - Writeup commits only (not readme_weekly_sync) are candidates to shift
writeup_commits = [c for c in original_schedule if c['type'] == 'writeup']
readme_commits  = [c for c in original_schedule if c['type'] == 'readme_weekly_sync']

# Take the LAST N_SHIFT writeup commits and reassign their dates to 2025-2026
# The rest stay in 2023-2024
early_writeups = writeup_commits[:-N_SHIFT]   # stays in 2023-2024
shifted_writeups = writeup_commits[-N_SHIFT:]  # moves to 2025-2026

print(f"Writeup commits staying in 2023-2024: {len(early_writeups)}")
print(f"Writeup commits shifted to 2025-2026: {len(shifted_writeups)}")
print(f"README sync commits (2023-2024): {len(readme_commits)}")

# Reassign dates for shifted commits -> weekly Saturdays 2025-2026
for i, c in enumerate(shifted_writeups):
    new_date = SATURDAYS_2025_2026[i]
    new_time = WEEKLY_TIMES[i % len(WEEKLY_TIMES)]
    c['datetime'] = f"{new_date} {new_time}"
    c['date'] = new_date

# Merge everything back and sort chronologically
final_schedule = early_writeups + readme_commits + shifted_writeups
final_schedule.sort(key=lambda x: x['datetime'])

total = len(final_schedule)
print(f"Final schedule: {total} commits (2023-2024 bulk + 2025-2026 weekly)")
print(f"  Earliest: {final_schedule[0]['datetime'][:10]}")
print(f"  Latest:   {final_schedule[-1]['datetime'][:10]}")

# Backup all file contents (exclude commit.md — never push it)
EXCLUDED_FILES = {'commit.md', 'newcommitschedule.md'}
file_contents = {}
for f in os.listdir(base_dir):
    if f.endswith('.md') and f not in EXCLUDED_FILES:
        fp = os.path.join(base_dir, f)
        with open(fp, 'r', encoding='utf-8', errors='ignore') as fh:
            file_contents[f] = fh.readlines()

readme_full_lines = file_contents.get('README.md', [])

# Initialize git
if not os.path.exists(os.path.join(base_dir, '.git')):
    subprocess.run(['git', 'init'], cwd=base_dir, check=True)
subprocess.run(['git', 'branch', '-M', 'main'], cwd=base_dir, check=True)

print(f"\nApplying {total} commits across 2023-2026...")

try:
    for idx, c in enumerate(final_schedule, 1):
        fn = c['filename']
        dt = c['datetime']
        msg = c['message']
        ctype = c['type']

        env = os.environ.copy()
        env['GIT_AUTHOR_DATE'] = dt
        env['GIT_COMMITTER_DATE'] = dt

        if ctype == 'readme_weekly_sync':
            w_num = c['part']
            ratio = min(1.0, w_num / 104.0)
            lines_count = max(35, int(len(readme_full_lines) * ratio))
            weekly_content = readme_full_lines[:lines_count] + [
                f"\n\n<!-- Weekly Progress: Week {w_num}/104 | {dt[:10]} -->\n"
            ]
            fp = os.path.join(base_dir, 'README.md')
            with open(fp, 'w', encoding='utf-8') as fh:
                fh.writelines(weekly_content)
            subprocess.run(['git', 'add', 'README.md'], cwd=base_dir, check=True)
            subprocess.run(['git', 'commit', '--allow-empty', '-m', msg], cwd=base_dir, env=env, check=True)

        else:
            part = c['part']
            total_parts = c['total_parts']
            if fn in file_contents:
                all_lines = file_contents[fn]
                lines_to_write = max(1, int(len(all_lines) * (part / total_parts)))
                fp = os.path.join(base_dir, fn)
                with open(fp, 'w', encoding='utf-8') as fh:
                    fh.writelines(all_lines[:lines_to_write])
                subprocess.run(['git', 'add', fn], cwd=base_dir, check=True)
                subprocess.run(['git', 'commit', '--allow-empty', '-m', msg], cwd=base_dir, env=env, check=True)

        if idx % 100 == 0 or idx == total:
            print(f"  [{idx}/{total}] {dt[:10]} | {msg}")

finally:
    # Restore all files to full content
    print("\nRestoring all files to complete versions...")
    for fn, lines in file_contents.items():
        fp = os.path.join(base_dir, fn)
        with open(fp, 'w', encoding='utf-8') as fh:
            fh.writelines(lines)

# Final commit at Dec 2024
final_dt = "2024-12-28 23:30:00"
env = os.environ.copy()
env['GIT_AUTHOR_DATE'] = final_dt
env['GIT_COMMITTER_DATE'] = final_dt
subprocess.run(['git', 'add', 'README.md'], cwd=base_dir, check=True)
if os.path.exists(os.path.join(base_dir, 'apply_git_history.py')):
    subprocess.run(['git', 'add', 'apply_git_history.py'], cwd=base_dir, check=True)
subprocess.run(
    ['git', 'commit', '--allow-empty', '-m', 'Finalize repository curriculum roadmap'],
    cwd=base_dir, env=env, check=True
)

print(f"\nSUCCESS: {total + 1} total commits applied across 2023-2026!")
print("Run: git push -u origin main --force")
