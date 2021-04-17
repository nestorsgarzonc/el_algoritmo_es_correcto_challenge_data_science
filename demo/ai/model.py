from xgboost import XGBRegressor
import pandas as pd
import joblib


class XGBoost:
    def __init__(self):
        self.xgBoost = XGBRegressor()
        self.cols = ['area', 'banos', 'estrato', 'garajes', 'habitaciones', 'piso',
                     'valoradministracion', 'valorventa', 'latitud', 'longitud', '0-1 anos', '1-10 anos',
                     '10-30 anos', '30 anos', 'tiponegocio_Arriendo', 'tiponegocio_Venta',
                     'tiponegocio_Venta Y Arriendo', 'tipoinmueble_Casa',
                     'tipoinmueble_Apartamento'
                     ]

    def load_model(self, path='./sklearn_pipeline.pkl'):
        self.xgBoost = joblib.load(path)

    def predict(self, arr: list) -> list:
        df = pd.DataFrame(data=arr).T
        df.columns = self.cols
        print(df)
        return self.xgBoost.predict(df)


if __name__ == '__main__':
    model = XGBoost()
    model.load_model()
    res = model.predict(
        [
            104, 2, 2, 1,
            3, 3, 0, 185000000,
            4.71150, - 74.13238, 0, 0,
            0, 0, 0, 1,
            0, 1, 0
        ]
    )
    print(res)
