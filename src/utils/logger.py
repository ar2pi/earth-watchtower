import logging
from .cli_args import args

verbosity_level = [
    None,
    logging.CRITICAL,
    logging.ERROR,
    logging.WARNING,
    logging.INFO,
    logging.DEBUG
]

level = verbosity_level[min(args.verbose, len(verbosity_level) - 1)]

logging.basicConfig(level=level, format='%(asctime)s.%(msecs)03d %(levelname)s ❯ %(message)s', datefmt='%H:%M:%S')

logger = logging.getLogger(__name__)
