import fileinput


class file_processor():
    def __init__(self, files):
        "takes in all files to be processes"
        return "processed"

    def filename(file):
        name = file
        return fileinput.filename()

    def lineno(file):
        "returns current (cummulative) line number"
        return fileinput.lineno()
    
    def filelineno(file):
        "returns line number within current file"
        return fileinput.filelineno()
    
    def isfileline(file):
        "checks whether current line is first in line"
        return fileinput.isfileline()
    
    def isstdin(file):
        "checks whether last line was from sys.stdin"
        return fileinput.isstdin()

    def nextfile(file):
        "close current file and moves to the next"
        return fileinput.nextfile()
    def close(file):
        "close the sequence"
        return fileinput.close()