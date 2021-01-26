# *-* encoding: utf-8 *-*
import requests
import json


class SerializacaoJSON(object):
    _ambiente = 1  # 1 = Produção, 2 = Homologação
    _nome_aplicacao = 'PyPlugNotas'

    def __init__(
        self,
        homologacao=False,
    ):
        self._ambiente = homologacao and 2 or 1

    def serializar_emitente(self, cpfCnpj):
        emitente = {}
        emitente['cpfCnpj'] = cpfCnpj
        return emitente

    def serialize_recipient(
        self,
        cpfCnpj,
        razaoSocial,
    ):
        recipient = {}
        recipientAddress = {}
        recipient['cpfCnpj'] = cpfCnpj
        if self._ambiente == 1:
            recipient['razaoSocial'] = razaoSocial
        else:
            recipient[
                'razaoSocial'] = 'NF-E EMITIDA EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL'
        recipient['email'] = 'contato@tecnospeed.com.br'
        recipientAddress['logradouro'] = 'AVENIDA DUQUE DE CAXIAS'
        recipientAddress['numero'] = '882'
        recipientAddress['bairro'] = 'CENTRO'
        recipientAddress['codigoCidade'] = '4115200'
        recipientAddress['descricaoCidade'] = 'MARINGA'
        recipientAddress['estado'] = 'PR'
        recipientAddress['cep'] = '87020025'
        recipient['endereco'] = recipientAddress
        return recipient

    def serializar_itens(self):

        itens = {}
        itensValorUnitario = {}
        itensTributos = {}
        itensTributosIcms = {}
        itensTributosIcmsBaseCalculo = {}
        itensTributosPis = {}
        itensTributosPisBaseCalculo = {}
        itensTributosCofins = {}
        itensTributosCofinsBaseCalculo = {}

        itens['codigo'] = '1'
        itens[
            'descricao'] = 'NOTA FISCAL EMITIDA EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL'
        itens['ncm'] = '06029090'
        itens['cest'] = '0123456'
        itens['cfop'] = '5101'
        itensValorUnitario['comercial'] = '4.6'
        itensValorUnitario['tributavel'] = '4.6'
        itens['valorUnitario'] = itensValorUnitario
        itens['valor'] = '4.6'

        itensTributosIcms['origem'] = '0'
        itensTributosIcms['cst'] = '00'
        itensTributosIcms['aliquota'] = '0'
        itensTributosIcms['valor'] = '0'
        itensTributosIcmsBaseCalculo['modalidadeDeterminacao'] = '0'
        itensTributosIcmsBaseCalculo['valor'] = '0'
        itensTributosIcms['baseCalculo'] = itensTributosIcmsBaseCalculo

        itensTributosPis['cst'] = '00'
        itensTributosPis['aliquota'] = '0'
        itensTributosPis['valor'] = '0'
        itensTributosPisBaseCalculo['valor'] = '0'
        itensTributosPisBaseCalculo['quantidade'] = '0'
        itensTributosPis['baseCalculo'] = itensTributosPisBaseCalculo

        itensTributosCofins['cst'] = '07'
        itensTributosCofins['aliquota'] = '0'
        itensTributosCofins['valor'] = '0'
        itensTributosCofinsBaseCalculo['valor'] = '0'
        itensTributosCofins['baseCalculo'] = itensTributosCofinsBaseCalculo

        itensTributos['icms'] = itensTributosIcms
        itensTributos['pis'] = itensTributosPis
        itensTributos['cofins'] = itensTributosCofins

        itens['tributos'] = itensTributos

        return itens

    def serializar_pagamentos(self):
        pagamentos = {}
        pagamentos['aVista'] = 'true'
        pagamentos['meio'] = '01'
        pagamentos['valor'] = '4.6'
        return pagamentos

    def serializar_responsavelTecnico(self):
        responsavelTecnico = {}
        responsavelTecnicoTelefone = {}
        responsavelTecnico['cpfCnpj'] = '68080571000117'
        responsavelTecnico['nome'] = 'Tompast Tecnologia da Informação LTDA'
        responsavelTecnico['email'] = 'suporte@startupcode.com.br'
        responsavelTecnicoTelefone['ddd'] = '44'
        responsavelTecnicoTelefone['numero'] = '30379500'
        responsavelTecnico['telefone'] = responsavelTecnicoTelefone
        return responsavelTecnico


data = {}
instance = SerializacaoJSON(homologacao=False)
data['emitente'] = instance.serializar_emitente(cpfCnpj='08187168000160')
data['destinatario'] = instance.serialize_recipient(cpfCnpj='08114280956',
                                                    razaoSocial='Teste')
data['itens'] = instance.serializar_itens()
data['pagamentos'] = instance.serializar_pagamentos()
data['responsavelTecnico'] = instance.serializar_responsavelTecnico()

json_data = json.dumps(data)

print(json.dumps(data, indent=4, sort_keys=False))