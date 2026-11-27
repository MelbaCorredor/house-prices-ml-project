import sys
print("Python usado:", sys.executable)

import argparse
import sys
import zipfile
from pathlib import Path

import pandas as pd

# ---------------------------------------------------------------------------
# Configuración
# ---------------------------------------------------------------------------
COMPETENCIA = "house-prices-advanced-regression-techniques"

# Raíz del repositorio: este archivo está en scripts/data_acquisition/main.py
RAIZ_REPO = Path(__file__).resolve().parents[2]
DIR_DATOS_DEFECTO = RAIZ_REPO / "data" / "raw"

ARCHIVOS_ESPERADOS = [
    "train.csv",
    "test.csv",
    "data_description.txt",
    "sample_submission.csv",
]

VARIABLE_OBJETIVO = "SalePrice"
LLAVE = "Id"

# Tamaños conocidos del dataset publicado en Kaggle
FILAS_TRAIN_ESPERADAS = 1460
FILAS_TEST_ESPERADAS = 1459
COLUMNAS_TRAIN_ESPERADAS = 81  # Id + 79 variables explicativas + SalePrice
COLUMNAS_TEST_ESPERADAS = 80   # Id + 79 variables explicativas


# ---------------------------------------------------------------------------
# 1. Descarga
# ---------------------------------------------------------------------------
def archivos_presentes(directorio: Path) -> bool:
    """Indica si todos los archivos esperados ya existen en el directorio."""
    return all((directorio / nombre).exists() for nombre in ARCHIVOS_ESPERADOS)


def descargar_datos(directorio: Path, forzar: bool = False) -> None:
    """Descarga y descomprime los archivos de la competencia en `directorio`."""
    directorio.mkdir(parents=True, exist_ok=True)

    if archivos_presentes(directorio) and not forzar:
        print(f"[INFO] Los datos ya existen en {directorio}. Se omite la descarga "
              "(use --force para volver a descargar).")
        return

    # La librería kaggle intenta autenticarse al importarse; por eso se importa
    # aquí y se capturan los errores para dar un mensaje claro.
    try:
        from kaggle.api.kaggle_api_extended import KaggleApi
    except ImportError:
        sys.exit("[ERROR] No está instalada la librería 'kaggle'. "
                 "Instálela con: pip install kaggle")
    except (OSError, ValueError) as error:
        sys.exit(f"[ERROR] No se encontraron credenciales de Kaggle: {error}\n"
                 "Ubique kaggle.json en ~/.kaggle/ o defina KAGGLE_USERNAME y KAGGLE_KEY.")

    api = KaggleApi()
    try:
        api.authenticate()
    except Exception as error:  # noqa: BLE001 - se informa cualquier fallo de autenticación
        sys.exit(f"[ERROR] Falló la autenticación con Kaggle: {error}")

    print(f"[INFO] Descargando la competencia '{COMPETENCIA}' en {directorio} ...")
    try:
        api.competition_download_files(COMPETENCIA, path=str(directorio), quiet=False)
    except Exception as error:  # noqa: BLE001
        sys.exit(f"[ERROR] No se pudo descargar la competencia: {error}\n"
                 "Verifique que aceptó las reglas en "
                 f"https://www.kaggle.com/c/{COMPETENCIA}/rules")

    archivo_zip = directorio / f"{COMPETENCIA}.zip"
    if archivo_zip.exists():
        print(f"[INFO] Descomprimiendo {archivo_zip.name} ...")
        with zipfile.ZipFile(archivo_zip) as zf:
            zf.extractall(directorio)
        archivo_zip.unlink()  # se elimina el .zip para no duplicar los datos

    faltantes = [n for n in ARCHIVOS_ESPERADOS if not (directorio / n).exists()]
    if faltantes:
        sys.exit(f"[ERROR] Después de la descarga faltan archivos: {faltantes}")
    print("[INFO] Descarga completada.")


# ---------------------------------------------------------------------------
# 2. Carga
# ---------------------------------------------------------------------------
def cargar_datos(directorio: Path = DIR_DATOS_DEFECTO) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Carga train.csv y test.csv y los retorna como DataFrames.

    Nota: pandas lee el texto "NA" como valor nulo. En este dataset, en
    varias variables categóricas "NA" significa "no tiene" (p. ej. sin
    piscina, sin sótano, sin garaje) y no un dato perdido. Esto se tendrá
    en cuenta en la etapa de preprocesamiento (ver diccionario de datos).
    """
    train = pd.read_csv(directorio / "train.csv")
    test = pd.read_csv(directorio / "test.csv")
    return train, test


# ---------------------------------------------------------------------------
# 3. Validación
# ---------------------------------------------------------------------------
def validar_datos(train: pd.DataFrame, test: pd.DataFrame) -> list[str]:
    """Revisa que los datos cargados sean los esperados. Retorna la lista de problemas."""
    problemas = []

    if train.shape != (FILAS_TRAIN_ESPERADAS, COLUMNAS_TRAIN_ESPERADAS):
        problemas.append(f"train tiene forma {train.shape}, se esperaba "
                         f"({FILAS_TRAIN_ESPERADAS}, {COLUMNAS_TRAIN_ESPERADAS})")
    if test.shape != (FILAS_TEST_ESPERADAS, COLUMNAS_TEST_ESPERADAS):
        problemas.append(f"test tiene forma {test.shape}, se esperaba "
                         f"({FILAS_TEST_ESPERADAS}, {COLUMNAS_TEST_ESPERADAS})")

    if VARIABLE_OBJETIVO not in train.columns:
        problemas.append(f"train no contiene la variable objetivo '{VARIABLE_OBJETIVO}'")
    else:
        if train[VARIABLE_OBJETIVO].isna().any():
            problemas.append(f"'{VARIABLE_OBJETIVO}' tiene valores nulos")
        if (train[VARIABLE_OBJETIVO] <= 0).any():
            problemas.append(f"'{VARIABLE_OBJETIVO}' tiene valores menores o iguales a 0")

    if VARIABLE_OBJETIVO in test.columns:
        problemas.append(f"test no debería contener '{VARIABLE_OBJETIVO}'")

    columnas_train = set(train.columns) - {VARIABLE_OBJETIVO}
    if columnas_train != set(test.columns):
        diferencia = columnas_train.symmetric_difference(test.columns)
        problemas.append(f"train y test no tienen las mismas variables: {sorted(diferencia)}")

    for nombre, df in (("train", train), ("test", test)):
        if LLAVE not in df.columns:
            problemas.append(f"{nombre} no contiene la llave '{LLAVE}'")
        elif not df[LLAVE].is_unique:
            problemas.append(f"{nombre} tiene valores repetidos en '{LLAVE}'")

    if LLAVE in train.columns and LLAVE in test.columns:
        if set(train[LLAVE]) & set(test[LLAVE]):
            problemas.append("hay Ids que aparecen en train y en test a la vez")

    return problemas


# ---------------------------------------------------------------------------
# 4. Resumen
# ---------------------------------------------------------------------------
def resumen_datos(train: pd.DataFrame, test: pd.DataFrame) -> None:
    """Imprime un resumen inicial de los datos cargados."""
    print("\n" + "=" * 70)
    print("RESUMEN DE LOS DATOS CARGADOS")
    print("=" * 70)
    print(f"train: {train.shape[0]:,} filas x {train.shape[1]} columnas")
    print(f"test : {test.shape[0]:,} filas x {test.shape[1]} columnas")

    explicativas = train.drop(columns=[LLAVE, VARIABLE_OBJETIVO])
    numericas = explicativas.select_dtypes(include="number").columns
    categoricas = explicativas.select_dtypes(exclude="number").columns
    print(f"\nVariables explicativas: {explicativas.shape[1]} "
          f"({len(numericas)} numéricas, {len(categoricas)} categóricas)")

    print(f"\nVariable objetivo '{VARIABLE_OBJETIVO}' (dólares):")
    print(train[VARIABLE_OBJETIVO].describe().map("{:,.0f}".format).to_string())

    nulos = train.isna().sum()
    nulos = nulos[nulos > 0].sort_values(ascending=False)
    print(f"\nColumnas con valores faltantes en train: {len(nulos)}")
    if not nulos.empty:
        tabla = pd.DataFrame({"nulos": nulos, "% nulos": (nulos / len(train) * 100).round(1)})
        print(tabla.to_string())

    print("\nPrimeras filas de train:")
    with pd.option_context("display.max_columns", 10, "display.width", 120):
        print(train.head())


# ---------------------------------------------------------------------------
# Programa principal
# ---------------------------------------------------------------------------
def main() -> None:
    parser = argparse.ArgumentParser(
        description="Descarga, carga y valida el dataset House Prices de Kaggle.")
    parser.add_argument("--output-dir", type=Path, default=DIR_DATOS_DEFECTO,
                        help=f"Carpeta donde se guardan los datos (por defecto: {DIR_DATOS_DEFECTO})")
    parser.add_argument("--force", action="store_true",
                        help="Vuelve a descargar los datos aunque ya existan.")
    args = parser.parse_args()

    descargar_datos(args.output_dir, forzar=args.force)
    train, test = cargar_datos(args.output_dir)

    problemas = validar_datos(train, test)
    if problemas:
        print("\n[ADVERTENCIA] La validación encontró problemas:")
        for problema in problemas:
            print(f"  - {problema}")
    else:
        print("\n[OK] Validación superada: los datos están completos y son consistentes.")

    resumen_datos(train, test)


if __name__ == "__main__":
    main()
