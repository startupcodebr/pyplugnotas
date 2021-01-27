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

    def serialize_issuer(self, cpfCnpj):
        issuer = {}
        issuer['cpfCnpj'] = cpfCnpj

        return issuer

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

    def serializer_items(self):

        items = {}
        itemsValueUnit = {}
        itemsTributes = {}
        itemsTributesIcms = {}
        itemsTributesIcmsBaseCalculation = {}
        itemsTributesPis = {}
        itemsTributesPisBaseCalculation = {}
        itemsTributesCofins = {}
        itemsTributesCofinsBaseCalculation = {}

        items['codigo'] = '1'
        items[
            'descricao'] = 'NOTA FISCAL EMITIDA EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL'
        items['ncm'] = '06029090'
        items['cest'] = '0123456'
        items['cfop'] = '5101'
        itemsValueUnit['comercial'] = '4.6'
        itemsValueUnit['tributavel'] = '4.6'
        items['valorUnitario'] = itemsValueUnit
        items['valor'] = '4.6'

        itemsTributesIcms['origem'] = '0'
        itemsTributesIcms['cst'] = '00'
        itemsTributesIcms['aliquota'] = '0'
        itemsTributesIcms['valor'] = '0'
        itemsTributesIcmsBaseCalculation['modalidadeDeterminacao'] = '0'
        itemsTributesIcmsBaseCalculation['valor'] = '0'
        itemsTributesIcms['baseCalculo'] = itemsTributesIcmsBaseCalculation

        itemsTributesPis['cst'] = '00'
        itemsTributesPis['aliquota'] = '0'
        itemsTributesPis['valor'] = '0'
        itemsTributesPisBaseCalculation['valor'] = '0'
        itemsTributesPisBaseCalculation['quantidade'] = '0'
        itemsTributesPis['baseCalculo'] = itemsTributesPisBaseCalculation
        itemsTributesCofins['cst'] = '07'
        itemsTributesCofins['aliquota'] = '0'
        itemsTributesCofins['valor'] = '0'
        itemsTributesCofinsBaseCalculation['valor'] = '0'
        itemsTributesCofins['baseCalculo'] = itemsTributesCofinsBaseCalculation

        itemsTributes['icms'] = itemsTributesIcms
        itemsTributes['pis'] = itemsTributesPis
        itemsTributes['cofins'] = itemsTributesCofins

        items['tributos'] = itemsTributes

        return items

    def serialize_payments(self):
        payments = {}
        payments['aVista'] = 'true'
        payments['meio'] = '01'
        payments['valor'] = '4.6'

        return payments

    def serialize_responsible(self):
        responsibleTechnician = {}
        responsibleTechnicianPhone = {}
        responsibleTechnician['cpfCnpj'] = '68080571000117'
        responsibleTechnician['nome'] = 'Tompast Tecnologia da Informação LTDA'
        responsibleTechnician['email'] = 'suporte@startupcode.com.br'
        responsibleTechnicianPhone['ddd'] = '44'
        responsibleTechnicianPhone['numero'] = '30379500'
        responsibleTechnician['telefone'] = responsibleTechnicianPhone

        return responsibleTechnician

    def json_data(self):
        data = {}
        instance = SerializacaoJSON(homologacao=False)
        data['emitente'] = instance.serialize_issuer(cpfCnpj='08187168000160')
        data['destinatario'] = instance.serialize_recipient(
            cpfCnpj='08114280956',
            razaoSocial='Teste',
        )
        data['itens'] = instance.serializer_items()
        data['pagamentos'] = instance.serialize_payments()
        data['responsavelTecnico'] = instance.serialize_responsible()
        json_data = json.dumps(data)

        return json_data

    def post_nfe(self, apikey, payload):
        url = "https://api.sandbox.plugnotas.com.br/nfe"
        headers = {'x-api-key': apikey, 'Content-Type': 'application/json'}

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text.encode('utf8'))