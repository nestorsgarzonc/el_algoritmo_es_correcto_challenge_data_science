from xgboost import XGBRegressor
import pandas as pd
import joblib


class ModelData():
    def __init__(self, area=0, banos=0, estrato=0, garajes=0, habitaciones=0, piso=0, valoradministracion=0, valorventa=0, latitud=0, longitud=0, anos_0_1=0, anos_1_10=0, anos_10_30=0, anos_30=0, tiponegocio_Arriendo=0, tiponegocio_Venta=0, tiponegocio_Venta_Y_Arriendo=0, tipoinmueble_Casa=0, tipoinmueble_Apartamento=0):
        self.area = area
        self.banos = banos
        self.estrato = estrato
        self.garajes = garajes
        self.habitaciones = habitaciones
        self.piso = piso
        self.valoradministracion = valoradministracion
        self.valorventa = valorventa
        self.latitud = latitud
        self.longitud = longitud
        self.anos_0_1 = anos_0_1
        self.anos_1_10 = anos_1_10
        self.anos_10_30 = anos_10_30
        self.anos_30 = anos_30
        self.tiponegocio_Arriendo = tiponegocio_Arriendo
        self.tiponegocio_Venta = tiponegocio_Venta
        self.tiponegocio_Venta_Y_Arriendo = tiponegocio_Venta_Y_Arriendo
        self.tipoinmueble_Casa = tipoinmueble_Casa
        self.tipoinmueble_Apartamento = tipoinmueble_Apartamento

    def to_arr(self):
        return [
            self.area,
            self.banos,
            self.estrato,
            self.garajes,
            self.habitaciones,
            self.piso,
            self.valoradministracion,
            self.valorventa,
            self.latitud,
            self.longitud,
            self.anos_0_1,
            self.anos_1_10,
            self.anos_10_30,
            self.anos_30,
            self.tiponegocio_Arriendo,
            self.tiponegocio_Venta,
            self.tiponegocio_Venta_Y_Arriendo,
            self.tipoinmueble_Casa,
            self.tipoinmueble_Apartamento,
        ]

    def __str__(self):
        return f'''
        ###################################################################################
        ###################################################################################
        MODEL DATA: 
        area: {self.area}
        banos: {self.banos}
        estrato: {self.estrato}
        garajes: {self.garajes}
        habitaciones: {self.habitaciones}
        piso: {self.piso}
        valoradministracion: {self.valoradministracion}
        valorventa: {self.valorventa}
        latitud: {self.latitud}
        longitud: {self.longitud}
        anos_0_1: {self.anos_0_1}
        anos_1_10: {self.anos_1_10}
        anos_10_30: {self.anos_10_30}
        anos_30: {self.anos_30}
        tiponegocio_Arriendo: {self.tiponegocio_Arriendo}
        tiponegocio_Venta: {self.tiponegocio_Venta}
        tiponegocio_Venta_Y_Arri: {self.tiponegocio_Venta_Y_Arriendo}
        tipoinmueble_Casa: {self.tipoinmueble_Casa}
        tipoinmueble_Apartamento: {self.tipoinmueble_Apartamento}
        ###################################################################################
        ###################################################################################
        '''


class XGBoost:
    def __init__(self):
        self.xgBoost = XGBRegressor()
        self.cols = [
            'area', 'banos', 'estrato', 'garajes', 'habitaciones', 'piso',
            'valoradministracion', 'valorventa', 'latitud', 'longitud', '0-1 anos', '1-10 anos',
            '10-30 anos', '30 anos', 'tiponegocio_Arriendo', 'tiponegocio_Venta',
            'tiponegocio_Venta Y Arriendo', 'tipoinmueble_Casa',
            'tipoinmueble_Apartamento'
        ]

    def load_model(self, path='./ai/sklearn_pipeline.pkl'):
        self.xgBoost = joblib.load(path)
    
    def predict(self, arr: list) -> list:
        df = pd.DataFrame(data=arr).T
        df.columns = self.cols
        return self.xgBoost.predict(df)


if __name__ == '__main__':
    model = XGBoost()
    model.load_model()
    data = ModelData(
        104, 2, 2, 1,
        3, 3, 0, 185000000,
        4.71150, - 74.13238, 0, 0,
        0, 0, 0, 1,
        0, 1, 0
    )
    res = model.predict(data.to_arr())
    # res = model.predict(
    #     [
    #         104, 2, 2, 1,
    #         3, 3, 0, 185000000,
    #         4.71150, - 74.13238, 0, 0,
    #         0, 0, 0, 1,
    #         0, 1, 0
    #     ]
    # )
    print(res)
