import argparse



def main(argv=None):

    parser = argparse.ArgumentParser(
        "ReverseCap",
        "reverses are capitalizes"
    )

    parser.add_argument(
        "string",
        help="The string to be reversed"
        )
    # parser.add_argument(
    #     name="--reverse",
    #     help="Whether to reverse the string",
    #     default=True
    # )
    # parser.add_argument(
    #     name="--capitalize",
    #     help="Wether to capitalize the string",
    #     default=False
    # )
    args = parser.parse_args(argv)
    flipper(*args)

if __name__ == "__main__":
    main()
    # exit(main())
    # main(*args)