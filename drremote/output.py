from pathlib import Path
import logging


class OutputWriter:

    def __init__(self,
                 outfile: Path):
        self.outfile = outfile

    def error(self, msg: str):
        logging.error(msg)
        with open(self.outfile, "w") as f:
            f.write("Error\n" + msg)
            f.flush()

    def success(self, msg: str):
        logging.info(msg)
        with open(self.outfile, "w") as f:
            f.write("Success\n" + msg)
            f.flush()

    def logdebug(self, msg: str):
        logging.debug(msg)

    def loginfo(self, msg: str):
        logging.info(msg)
