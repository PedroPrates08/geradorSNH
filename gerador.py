import random

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZÇ"
lower = "abcdefghijklmnopqrstuvwxyzç"
number = "0123456789"
symbols = "!@#$%¨&*(){}[]ªº°§?/:;.,¬"

qnt = 6
qntInt = int(qnt)
tamanho = qntInt

MaxMin = upper + lower + number + symbols
senhaMaxMin = "".join(random.sample(MaxMin,tamanho))

print("senhaMaxmin = " + senhaMaxMin)