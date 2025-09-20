import re
from backEnd.infrastructure.database import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from backEnd.infrastructure.database.models import LavouraPermanente
from sqlalchemy import text , create_engine , func , case 
from backEnd.service.criptografia import CriptografiaSimetrica , JWTManager
from sqlalchemy.orm import Session

class LavouraService:
    def __init__(self , db: SQLAlchemy):
        self.db = db


    def rendimento_ponderado_por_uf(self , ano):
        
        subquery = (
            self.db.session.query(
                LavouraPermanente.sigla_uf.label("uf"),
                (
                    func.sum(
                        LavouraPermanente.rendimento_medio_producao *
                        LavouraPermanente.area_colhida
                    ) /
                    func.nullif(func.sum(LavouraPermanente.area_colhida), 0)
                ).label("rendimento_ponderado")
            )
            .filter(LavouraPermanente.ano == ano )
            .group_by(LavouraPermanente.sigla_uf)
        )
        return subquery.all()
    
    def indicadores_agricolas(self, ano: str):
        query = (
            self.db.session.query(
                func.sum(LavouraPermanente.area_destinada_colheita).label("total_area_destinada"),
                func.sum(LavouraPermanente.quantidade_produzida).label("total_quantidade"),
                (
                    func.sum(LavouraPermanente.rendimento_medio_producao * LavouraPermanente.area_colhida)
                    / func.nullif(func.sum(LavouraPermanente.area_colhida), 0)
                ).label("rendimento_medio_ponderado")
            )
            .filter(LavouraPermanente.ano == ano)
        )
        result = query.one()
        
        return {
            "ano": ano,
            "total_area_destinada": float(result.total_area_destinada or 0),
            "total_quantidade": float(result.total_quantidade or 0),
            "rendimento_medio_ponderado": float(result.rendimento_medio_ponderado or 0),
        }