from files import *
import pandas as pd

# print(oscha3)
# print(oscha3.sort_values(0))

pd.set_option('display.max_rows', 1000000000000000000000)
# pd.set_option('display.max_columns', 1000000000000000000000)


def getdtlst(bd):
    col = bd + ".id"
    op = ">"
    qts = 1
    idd = 0
    rspx = pld(col, idd, op, qts, url + bd, 'desc')
    lst = rspx['registros'][0]['id']
    return lst


def marcoslindo(bd):
    col = bd + ".data_vencimento"
    op = ">"
    qts = 10000000000
    idd = "2023-12-01"
    rspx = pld(col, idd, op, qts, url + bd, 'asc')
    lst = rspx
    return lst
    print(lst)


def getdtall(bd):
    col = bd + ".id"
    op = ">"
    qts = 1000000
    idd = 0
    rspx = pld(col, idd, op, qts, url + bd, 'asc')
    print(rspx)
    return rspx


def getdt(operator, bd, cl, idd):
    col = bd + "." + cl
    op = operator
    qts = 100000
    rspx = pld(col, idd, op, qts, url + bd, 'desc')
    # print(rspx)
    return rspx


def ardt(rp):
    xx = rp['registros']
    date = []
    for x in xx:
        for t in x:
            date.append([t, x[t]])
        date.append(['---------', '---------'])
    df2 = pd.DataFrame(date)
    return df2


def ardtt(rp):
    xx = rp['registros']
    date = []
    for x in xx:
        date.append([x['id_saida'],
                     x['valor_total'],
                     ])
    df2 = pd.DataFrame(date)
    df2 = df2.rename(columns={0: 'id_saida',
                              1: 'valor_total',
                              })
    return df2

hoje = datetime.now().strftime('%Y-%m-%d')
print(hoje)


print(ardt(getdt('=', 'su_oss_chamado', 'id_assunto', '77')))


