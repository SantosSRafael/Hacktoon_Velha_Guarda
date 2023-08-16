import binascii
from datetime import date
from datetime import datetime


def Descriptografa(string):
    binstr = binascii.a2b_base64(string)
    hexBased = binascii.hexlify(binstr)
    hexBased = (bytes(hexBased[len(hexBased) - 1 :]) + bytes(hexBased[:-1]))[2:]
    result = binascii.unhexlify(hexBased).decode("utf-8").replace("\n", "")
    return result


def Criptografa(string):
    hexBased = "6" + (string).encode("utf-8").hex() + "1"
    binstr = binascii.unhexlify(hexBased)
    result = binascii.b2a_base64(binstr)
    return result


def SaveLog(string, path=""):
    currentDate = date.today().strftime("%Y%m%d")
    currentTime = datetime.now().time().strftime("%H%M%S")
    dateFormated = "{}_{}".format(currentDate, currentTime)
    textFile = open("{}log_{}.txt".format(path, date.today().strftime("%Y%m%d")), "a")
    textFile.write("\n[{}]{}".format(dateFormated, string))
    textFile.close()
