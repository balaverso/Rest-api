from sql_alchemy import banco

class MoedaModel(banco.Model):
    __tablename__ = 'hoteis'

    moeda_id = banco.Column(banco.String, primary_key=True)
    nome = banco.Column(banco.String(80))
    fechou = banco.Column(banco.Float(precision=1))
    volume = banco.Column(banco.Float(precision=2))
    categoria = banco.Column(banco.String(40))

    def __init__(self, moeda_id, nome, fechou, volume, categoria):
        self.moeda_id = moeda_id
        self.nome = nome
        self.fechou = fechou
        self.volume = volume
        self.categoria = categoria

    def json(self):
        return {
            'moeda_id': self.moeda_id,
            'nome': self.nome,
            'fechou': self.fechou,
            'volume': self.volume,
            'categoria': self.categoria
        }

    @classmethod
    def find_moeda(cls, moeda_id):
        moeda = cls.query.filter_by(moeda_id=moeda_id).first()
        if moeda:
            return moeda
        return None

    def save_moeda(self):
        banco.session.add(self)
        banco.session.commit()

    def update_moeda(self, nome, fechou, volume, categoria):
        self.nome = nome
        self.fechou = fechou
        self.volume = volume
        self.categoria = categoria

    def delete_moeda(self):
        banco.session.delete(self)
        banco.session.commit()
