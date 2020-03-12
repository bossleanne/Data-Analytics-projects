import subprocess
import sys, termios, tty, os, time
import pyperclip
import argparse

def launch_log_playback():
    pcd_dir = args.dir
    path = args.tool
    os.chdir(path)
    pcd = [pcd for pcd in os.listdir(pcd_dir)]
    pcd.sort()
    toger = 28
    print("\n !!! Rules: `D` to next page, `A` to previous page, `ESC` to terminate,`TAB` to zoom !!!\n")
    button_delay = 0.2

    while True:
        char = getch()
        if (char == "p"):
            print("Stop!")
            exit(0)

        if (char == "a"):  # left
            toger -= 1
            print("========================================pcd number:===", toger)

            pyperclip.copy(pcd[toger])
            subprocess.call(['./StartAViewer', pcd_dir + pcd[toger]])

            # time.sleep(button_delay)

        elif (char == "d"):  # right
            toger += 1
            print("========================================pcd number:===", toger)
            pyperclip.copy(pcd[toger])
            subprocess.call(['./StartViewer', pcd_dir + pcd[toger]])

            # time.sleep(button_delay)


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    parser.add_argument('--dir', type=str, default='/home/', help='Pcd files directory.')
    parser.add_argument('--tool', type=str, default='/home/', help='Annotation review tool.')

    args = parser.parse_args()
    launch_log_playback()