import sys
import inspect

debug_flag = False

def help(cmd: str = ""):
    """
    This help function gives instruction on how to use the application.

    Usage:
        pyBudget [cmd] [options]

    Commands:
        help [cmd] [option]

    Args:
        cmd: optionally display specific command usage.
        If no cmd argument is provided, this message is displayed.
    """
    if debug_flag:
        print(f"~~~ DEBUG:\n\tcmd str: {cmd}")
    if cmd:
        match cmd:
            case "repl" | "r":
                print('repl sample help output')
            case _:
                print("Command option not found, try again.")
    else:
        print(inspect.getdoc(help))


def main():
    args = sys.argv
    global debug_flag
    # debug
    if args.__len__() > 1 and args[1] == "d" or "debug":
        debug_flag = True
        print("\n~~~ DEBUG MODE STARTED ~~~")
        print('args: ', args)
        print('args len: ', args.__len__())
        args.pop(1) # remove debug option str so we can use regular arg parsing
    
    # check which args option was used
    if args.__len__() == 1:
        print("\nNo command used, printing help command...\n")
        help()
    elif args.__len__() > 1:
        match args[1]:
            case "h" | "help":
                help()

    if debug_flag:
        print("\n~~~ DEBUG MODE END ~~~")


if __name__ == "__main__":
    main()
