import datetime
import time

# data_entrada_oc = input("Data de entrada (dd/mm/aaaa): ")
# prazo_dias = int(input("Prazo: "))

lista_feriados = ['07/09/2023', '12/10/2023', '02/11/2023', '15/11/2023', '20/11/2023', '25/12/2023',
                  '01/01/2024', '25/01/2024']


def calcular_prazo_sla(data_entrada, sla):
    dt_entrada = converter_string_p_datetime(data_entrada)
    prazo_sla = adicionar_dias(dt_entrada, sla)
    # Atribuindo os dias entre a data de entrada e data de vencimento bruto na lista intervalo_dias:
    intervalo_dias = [dt_entrada + datetime.timedelta(days=i) for i in range(0, sla + 1)]
    # Verificar dia da semana dos itens da lista intervalo_dias:
    for data in intervalo_dias:
        if not validar_dia_util(data, lista_feriados):
            prazo_sla = adicionar_dias(prazo_sla, 1)
    # Se o prazo SLA cair em dia não útil somar 1 até que caia no próximo dia útil:
    while not validar_dia_util(prazo_sla, lista_feriados):
        prazo_sla = adicionar_dias(prazo_sla, 1)
    return prazo_sla


def converter_time_p_datetime(obj_time: time):
    obj_datetime = time.localtime(obj_time)
    return obj_datetime


def converter_datetime_p_structTime(obj_datetime: datetime):
    obj_string_datetime = obj_datetime.strftime('%d/%m/%Y')
    obj_struct_time = time.strptime(obj_string_datetime, '%d/%m/%Y')
    return obj_struct_time


def converter_time_p_structTime(obj_time: time):
    obj_struct_time = time.localtime(obj_time)
    return obj_struct_time


def converter_structTime_p_datetime(obj_structTime: time.struct_time):
    obj_datetime = datetime.datetime(obj_structTime.tm_year, obj_structTime.tm_mon, obj_structTime.tm_mday,
                                     obj_structTime.tm_hour, obj_structTime.tm_min, obj_structTime.tm_sec)
    return obj_datetime


def converter_structTime_p_time(obj_struct_Time: time.struct_time):
    obj_time = time.mktime(obj_struct_Time)
    return obj_time


def retornar_dia_semana(obj_datetime: datetime.datetime):
    obj_datetime_formatado = obj_datetime.strftime('%d/%m/%Y')
    dia_semana = time.strptime(obj_datetime_formatado, '%d/%m/%Y').tm_wday
    return dia_semana


def validar_dia_util(obj_datetime: datetime, feriados: list):
    fim_de_semana = [5, 6]

    obj_datetime_formatado = obj_datetime.strftime('%d/%m/%Y')
    dia_semana = time.strptime(obj_datetime_formatado, '%d/%m/%Y').tm_wday
    if dia_semana in fim_de_semana or obj_datetime_formatado in feriados:
        return False
    else:
        return True


def adicionar_dias(obj_datetime: datetime.datetime, dias: int):
    data = obj_datetime + datetime.timedelta(dias)
    return data


def converter_string_p_datetime(string_data: str):
    try:
        datetime_data = datetime.datetime.strptime(string_data, '%d/%m/%Y')
        return datetime_data
    except:
        try:
            datetime_data = datetime.datetime.strptime(string_data, '%m/%d/%Y')
            return datetime_data
        except:
            print('Erro!!\nFunção --> converter_time_p_datetime(): Valores Inválidos.')


def converter_datetime_p_string(obj_datetime: datetime):
    string_data = obj_datetime.strftime('%d/%m/%Y')
    return string_data


dict_ocorrPrazoSLA = {}


def exibir_resultado(dict_oc_sla):
    for ocorrencia, informacoes in dict_ocorrPrazoSLA.items():
        prazo_sla = calcular_prazo_sla(informacoes[0], informacoes[1])
        print(f'\nOcorrência {ocorrencia}:\n'
              f'\tEntrada: {informacoes[0]}\n'
              f'\tSLA:     {informacoes[1]} dias úteis\n'
              f'\tPrazo:   {prazo_sla.strftime("%d/%m/%Y")}\n')


while True:
    data_entrada = input("Digite a data de entrada: ")
    prazo = int(input("Digite o prazo: "))

    cont = str(len(dict_ocorrPrazoSLA)+1)
    print(cont)
    dict_ocorrPrazoSLA[cont] = [data_entrada, prazo]
    if input("sair?: (s)").lower() == "s":
        break

exibir_resultado(dict_ocorrPrazoSLA)