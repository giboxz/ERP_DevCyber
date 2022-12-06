import xlsxwriter
from django.shortcuts import render, redirect
from .models import *
from datetime import datetime
from xml.etree.ElementTree import tostring


def home(request):
    return render(request, "home.html")


def form_entrada(request):
    msg = ''
    if request.method == "POST":
        dataCriacao = request.POST.get('data_criacao')
        valor = request.POST.get('valor')
        descricao = request.POST.get('descricao')
        setor = request.POST.get('setor')
        Entradas(dataCriacao=dataCriacao, valor=valor,
                 descricao=descricao, setor=setor).save()
        msg = 'Salvo!'
    return render(request, 'forms_entrada_erp.html', {'msg': msg})


def consulta_entrada(request):
    dados = Entradas.objects.all()
    return render(request, 'consulta_entradas.html', {'Entradas': dados})


def form_saida(request):
    msg = ''
    if request.method == "POST":
        dataCriacao = request.POST.get('data_criacao')
        dataPagamento = request.POST.get('data_pagamento')
        valor = request.POST.get('valor')
        descricao = request.POST.get('descricao')
        setor = request.POST.get('setor')
        Saidas(dataCriacao=dataCriacao, dataPagamento=dataPagamento,
               valor=valor, descricao=descricao, setor=setor).save()
        msg = 'Salvo!'
    return render(request, 'forms_saida_erp.html', {'msg': msg})


def consulta_saida(request):
    saidas = Saidas.objects.all()
    return render(request, 'consulta_saidas.html', {'Saidas': saidas})


def editar_entrada(request, id):
    entradas = Entradas.objects.get(id=id)
    print(entradas.dataCriacao)
    return render(request, "modifica_entradas.html", {"Entradas": entradas})


def delete_entrada(request, id):
    entradas = Entradas.objects.get(id=id)
    entradas.delete()
    return redirect(consulta_entrada)


def update_entrada(request, id):
    dataCriacao = request.POST.get('data_criacao')
    valor = request.POST.get('valor')
    descricao = request.POST.get('descricao')
    setor = request.POST.get('setor')
    entradas = Entradas.objects.get(id=id)
    entradas.dataCriacao = dataCriacao
    entradas.valor = valor
    entradas.descricao = descricao
    entradas.setor = setor
    entradas.save()
    return redirect(consulta_entrada)


def editar_saida(request, id):
    saidas = Saidas.objects.get(id=id)
    return render(request, "modifica_saidas.html", {"Saidas": saidas})


def delete_saida(request, id):
    saidas = Saidas.objects.get(id=id)
    saidas.delete()
    return redirect(consulta_saida)


def update_saida(request, id):
    dataCriacao = request.POST.get('data_criacao')
    dataPagamento = request.POST.get('data_pagamento')
    valor = request.POST.get('valor')
    descricao = request.POST.get('descricao')
    setor = request.POST.get('setor')
    saidas = Saidas.objects.get(id=id)
    saidas.dataCriacao = dataCriacao
    saidas.dataPagamento = dataPagamento
    saidas.valor = valor
    saidas.descricao = descricao
    saidas.setor = setor
    saidas.save()
    return redirect(consulta_saida)

def salva_excel_entradas(request):
    msg = ''
    dados = Entradas.objects.all()

    workbook = xlsxwriter.Workbook("EntradasERP.xlsx")
    worksheet = workbook.add_worksheet("Entradas")

    worksheet.write(0, 0, "data_criacao")
    worksheet.write(0, 1, "valor")
    worksheet.write(0, 2, "descricao")
    worksheet.write(0, 3, "setor")

    linha = 1
    for d in dados:
        worksheet.write(linha, 0, d.dataCriacao.strftime('%Y-%m-%d'))
        worksheet.write(linha, 1, d.valor)
        worksheet.write(linha, 2, d.descricao)
        worksheet.write(linha, 3, d.setor)
        linha = linha + 1

    workbook.close()
    msg = 'Dados salvos no excel!'
    return render(request, 'consulta_entradas.html', {'msg': msg, "Entradas": dados})

def salva_excel_saidas(request):
    msg = ''
    dados = Saidas.objects.all()

    workbook = xlsxwriter.Workbook("SaidasERP.xlsx")
    worksheet = workbook.add_worksheet("Saidas")

    worksheet.write(0, 0, "data_criacao")
    worksheet.write(0, 1, "data_pagamento")
    worksheet.write(0, 2, "valor")
    worksheet.write(0, 3, "descricao")
    worksheet.write(0, 4, "setor")

    linha = 1
    for d in dados:
        worksheet.write(linha, 0, d.dataCriacao.strftime('%Y-%m-%d'))
        worksheet.write(linha, 1, d.dataPagamento.strftime('%Y-%m-%d'))
        worksheet.write(linha, 2, d.valor)
        worksheet.write(linha, 3, d.descricao)
        worksheet.write(linha, 4, d.setor)
        linha = linha + 1

    workbook.close()
    msg = 'Dados salvos no excel!'
    return render(request, 'consulta_saidas.html', {'msg': msg, "Saidas": dados})

