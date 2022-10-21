from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

import numpy as np

import pandas as pd


@api_view(["GET"])
def dgt(request):

    # me descargo el excel en formato csv

    aprobados_por_mes = []
    presentados_por_mes = []
    porcentaje_de_aprobados = []

    porcentaje_de_aprobados_total = []
    aprobados_total = []
    presentados_total = []
    presentados_total_promedio = []

    datos_por_autoescuela = {}

    try:
        for x in range(1, 12):

            data = pd.read_csv(
                "./dumps_autoescuela/export_auto_20220" + str(x) + "01.txt",
                sep=";",
                encoding="latin-1",
            )
            data = data.loc[data["CENTRO_EXAMEN"].isin(["Palmas de Gran Canaria, Las"])]

            for x in data["NOMBRE_AUTOESCUELA"].unique():

                segun_carnet = {}
                for y in data.loc[data["NOMBRE_AUTOESCUELA"].isin([x])][
                    "NOMBRE_PERMISO"
                ]:

                    data2 = data.loc[data["NOMBRE_AUTOESCUELA"].isin([x])].loc[
                        data["NOMBRE_PERMISO"].isin([y])
                    ]

                    segun_carnet[y] = {}

                aprobados_teorico = data.loc[data["NOMBRE_AUTOESCUELA"].isin([x])][
                    data["TIPO_EXAMEN"].isin(["PRUEBA TEÓRICA"])
                ]["NUM_APTOS"].sum()
                presentaciones_teorico = (
                    aprobados_teorico
                    + data.loc[data["NOMBRE_AUTOESCUELA"].isin([x])][
                        data["TIPO_EXAMEN"].isin(["PRUEBA TEÓRICA"])
                    ]["NUM_NO_APTOS"].sum()
                )

                aprobados_teorico_especifico = data.loc[
                    data["NOMBRE_AUTOESCUELA"].isin([x])
                ][data["TIPO_EXAMEN"].isin(["PRUEBA ESPECÍFICO"])]["NUM_APTOS"].sum()
                presentaciones_teorico_especifico = (
                    aprobados_teorico_especifico
                    + data.loc[data["NOMBRE_AUTOESCUELA"].isin([x])][
                        data["TIPO_EXAMEN"].isin(["PRUEBA ESPECÍFICO"])
                    ]["NUM_NO_APTOS"].sum()
                )

                aprobados_practico = data.loc[data["NOMBRE_AUTOESCUELA"].isin([x])][
                    data["TIPO_EXAMEN"].isin(["PRUEBA CONDUCCIÓN Y CIRCULACIÓN"])
                ]["NUM_APTOS"].sum()
                presentaciones_practico = (
                    aprobados_practico
                    + data.loc[data["NOMBRE_AUTOESCUELA"].isin([x])][
                        data["TIPO_EXAMEN"].isin(["PRUEBA CONDUCCIÓN Y CIRCULACIÓN"])
                    ]["NUM_NO_APTOS"].sum()
                )

                aprobados_practico_circuito_cerrado = data.loc[
                    data["NOMBRE_AUTOESCUELA"].isin([x])
                ][data["TIPO_EXAMEN"].isin(["PRUEBA DESTREZA"])]["NUM_APTOS"].sum()
                presentaciones_practico_circuito_cerrado = (
                    aprobados_practico_circuito_cerrado
                    + data.loc[data["NOMBRE_AUTOESCUELA"].isin([x])][
                        data["TIPO_EXAMEN"].isin(["PRUEBA DESTREZA"])
                    ]["NUM_NO_APTOS"].sum()
                )

                final_data = {
                    "total_aprobados_teorico": aprobados_teorico
                    + (
                        datos_por_autoescuela[x]["total_aprobados_teorico"]
                        if x in datos_por_autoescuela
                        else 0
                    ),
                    "total_presentados_teorico": presentaciones_teorico
                    + (
                        datos_por_autoescuela[x]["total_presentados_teorico"]
                        if x in datos_por_autoescuela
                        else 0
                    ),
                    "presentados_teorico_por_mes": (
                        datos_por_autoescuela[x]["presentados_teorico_por_mes"]
                        if x in datos_por_autoescuela
                        else []
                    )
                    + [presentaciones_teorico],
                    "aprobados_teorico_por_mes": (
                        datos_por_autoescuela[x]["aprobados_teorico_por_mes"]
                        if x in datos_por_autoescuela
                        else []
                    )
                    + [aprobados_teorico],
                    "porcentaje_aprobados_teorico_por_mes": (
                        (
                            datos_por_autoescuela[x][
                                "porcentaje_aprobados_teorico_por_mes"
                            ]
                        )
                        if x in datos_por_autoescuela
                        else []
                    )
                    + [
                        aprobados_teorico
                        / (presentaciones_teorico if presentaciones_teorico > 0 else 1)
                    ],
                    # TEORICO ESPECIFICO
                    "presentados_teorico_especifico_por_mes": (
                        datos_por_autoescuela[x][
                            "presentados_teorico_especifico_por_mes"
                        ]
                        if x in datos_por_autoescuela
                        else []
                    )
                    + [presentaciones_teorico_especifico],
                    "aprobados_teorico_especifico_por_mes": (
                        datos_por_autoescuela[x]["aprobados_teorico_especifico_por_mes"]
                        if x in datos_por_autoescuela
                        else []
                    )
                    + [aprobados_teorico_especifico],
                    "porcentaje_aprobados_teorico_especifico_por_mes": (
                        (
                            datos_por_autoescuela[x][
                                "porcentaje_aprobados_teorico_especifico_por_mes"
                            ]
                        )
                        if x in datos_por_autoescuela
                        else []
                    )
                    + [
                        aprobados_teorico_especifico
                        / (
                            presentaciones_teorico_especifico
                            if presentaciones_teorico_especifico > 0
                            else 1
                        )
                    ],
                    # PRACTICO
                    "presentados_practico_por_mes": (
                        datos_por_autoescuela[x]["presentados_practico_por_mes"]
                        if x in datos_por_autoescuela
                        else []
                    )
                    + [presentaciones_practico],
                    "aprobados_practico_por_mes": (
                        datos_por_autoescuela[x]["aprobados_practico_por_mes"]
                        if x in datos_por_autoescuela
                        else []
                    )
                    + [aprobados_practico],
                    "porcentaje_aprobados_practico_por_mes": (
                        (
                            datos_por_autoescuela[x][
                                "porcentaje_aprobados_practico_por_mes"
                            ]
                        )
                        if x in datos_por_autoescuela
                        else []
                    )
                    + [
                        aprobados_practico
                        / (
                            presentaciones_practico
                            if presentaciones_practico > 0
                            else 1
                        )
                    ],
                    # PRACTICO CIRCUITO CERRADO
                    "presentados_practico_circuito_cerrado_por_mes": (
                        datos_por_autoescuela[x][
                            "presentados_practico_circuito_cerrado_por_mes"
                        ]
                        if x in datos_por_autoescuela
                        else []
                    )
                    + [presentaciones_practico_circuito_cerrado],
                    "aprobados_practico_circuito_cerrado_por_mes": (
                        datos_por_autoescuela[x][
                            "aprobados_practico_circuito_cerrado_por_mes"
                        ]
                        if x in datos_por_autoescuela
                        else []
                    )
                    + [aprobados_practico_circuito_cerrado],
                    "porcentaje_aprobados_practico_circuito_cerrado_por_mes": (
                        (
                            datos_por_autoescuela[x][
                                "porcentaje_aprobados_practico_circuito_cerrado_por_mes"
                            ]
                        )
                        if x in datos_por_autoescuela
                        else []
                    )
                    + [
                        aprobados_practico_circuito_cerrado
                        / (
                            presentaciones_practico_circuito_cerrado
                            if presentaciones_practico_circuito_cerrado > 0
                            else 1
                        )
                    ],
                    "segun_carnet": segun_carnet,
                }

                datos_por_autoescuela[x] = final_data
    except:
        print("error")

    return Response(datos_por_autoescuela)
