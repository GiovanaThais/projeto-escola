from rest_framework import serializers 
from .models import Curso, Avaliacao
from django.db.models import Avg #funcao de media


class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'nota',
            'criacao',
            'ativo'
        )
    def validate_avaliacao(self, valor):
        if valor in range(1, 6):  # 1, 2, 3, 4, 5
            return valor
        raise serializers.ValidationError('A avaliação precisa ser um inteiro entre 1 e 5')
class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields= '__all__'

    media_avaliacoes = serializers.SerializerMethodField()

    def get_media_avaliacoes(self, obj):
        media = obj.avaliacoes.aggregate(Avg('avaliacao')).get('avaliacao__avg')

        if media is None:
            return 0
        return round(media * 2) / 2