import argparse
from colorama import init, Fore

init()
GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX

parser = argparse.ArgumentParser(prog = "video-editor")
parser.add_argument('file_name', help = 'name or path of video file name')
group = parser.add_argument_group()
group.add_argument('-s', '--speed', type=int,
                    help = "acceleration of video")
group.add_argument('-c', '--cut', type=int,
                    help = "write time to cut video")
group.add_argument('-g', '--glue', type=str,
                    help = "write name or path to glue video")
args = parser.parse_args()
