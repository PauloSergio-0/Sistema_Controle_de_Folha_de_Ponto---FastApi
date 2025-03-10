from fastapi import UploadFile
import io
import pandas as pd


class Service_funcionario:
    
    async def importar_funcionario(File: UploadFile):
        if File.filename.endswith('.csv'):
            
            data = await File.read()
            data_decode= io.StringIO(data.decode('utf-8'))
            
            funcionario_data= pd.read_csv(data_decode, sep=',')
            print(funcionario_data)