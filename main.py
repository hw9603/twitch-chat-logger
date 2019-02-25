import argparse
import sys
from manager import TwitchManager


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--streams-to-log", dest="channels_amount", type=int,
                        help="the number of streams to log", default=100)
    parser.add_argument("-f", "--log-filename", dest="log_filename",
                        help="the filename to log to", default=None)
    parser.add_argument("-c", "--channels", dest="channels", type=str, nargs='+',
                        help="the specific channel names to log", default=[])
    parser.add_argument("-l", "--channel-filename", dest="channel_filename",
                        help="the filename containing all the specific channels", default=None)
    args = parser.parse_args()

    manager = TwitchManager(channels_amount=args.channels_amount, channels=args.channels, log_filename=args.log_filename, channel_filename=args.channel_filename)
    try:
        manager.run_log_loop()
    except KeyboardInterrupt:
        print 'Exiting gracefully...'
        manager.stop_bot()

if __name__ == "__main__":
    main()
