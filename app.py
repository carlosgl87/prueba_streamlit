import pandas as pd
import numpy as np
from hdbcli import dbapi
import time 
import streamlit as st

pd.options.display.max_columns = None
starttime=time.time()
address_name = str('zeus.hana.prod.us-east-1.whitney.dbaas.ondemand.com')

port_name = str('26613')
user_name = str('USER_PBI')
pwd_name = str('Un19u3.2020')

conn = dbapi.connect(
address=address_name,
port=port_name,
encrypt="true",
user=user_name,
password=pwd_name,
sslValidateCertificate="false")

sql_query = '''
select VCH_COD_PAIS_CORP as COD_PAIS,VCH_DES_PAIS, CHRCODIGOPRODUCTO as VCH_COD_PRODUCTO, AVG(MNYCOSTOBASEUSD) COSTO_USD  
from \"EDW_CORPORACION\".\"EDW_CORPORACION.shahdb_corporacion.CalculationViews.Marketing.Ventas_Corp.Fact::CV_COSTOS\" 
where  INTSEMANAANUALINVENTARIO LIKE '2021%' AND MNYCOSTOESTANDARUSD > 0 GROUP BY VCH_COD_PAIS_CORP, VCH_DES_PAIS, CHRCODIGOPRODUCTO;
'''

costos = pd.read_sql(sql_query,conn)

st.table(costos.head())

