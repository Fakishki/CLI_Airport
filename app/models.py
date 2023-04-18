# Import Any Additional sqlalchemy types here
from sqlalchemy import Column, Integer, String, ForeignKey 
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Models:
# class Model(Base):
#   __tablename__ = "models"
#   __table_arge__ = (TableArgsAsTuple)
#   
#   Setup Columns and DataTypes
#   
#   Setup Relationships
# 
#   Optional:
#   def __repr__(self): 
#     return "A Better Print Output"
