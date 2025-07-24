from rest_framework import serializers

from api.produtor.models import Produtor


class ProdutorSerializer(serializers.ModelSerializer):
    cpf_cnpj_mascara = serializers.SerializerMethodField()

    class Meta:
        model = Produtor
        fields = '__all__'

    def get_cpf_cnpj_mascara(self, obj):
        cpf_cnpj = ''
        if len(obj.cpf_cnpj) == 11:
            cpf_cnpj = obj.cpf_cnpj[:3] + '.' + obj.cpf_cnpj[3:6] + '.' + obj.cpf_cnpj[6:9] + '-' + obj.cpf_cnpj[9:]
        if len(obj.cpf_cnpj) == 14:
            cpf_cnpj = obj.cpf_cnpj[:2] + '.' + obj.cpf_cnpj[2:5] + '.' + obj.cpf_cnpj[5:8] + '/' + obj.cpf_cnpj[8:12] + '-' + obj.cpf_cnpj[12:]
        return cpf_cnpj
