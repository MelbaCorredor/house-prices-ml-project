# Diccionario de datos

Proyecto: **Predicción del precio de venta de viviendas residenciales en Ames, Iowa**.

Fuente general: competencia de Kaggle *House Prices – Advanced Regression Techniques* (https://www.kaggle.com/c/house-prices-advanced-regression-techniques). Los datos los compiló Dean De Cock (Truman State University) a partir de los registros de avalúo de la ciudad de Ames, Iowa (Ames City Assessor's Office), para ventas de viviendas entre 2006 y 2010. Las descripciones se tradujeron y adaptaron del archivo oficial `data_description.txt`. Los rangos y valores faltantes se calcularon directamente sobre los archivos.

Unidades: las áreas están en pies cuadrados (1 pie² ≈ 0,093 m²), las longitudes en pies (1 pie ≈ 0,305 m) y los valores monetarios en dólares estadounidenses.

## Base de datos 1

**train.csv** – Conjunto de entrenamiento. Tiene 1.460 viviendas vendidas (una fila por venta) y 81 columnas: el identificador `Id`, 79 variables explicativas (35 numéricas y 44 categóricas, contando `MSSubClass` como categórica aunque esté codificada con números) y la variable objetivo `SalePrice`. Se usa para entrenar y validar los modelos.

**Nota sobre los valores faltantes:** en varias variables categóricas el código `NA` no es un dato perdido, sino que significa que la vivienda *no tiene* ese elemento (sin callejón, sótano, chimenea, garaje, piscina, cerca o característica adicional). pandas lee `NA` y `None` como nulos, así que esos casos aparecen como faltantes. En el preprocesamiento se deben reemplazar por una categoría como "Ninguno" y no imputar. Los faltantes reales son pocos (por ejemplo `LotFrontage`, `MasVnrArea`, `Electrical`). `GarageYrBlt` queda vacío cuando la vivienda no tiene garaje.

| Variable | Descripción | Tipo de dato | Rango/Valores posibles | Fuente de datos |
| --- | --- | --- | --- | --- |
| Id | Identificador único de la vivienda (llave del registro). No se usa como predictor. | Entero (identificador) | 1 a 1.460 | Kaggle – train.csv |
| MSSubClass | Tipo de vivienda involucrada en la venta (código que combina número de pisos, antigüedad y tipo). | Categórica nominal (codificada como entero) | 20 = 1 piso, 1946 o más nueva; 30 = 1 piso, 1945 o más antigua; 40 = 1 piso con ático terminado; 45 = 1½ pisos sin terminar; 50 = 1½ pisos terminado; 60 = 2 pisos, 1946 o más nueva; 70 = 2 pisos, 1945 o más antigua; 75 = 2½ pisos; 80 = varios niveles (split/multi-level); 85 = split foyer; 90 = dúplex; 120 = 1 piso PUD (desarrollo planificado), 1946 o más nueva; 150 = 1½ pisos PUD; 160 = 2 pisos PUD, 1946 o más nueva; 180 = PUD multinivel; 190 = conversión a 2 familias | Kaggle – train.csv |
| MSZoning | Clasificación general de zonificación (uso del suelo) del predio. | Categórica nominal (texto) | A = agrícola; C (all) = comercial; FV = residencial Floating Village; I = industrial; RH = residencial alta densidad; RL = residencial baja densidad; RP = residencial baja densidad tipo parque; RM = residencial densidad media | Kaggle – train.csv |
| LotFrontage | Longitud del frente del lote que da a la calle. | Numérica continua (decimal) | 21 a 313 pies lineales. **Faltantes: 259 (17,7 %)** | Kaggle – train.csv |
| LotArea | Área del lote. | Numérica continua (entero) | 1.300 a 215.245 pies² | Kaggle – train.csv |
| Street | Tipo de vía de acceso a la propiedad. | Categórica nominal (texto) | Grvl = grava; Pave = pavimentada | Kaggle – train.csv |
| Alley | Tipo de acceso por callejón. | Categórica nominal (texto) | Grvl = grava; Pave = pavimentado; NA = sin acceso por callejón. **Faltantes: 1369 (93,8 %)** | Kaggle – train.csv |
| LotShape | Forma general del lote. | Categórica ordinal (texto) | Reg = regular; IR1 = ligeramente irregular; IR2 = moderadamente irregular; IR3 = irregular | Kaggle – train.csv |
| LandContour | Planitud del terreno. | Categórica nominal (texto) | Lvl = casi plano; Bnk = con talud (sube rápido desde la calle); HLS = ladera (pendiente lateral); Low = depresión | Kaggle – train.csv |
| Utilities | Servicios públicos disponibles. | Categórica ordinal (texto) | AllPub = todos los servicios (electricidad, gas, agua y alcantarillado); NoSewr = electricidad, gas y agua (pozo séptico); NoSeWa = solo electricidad y gas; ELO = solo electricidad | Kaggle – train.csv |
| LotConfig | Configuración del lote. | Categórica nominal (texto) | Inside = lote interior; Corner = esquinero; CulDSac = en calle sin salida; FR2 = frente a 2 calles; FR3 = frente a 3 calles | Kaggle – train.csv |
| LandSlope | Pendiente del terreno. | Categórica ordinal (texto) | Gtl = suave; Mod = moderada; Sev = fuerte | Kaggle – train.csv |
| Neighborhood | Barrio de Ames donde está la vivienda. | Categórica nominal (texto) | Blmngtn = Bloomington Heights; Blueste = Bluestem; BrDale = Briardale; BrkSide = Brookside; ClearCr = Clear Creek; CollgCr = College Creek; Crawfor = Crawford; Edwards; Gilbert; IDOTRR = Iowa DOT and Rail Road; MeadowV = Meadow Village; Mitchel = Mitchell; NAmes = North Ames; NoRidge = Northridge; NPkVill = Northpark Villa; NridgHt = Northridge Heights; NWAmes = Northwest Ames; OldTown = Old Town; SWISU = sur y oeste de Iowa State University; Sawyer; SawyerW = Sawyer West; Somerst = Somerset; StoneBr = Stone Brook; Timber = Timberland; Veenker | Kaggle – train.csv |
| Condition1 | Cercanía a condiciones del entorno (vías, ferrocarril, parques). | Categórica nominal (texto) | Artery = junto a avenida principal; Feedr = junto a vía colectora; Norm = normal; RRNn = a menos de 200 pies de vía férrea norte-sur; RRAn = junto a vía férrea norte-sur; PosN = cerca de un elemento positivo (parque, zona verde); PosA = junto a un elemento positivo; RRNe = a menos de 200 pies de vía férrea este-oeste; RRAe = junto a vía férrea este-oeste | Kaggle – train.csv |
| Condition2 | Segunda condición del entorno (si hay más de una). | Categórica nominal (texto) | Artery = junto a avenida principal; Feedr = junto a vía colectora; Norm = normal; RRNn = a menos de 200 pies de vía férrea norte-sur; RRAn = junto a vía férrea norte-sur; PosN = cerca de un elemento positivo (parque, zona verde); PosA = junto a un elemento positivo; RRNe = a menos de 200 pies de vía férrea este-oeste; RRAe = junto a vía férrea este-oeste | Kaggle – train.csv |
| BldgType | Tipo de edificación. | Categórica nominal (texto) | 1Fam = unifamiliar independiente; 2fmCon = conversión a 2 familias (construida para una); Duplex = dúplex; TwnhsE = casa adosada de esquina; Twnhs = casa adosada interior | Kaggle – train.csv |
| HouseStyle | Estilo de la vivienda (número de pisos y terminación). | Categórica nominal (texto) | 1Story = 1 piso; 1.5Fin = 1½ pisos, 2.º nivel terminado; 1.5Unf = 1½ pisos, 2.º nivel sin terminar; 2Story = 2 pisos; 2.5Fin = 2½ pisos, 2.º nivel terminado; 2.5Unf = 2½ pisos, 2.º nivel sin terminar; SFoyer = split foyer; SLvl = split level | Kaggle – train.csv |
| OverallQual | Calificación de la calidad general de materiales y acabados de la vivienda. | Categórica ordinal (entero 1–10) | 10 = muy excelente; 9 = excelente; 8 = muy bueno; 7 = bueno; 6 = sobre el promedio; 5 = promedio; 4 = bajo el promedio; 3 = regular; 2 = malo; 1 = muy malo | Kaggle – train.csv |
| OverallCond | Calificación del estado general de la vivienda. | Categórica ordinal (entero 1–10) | Misma escala que OverallQual: 10 = muy excelente … 1 = muy malo | Kaggle – train.csv |
| YearBuilt | Año de construcción original. | Numérica discreta (año) | 1.872 a 2.010 | Kaggle – train.csv |
| YearRemodAdd | Año de remodelación o ampliación (igual al año de construcción si no hubo). | Numérica discreta (año) | 1.950 a 2.010 | Kaggle – train.csv |
| RoofStyle | Tipo de techo. | Categórica nominal (texto) | Flat = plano; Gable = a dos aguas; Gambrel = tipo granero; Hip = a cuatro aguas; Mansard = mansarda; Shed = a un agua | Kaggle – train.csv |
| RoofMatl | Material del techo. | Categórica nominal (texto) | ClyTile = arcilla o teja; CompShg = teja compuesta estándar; Membran = membrana; Metal = metal; Roll = rollo; Tar&Grv = grava y alquitrán; WdShake = tablillas de madera; WdShngl = tejas de madera | Kaggle – train.csv |
| Exterior1st | Material de revestimiento exterior principal. | Categórica nominal (texto) | AsbShng = tejas de asbesto; AsphShn = tejas asfálticas; BrkComm = ladrillo común; BrkFace = ladrillo de fachada; CBlock = bloque de concreto; CemntBd = fibrocemento; HdBoard = tablero duro; ImStucc = estuco imitación; MetalSd = revestimiento metálico; Other = otro; Plywood = madera contrachapada; PreCast = prefabricado; Stone = piedra; Stucco = estuco; VinylSd = revestimiento de vinilo; Wd Sdng = revestimiento de madera; WdShing = tejas de madera | Kaggle – train.csv |
| Exterior2nd | Segundo material de revestimiento exterior (si hay más de uno). | Categórica nominal (texto) | AsbShng = tejas de asbesto; AsphShn = tejas asfálticas; BrkComm = ladrillo común; BrkFace = ladrillo de fachada; CBlock = bloque de concreto; CemntBd = fibrocemento; HdBoard = tablero duro; ImStucc = estuco imitación; MetalSd = revestimiento metálico; Other = otro; Plywood = madera contrachapada; PreCast = prefabricado; Stone = piedra; Stucco = estuco; VinylSd = revestimiento de vinilo; Wd Sdng = revestimiento de madera; WdShing = tejas de madera. En los datos algunos códigos aparecen escritos distinto: Brk Cmn, CmentBd, Wd Shng | Kaggle – train.csv |
| MasVnrType | Tipo de enchape de mampostería (ladrillo o piedra decorativa en la fachada). | Categórica nominal (texto) | BrkCmn = ladrillo común; BrkFace = ladrillo de fachada; CBlock = bloque de concreto; Stone = piedra; None = sin enchape. Ojo: pandas lee el texto "None" como nulo, por eso casi todos los faltantes son en realidad "sin enchape". **Faltantes: 872 (59,7 %)** | Kaggle – train.csv |
| MasVnrArea | Área del enchape de mampostería. | Numérica continua (decimal) | 0 a 1.600 pies². **Faltantes: 8 (0,5 %)** | Kaggle – train.csv |
| ExterQual | Calidad del material exterior. | Categórica ordinal (texto) | Ex = excelente; Gd = bueno; TA = típico/promedio; Fa = regular; Po = malo | Kaggle – train.csv |
| ExterCond | Estado actual del material exterior. | Categórica ordinal (texto) | Ex = excelente; Gd = bueno; TA = típico/promedio; Fa = regular; Po = malo | Kaggle – train.csv |
| Foundation | Tipo de cimentación. | Categórica nominal (texto) | BrkTil = ladrillo y baldosa; CBlock = bloque de concreto; PConc = concreto vaciado; Slab = losa; Stone = piedra; Wood = madera | Kaggle – train.csv |
| BsmtQual | Altura del sótano. | Categórica ordinal (texto) | Ex = excelente (100+ pulgadas); Gd = bueno (90–99); TA = típico (80–89); Fa = regular (70–79); Po = malo (<70); NA = sin sótano. **Faltantes: 37 (2,5 %)** | Kaggle – train.csv |
| BsmtCond | Estado general del sótano. | Categórica ordinal (texto) | Ex = excelente; Gd = bueno; TA = típico (algo de humedad); Fa = regular (humedad o algunas grietas); Po = malo (grietas graves, hundimiento o humedad); NA = sin sótano. **Faltantes: 37 (2,5 %)** | Kaggle – train.csv |
| BsmtExposure | Exposición del sótano (paredes con salida al exterior o a nivel de jardín). | Categórica ordinal (texto) | Gd = buena; Av = promedio; Mn = mínima; No = sin exposición; NA = sin sótano. **Faltantes: 38 (2,6 %)** | Kaggle – train.csv |
| BsmtFinType1 | Calificación del área terminada del sótano (tipo 1). | Categórica ordinal (texto) | GLQ = área habitable buena; ALQ = área habitable promedio; BLQ = área habitable bajo el promedio; Rec = cuarto de recreación promedio; LwQ = baja calidad; Unf = sin terminar; NA = sin sótano. **Faltantes: 37 (2,5 %)** | Kaggle – train.csv |
| BsmtFinSF1 | Área terminada del sótano de tipo 1. | Numérica continua (entero) | 0 a 5.644 pies² | Kaggle – train.csv |
| BsmtFinType2 | Calificación del área terminada del sótano (tipo 2, si hay más de uno). | Categórica ordinal (texto) | GLQ = área habitable buena; ALQ = área habitable promedio; BLQ = área habitable bajo el promedio; Rec = cuarto de recreación promedio; LwQ = baja calidad; Unf = sin terminar; NA = sin sótano. **Faltantes: 38 (2,6 %)** | Kaggle – train.csv |
| BsmtFinSF2 | Área terminada del sótano de tipo 2. | Numérica continua (entero) | 0 a 1.474 pies² | Kaggle – train.csv |
| BsmtUnfSF | Área sin terminar del sótano. | Numérica continua (entero) | 0 a 2.336 pies² | Kaggle – train.csv |
| TotalBsmtSF | Área total del sótano. | Numérica continua (entero) | 0 a 6.110 pies² | Kaggle – train.csv |
| Heating | Tipo de calefacción. | Categórica nominal (texto) | Floor = calefactor de piso; GasA = aire caliente forzado a gas; GasW = agua caliente o vapor a gas; Grav = calefactor por gravedad; OthW = agua caliente o vapor (no gas); Wall = calefactor de pared | Kaggle – train.csv |
| HeatingQC | Calidad y estado de la calefacción. | Categórica ordinal (texto) | Ex = excelente; Gd = bueno; TA = típico/promedio; Fa = regular; Po = malo | Kaggle – train.csv |
| CentralAir | Tiene aire acondicionado central. | Categórica binaria (texto) | N = no; Y = sí | Kaggle – train.csv |
| Electrical | Sistema eléctrico. | Categórica ordinal (texto) | SBrkr = breakers estándar y cableado Romex; FuseA = caja de fusibles >60 A, todo Romex (promedio); FuseF = caja de fusibles 60 A, mayormente Romex (regular); FuseP = caja de fusibles 60 A, cableado antiguo (malo); Mix = mixto. **Faltantes: 1 (0,1 %)** | Kaggle – train.csv |
| 1stFlrSF | Área del primer piso. | Numérica continua (entero) | 334 a 4.692 pies² | Kaggle – train.csv |
| 2ndFlrSF | Área del segundo piso (0 si no tiene). | Numérica continua (entero) | 0 a 2.065 pies² | Kaggle – train.csv |
| LowQualFinSF | Área terminada de baja calidad (todos los pisos). | Numérica continua (entero) | 0 a 572 pies² | Kaggle – train.csv |
| GrLivArea | Área habitable sobre el nivel del suelo. | Numérica continua (entero) | 334 a 5.642 pies² | Kaggle – train.csv |
| BsmtFullBath | Baños completos en el sótano. | Numérica discreta (conteo) | 0 a 3 | Kaggle – train.csv |
| BsmtHalfBath | Medios baños (sin ducha) en el sótano. | Numérica discreta (conteo) | 0 a 2 | Kaggle – train.csv |
| FullBath | Baños completos sobre el nivel del suelo. | Numérica discreta (conteo) | 0 a 3 | Kaggle – train.csv |
| HalfBath | Medios baños sobre el nivel del suelo. | Numérica discreta (conteo) | 0 a 2 | Kaggle – train.csv |
| BedroomAbvGr | Habitaciones sobre el nivel del suelo (no incluye las del sótano). En data_description.txt aparece como "Bedroom". | Numérica discreta (conteo) | 0 a 8 | Kaggle – train.csv |
| KitchenAbvGr | Cocinas sobre el nivel del suelo. En data_description.txt aparece como "Kitchen". | Numérica discreta (conteo) | 0 a 3 | Kaggle – train.csv |
| KitchenQual | Calidad de la cocina. | Categórica ordinal (texto) | Ex = excelente; Gd = bueno; TA = típico/promedio; Fa = regular; Po = malo | Kaggle – train.csv |
| TotRmsAbvGrd | Total de cuartos sobre el nivel del suelo (sin contar baños). | Numérica discreta (conteo) | 2 a 14 | Kaggle – train.csv |
| Functional | Funcionalidad de la vivienda (se asume típica salvo que haya deducciones). | Categórica ordinal (texto) | Typ = típica; Min1 = deducciones menores 1; Min2 = deducciones menores 2; Mod = deducciones moderadas; Maj1 = deducciones mayores 1; Maj2 = deducciones mayores 2; Sev = muy dañada; Sal = solo para rescate | Kaggle – train.csv |
| Fireplaces | Número de chimeneas. | Numérica discreta (conteo) | 0 a 3 | Kaggle – train.csv |
| FireplaceQu | Calidad de la chimenea. | Categórica ordinal (texto) | Ex = excepcional de mampostería; Gd = de mampostería en el nivel principal; TA = prefabricada en el área principal o de mampostería en el sótano; Fa = prefabricada en el sótano; Po = estufa Ben Franklin; NA = sin chimenea. **Faltantes: 690 (47,3 %)** | Kaggle – train.csv |
| GarageType | Ubicación del garaje. | Categórica nominal (texto) | 2Types = más de un tipo; Attchd = adosado a la casa; Basment = en el sótano; BuiltIn = integrado (con cuarto encima); CarPort = cochera abierta; Detchd = separado de la casa; NA = sin garaje. **Faltantes: 81 (5,5 %)** | Kaggle – train.csv |
| GarageYrBlt | Año de construcción del garaje. | Numérica discreta (año) | 1.900 a 2.010. **Faltantes: 81 (5,5 %)** | Kaggle – train.csv |
| GarageFinish | Acabado interior del garaje. | Categórica ordinal (texto) | Fin = terminado; RFn = terminado en obra gris; Unf = sin terminar; NA = sin garaje. **Faltantes: 81 (5,5 %)** | Kaggle – train.csv |
| GarageCars | Capacidad del garaje en número de carros. | Numérica discreta (conteo) | 0 a 4 | Kaggle – train.csv |
| GarageArea | Área del garaje. | Numérica continua (entero) | 0 a 1.418 pies² | Kaggle – train.csv |
| GarageQual | Calidad del garaje. | Categórica ordinal (texto) | Ex = excelente; Gd = bueno; TA = típico/promedio; Fa = regular; Po = malo; NA = sin garaje. **Faltantes: 81 (5,5 %)** | Kaggle – train.csv |
| GarageCond | Estado del garaje. | Categórica ordinal (texto) | Ex = excelente; Gd = bueno; TA = típico/promedio; Fa = regular; Po = malo; NA = sin garaje. **Faltantes: 81 (5,5 %)** | Kaggle – train.csv |
| PavedDrive | Entrada de vehículos pavimentada. | Categórica ordinal (texto) | Y = pavimentada; P = parcialmente pavimentada; N = tierra o grava | Kaggle – train.csv |
| WoodDeckSF | Área de terraza de madera (deck). | Numérica continua (entero) | 0 a 857 pies² | Kaggle – train.csv |
| OpenPorchSF | Área de porche abierto. | Numérica continua (entero) | 0 a 547 pies² | Kaggle – train.csv |
| EnclosedPorch | Área de porche cerrado. | Numérica continua (entero) | 0 a 552 pies² | Kaggle – train.csv |
| 3SsnPorch | Área de porche de tres estaciones. | Numérica continua (entero) | 0 a 508 pies² | Kaggle – train.csv |
| ScreenPorch | Área de porche con malla. | Numérica continua (entero) | 0 a 480 pies² | Kaggle – train.csv |
| PoolArea | Área de la piscina. | Numérica continua (entero) | 0 a 738 pies² | Kaggle – train.csv |
| PoolQC | Calidad de la piscina. | Categórica ordinal (texto) | Ex = excelente; Gd = bueno; TA = típico/promedio; Fa = regular; NA = sin piscina. **Faltantes: 1453 (99,5 %)** | Kaggle – train.csv |
| Fence | Calidad de la cerca. | Categórica ordinal (texto) | GdPrv = buena privacidad; MnPrv = privacidad mínima; GdWo = madera buena; MnWw = madera o alambre mínimo; NA = sin cerca. **Faltantes: 1179 (80,8 %)** | Kaggle – train.csv |
| MiscFeature | Característica adicional no cubierta en otras variables. | Categórica nominal (texto) | Elev = ascensor; Gar2 = segundo garaje; Othr = otra; Shed = cobertizo (más de 100 pies²); TenC = cancha de tenis; NA = ninguna. **Faltantes: 1406 (96,3 %)** | Kaggle – train.csv |
| MiscVal | Valor de la característica adicional. | Numérica continua (entero) | 0 a 15.500 dólares | Kaggle – train.csv |
| MoSold | Mes de la venta. | Numérica discreta (mes) | 1 a 12 | Kaggle – train.csv |
| YrSold | Año de la venta. | Numérica discreta (año) | 2.006 a 2.010 | Kaggle – train.csv |
| SaleType | Tipo de venta. | Categórica nominal (texto) | WD = escritura con garantía, convencional; CWD = escritura con garantía, de contado; VWD = escritura con garantía, crédito VA; New = vivienda recién construida y vendida; COD = escritura por funcionario judicial o sucesión; Con = contrato con 15 % de cuota inicial; ConLw = contrato con cuota inicial e interés bajos; ConLI = contrato con interés bajo; ConLD = contrato con cuota inicial baja; Oth = otro | Kaggle – train.csv |
| SaleCondition | Condición de la venta. | Categórica nominal (texto) | Normal = venta normal; Abnorml = venta anormal (permuta, remate, venta corta); AdjLand = compra de terreno contiguo; Alloca = asignación (dos propiedades vinculadas con escrituras separadas); Family = venta entre familiares; Partial = vivienda no terminada al momento del avalúo (casas nuevas) | Kaggle – train.csv |
| SalePrice | **Variable objetivo.** Precio de venta de la vivienda. | Numérica continua (entero) | 34.900 a 755.000 dólares | Kaggle – train.csv |

- **Variable**: nombre de la variable.
- **Descripción**: breve descripción de la variable.
- **Tipo de dato**: tipo de dato que contiene la variable.
- **Rango/Valores posibles**: rango o valores que puede tomar la variable.
- **Fuente de datos**: fuente de los datos de la variable.

## Base de datos 2

**test.csv** – Conjunto de prueba de la competencia. Tiene 1.459 viviendas y 80 columnas: `Id` y las mismas 79 variables explicativas de `train.csv`, con igual significado y codificación. No incluye `SalePrice`, porque es el valor que el modelo debe predecir; las predicciones se envían a Kaggle en el formato de `sample_submission.csv` (`Id`, `SalePrice`). Los `Id` van del 1.461 al 2.919 y no se cruzan con los de entrenamiento.

Como las variables son las mismas, abajo se muestran el rango observado y los faltantes en este conjunto. **Ojo:** 15 variables tienen faltantes en test pero no en train (`MSZoning`, `Utilities`, `Exterior1st`, `Exterior2nd`, `BsmtFinSF1`, `BsmtFinSF2`, `BsmtUnfSF`, `TotalBsmtSF`, `BsmtFullBath`, `BsmtHalfBath`, `KitchenQual`, `Functional`, `GarageCars`, `GarageArea`, `SaleType`), así que el preprocesamiento debe poder imputarlas aunque en entrenamiento no se vean vacíos.

| Variable | Descripción | Tipo de dato | Rango/Valores posibles | Fuente de datos |
| --- | --- | --- | --- | --- |
| Id | Identificador único de la vivienda (llave del registro). No se usa como predictor. | Entero (identificador) | 1.461 a 2.919 | Kaggle – test.csv |
| MSSubClass | Tipo de vivienda involucrada en la venta (código que combina número de pisos, antigüedad y tipo). | Categórica nominal (codificada como entero) | Valores observados: 120, 150, 160, 180, 190, 20, 30, 40, 45, 50, 60, 70, 75, 80, 85, 90 (significado igual que en train.csv) | Kaggle – test.csv |
| MSZoning | Clasificación general de zonificación (uso del suelo) del predio. | Categórica nominal (texto) | Valores observados: C (all), FV, RH, RL, RM (significado igual que en train.csv). **Faltantes: 4 (0,3 %)** | Kaggle – test.csv |
| LotFrontage | Longitud del frente del lote que da a la calle. | Numérica continua (decimal) | 21 a 200 pies lineales. **Faltantes: 227 (15,6 %)** | Kaggle – test.csv |
| LotArea | Área del lote. | Numérica continua (entero) | 1.470 a 56.600 pies² | Kaggle – test.csv |
| Street | Tipo de vía de acceso a la propiedad. | Categórica nominal (texto) | Valores observados: Grvl, Pave (significado igual que en train.csv) | Kaggle – test.csv |
| Alley | Tipo de acceso por callejón. | Categórica nominal (texto) | Valores observados: Grvl, Pave (significado igual que en train.csv). **Faltantes: 1352 (92,7 %)** | Kaggle – test.csv |
| LotShape | Forma general del lote. | Categórica ordinal (texto) | Valores observados: IR1, IR2, IR3, Reg (significado igual que en train.csv) | Kaggle – test.csv |
| LandContour | Planitud del terreno. | Categórica nominal (texto) | Valores observados: Bnk, HLS, Low, Lvl (significado igual que en train.csv) | Kaggle – test.csv |
| Utilities | Servicios públicos disponibles. | Categórica ordinal (texto) | Valores observados: AllPub (significado igual que en train.csv). **Faltantes: 2 (0,1 %)** | Kaggle – test.csv |
| LotConfig | Configuración del lote. | Categórica nominal (texto) | Valores observados: Corner, CulDSac, FR2, FR3, Inside (significado igual que en train.csv) | Kaggle – test.csv |
| LandSlope | Pendiente del terreno. | Categórica ordinal (texto) | Valores observados: Gtl, Mod, Sev (significado igual que en train.csv) | Kaggle – test.csv |
| Neighborhood | Barrio de Ames donde está la vivienda. | Categórica nominal (texto) | Valores observados: Blmngtn, Blueste, BrDale, BrkSide, ClearCr, CollgCr, Crawfor, Edwards, Gilbert, IDOTRR, MeadowV, Mitchel, NAmes, NPkVill, NWAmes, NoRidge, NridgHt, OldTown, SWISU, Sawyer, SawyerW, Somerst, StoneBr, Timber, Veenker (significado igual que en train.csv) | Kaggle – test.csv |
| Condition1 | Cercanía a condiciones del entorno (vías, ferrocarril, parques). | Categórica nominal (texto) | Valores observados: Artery, Feedr, Norm, PosA, PosN, RRAe, RRAn, RRNe, RRNn (significado igual que en train.csv) | Kaggle – test.csv |
| Condition2 | Segunda condición del entorno (si hay más de una). | Categórica nominal (texto) | Valores observados: Artery, Feedr, Norm, PosA, PosN (significado igual que en train.csv) | Kaggle – test.csv |
| BldgType | Tipo de edificación. | Categórica nominal (texto) | Valores observados: 1Fam, 2fmCon, Duplex, Twnhs, TwnhsE (significado igual que en train.csv) | Kaggle – test.csv |
| HouseStyle | Estilo de la vivienda (número de pisos y terminación). | Categórica nominal (texto) | Valores observados: 1.5Fin, 1.5Unf, 1Story, 2.5Unf, 2Story, SFoyer, SLvl (significado igual que en train.csv) | Kaggle – test.csv |
| OverallQual | Calificación de la calidad general de materiales y acabados de la vivienda. | Categórica ordinal (entero 1–10) | Valores observados: 1, 10, 2, 3, 4, 5, 6, 7, 8, 9 (significado igual que en train.csv) | Kaggle – test.csv |
| OverallCond | Calificación del estado general de la vivienda. | Categórica ordinal (entero 1–10) | Valores observados: 1, 2, 3, 4, 5, 6, 7, 8, 9 (significado igual que en train.csv) | Kaggle – test.csv |
| YearBuilt | Año de construcción original. | Numérica discreta (año) | 1.879 a 2.010 | Kaggle – test.csv |
| YearRemodAdd | Año de remodelación o ampliación (igual al año de construcción si no hubo). | Numérica discreta (año) | 1.950 a 2.010 | Kaggle – test.csv |
| RoofStyle | Tipo de techo. | Categórica nominal (texto) | Valores observados: Flat, Gable, Gambrel, Hip, Mansard, Shed (significado igual que en train.csv) | Kaggle – test.csv |
| RoofMatl | Material del techo. | Categórica nominal (texto) | Valores observados: CompShg, Tar&Grv, WdShake, WdShngl (significado igual que en train.csv) | Kaggle – test.csv |
| Exterior1st | Material de revestimiento exterior principal. | Categórica nominal (texto) | Valores observados: AsbShng, AsphShn, BrkComm, BrkFace, CBlock, CemntBd, HdBoard, MetalSd, Plywood, Stucco, VinylSd, Wd Sdng, WdShing (significado igual que en train.csv). **Faltantes: 1 (0,1 %)** | Kaggle – test.csv |
| Exterior2nd | Segundo material de revestimiento exterior (si hay más de uno). | Categórica nominal (texto) | Valores observados: AsbShng, AsphShn, Brk Cmn, BrkFace, CBlock, CmentBd, HdBoard, ImStucc, MetalSd, Plywood, Stone, Stucco, VinylSd, Wd Sdng, Wd Shng (significado igual que en train.csv). **Faltantes: 1 (0,1 %)** | Kaggle – test.csv |
| MasVnrType | Tipo de enchape de mampostería (ladrillo o piedra decorativa en la fachada). | Categórica nominal (texto) | Valores observados: BrkCmn, BrkFace, Stone (significado igual que en train.csv). **Faltantes: 894 (61,3 %)** | Kaggle – test.csv |
| MasVnrArea | Área del enchape de mampostería. | Numérica continua (decimal) | 0 a 1.290 pies². **Faltantes: 15 (1,0 %)** | Kaggle – test.csv |
| ExterQual | Calidad del material exterior. | Categórica ordinal (texto) | Valores observados: Ex, Fa, Gd, TA (significado igual que en train.csv) | Kaggle – test.csv |
| ExterCond | Estado actual del material exterior. | Categórica ordinal (texto) | Valores observados: Ex, Fa, Gd, Po, TA (significado igual que en train.csv) | Kaggle – test.csv |
| Foundation | Tipo de cimentación. | Categórica nominal (texto) | Valores observados: BrkTil, CBlock, PConc, Slab, Stone, Wood (significado igual que en train.csv) | Kaggle – test.csv |
| BsmtQual | Altura del sótano. | Categórica ordinal (texto) | Valores observados: Ex, Fa, Gd, TA (significado igual que en train.csv). **Faltantes: 44 (3,0 %)** | Kaggle – test.csv |
| BsmtCond | Estado general del sótano. | Categórica ordinal (texto) | Valores observados: Fa, Gd, Po, TA (significado igual que en train.csv). **Faltantes: 45 (3,1 %)** | Kaggle – test.csv |
| BsmtExposure | Exposición del sótano (paredes con salida al exterior o a nivel de jardín). | Categórica ordinal (texto) | Valores observados: Av, Gd, Mn, No (significado igual que en train.csv). **Faltantes: 44 (3,0 %)** | Kaggle – test.csv |
| BsmtFinType1 | Calificación del área terminada del sótano (tipo 1). | Categórica ordinal (texto) | Valores observados: ALQ, BLQ, GLQ, LwQ, Rec, Unf (significado igual que en train.csv). **Faltantes: 42 (2,9 %)** | Kaggle – test.csv |
| BsmtFinSF1 | Área terminada del sótano de tipo 1. | Numérica continua (entero) | 0 a 4.010 pies². **Faltantes: 1 (0,1 %)** | Kaggle – test.csv |
| BsmtFinType2 | Calificación del área terminada del sótano (tipo 2, si hay más de uno). | Categórica ordinal (texto) | Valores observados: ALQ, BLQ, GLQ, LwQ, Rec, Unf (significado igual que en train.csv). **Faltantes: 42 (2,9 %)** | Kaggle – test.csv |
| BsmtFinSF2 | Área terminada del sótano de tipo 2. | Numérica continua (entero) | 0 a 1.526 pies². **Faltantes: 1 (0,1 %)** | Kaggle – test.csv |
| BsmtUnfSF | Área sin terminar del sótano. | Numérica continua (entero) | 0 a 2.140 pies². **Faltantes: 1 (0,1 %)** | Kaggle – test.csv |
| TotalBsmtSF | Área total del sótano. | Numérica continua (entero) | 0 a 5.095 pies². **Faltantes: 1 (0,1 %)** | Kaggle – test.csv |
| Heating | Tipo de calefacción. | Categórica nominal (texto) | Valores observados: GasA, GasW, Grav, Wall (significado igual que en train.csv) | Kaggle – test.csv |
| HeatingQC | Calidad y estado de la calefacción. | Categórica ordinal (texto) | Valores observados: Ex, Fa, Gd, Po, TA (significado igual que en train.csv) | Kaggle – test.csv |
| CentralAir | Tiene aire acondicionado central. | Categórica binaria (texto) | Valores observados: N, Y (significado igual que en train.csv) | Kaggle – test.csv |
| Electrical | Sistema eléctrico. | Categórica ordinal (texto) | Valores observados: FuseA, FuseF, FuseP, SBrkr (significado igual que en train.csv) | Kaggle – test.csv |
| 1stFlrSF | Área del primer piso. | Numérica continua (entero) | 407 a 5.095 pies² | Kaggle – test.csv |
| 2ndFlrSF | Área del segundo piso (0 si no tiene). | Numérica continua (entero) | 0 a 1.862 pies² | Kaggle – test.csv |
| LowQualFinSF | Área terminada de baja calidad (todos los pisos). | Numérica continua (entero) | 0 a 1.064 pies² | Kaggle – test.csv |
| GrLivArea | Área habitable sobre el nivel del suelo. | Numérica continua (entero) | 407 a 5.095 pies² | Kaggle – test.csv |
| BsmtFullBath | Baños completos en el sótano. | Numérica discreta (conteo) | 0 a 3. **Faltantes: 2 (0,1 %)** | Kaggle – test.csv |
| BsmtHalfBath | Medios baños (sin ducha) en el sótano. | Numérica discreta (conteo) | 0 a 2. **Faltantes: 2 (0,1 %)** | Kaggle – test.csv |
| FullBath | Baños completos sobre el nivel del suelo. | Numérica discreta (conteo) | 0 a 4 | Kaggle – test.csv |
| HalfBath | Medios baños sobre el nivel del suelo. | Numérica discreta (conteo) | 0 a 2 | Kaggle – test.csv |
| BedroomAbvGr | Habitaciones sobre el nivel del suelo (no incluye las del sótano). En data_description.txt aparece como "Bedroom". | Numérica discreta (conteo) | 0 a 6 | Kaggle – test.csv |
| KitchenAbvGr | Cocinas sobre el nivel del suelo. En data_description.txt aparece como "Kitchen". | Numérica discreta (conteo) | 0 a 2 | Kaggle – test.csv |
| KitchenQual | Calidad de la cocina. | Categórica ordinal (texto) | Valores observados: Ex, Fa, Gd, TA (significado igual que en train.csv). **Faltantes: 1 (0,1 %)** | Kaggle – test.csv |
| TotRmsAbvGrd | Total de cuartos sobre el nivel del suelo (sin contar baños). | Numérica discreta (conteo) | 3 a 15 | Kaggle – test.csv |
| Functional | Funcionalidad de la vivienda (se asume típica salvo que haya deducciones). | Categórica ordinal (texto) | Valores observados: Maj1, Maj2, Min1, Min2, Mod, Sev, Typ (significado igual que en train.csv). **Faltantes: 2 (0,1 %)** | Kaggle – test.csv |
| Fireplaces | Número de chimeneas. | Numérica discreta (conteo) | 0 a 4 | Kaggle – test.csv |
| FireplaceQu | Calidad de la chimenea. | Categórica ordinal (texto) | Valores observados: Ex, Fa, Gd, Po, TA (significado igual que en train.csv). **Faltantes: 730 (50,0 %)** | Kaggle – test.csv |
| GarageType | Ubicación del garaje. | Categórica nominal (texto) | Valores observados: 2Types, Attchd, Basment, BuiltIn, CarPort, Detchd (significado igual que en train.csv). **Faltantes: 76 (5,2 %)** | Kaggle – test.csv |
| GarageYrBlt | Año de construcción del garaje. | Numérica discreta (año) | 1.895 a 2.207. **Faltantes: 78 (5,3 %)** | Kaggle – test.csv |
| GarageFinish | Acabado interior del garaje. | Categórica ordinal (texto) | Valores observados: Fin, RFn, Unf (significado igual que en train.csv). **Faltantes: 78 (5,3 %)** | Kaggle – test.csv |
| GarageCars | Capacidad del garaje en número de carros. | Numérica discreta (conteo) | 0 a 5. **Faltantes: 1 (0,1 %)** | Kaggle – test.csv |
| GarageArea | Área del garaje. | Numérica continua (entero) | 0 a 1.488 pies². **Faltantes: 1 (0,1 %)** | Kaggle – test.csv |
| GarageQual | Calidad del garaje. | Categórica ordinal (texto) | Valores observados: Fa, Gd, Po, TA (significado igual que en train.csv). **Faltantes: 78 (5,3 %)** | Kaggle – test.csv |
| GarageCond | Estado del garaje. | Categórica ordinal (texto) | Valores observados: Ex, Fa, Gd, Po, TA (significado igual que en train.csv). **Faltantes: 78 (5,3 %)** | Kaggle – test.csv |
| PavedDrive | Entrada de vehículos pavimentada. | Categórica ordinal (texto) | Valores observados: N, P, Y (significado igual que en train.csv) | Kaggle – test.csv |
| WoodDeckSF | Área de terraza de madera (deck). | Numérica continua (entero) | 0 a 1.424 pies² | Kaggle – test.csv |
| OpenPorchSF | Área de porche abierto. | Numérica continua (entero) | 0 a 742 pies² | Kaggle – test.csv |
| EnclosedPorch | Área de porche cerrado. | Numérica continua (entero) | 0 a 1.012 pies² | Kaggle – test.csv |
| 3SsnPorch | Área de porche de tres estaciones. | Numérica continua (entero) | 0 a 360 pies² | Kaggle – test.csv |
| ScreenPorch | Área de porche con malla. | Numérica continua (entero) | 0 a 576 pies² | Kaggle – test.csv |
| PoolArea | Área de la piscina. | Numérica continua (entero) | 0 a 800 pies² | Kaggle – test.csv |
| PoolQC | Calidad de la piscina. | Categórica ordinal (texto) | Valores observados: Ex, Gd (significado igual que en train.csv). **Faltantes: 1456 (99,8 %)** | Kaggle – test.csv |
| Fence | Calidad de la cerca. | Categórica ordinal (texto) | Valores observados: GdPrv, GdWo, MnPrv, MnWw (significado igual que en train.csv). **Faltantes: 1169 (80,1 %)** | Kaggle – test.csv |
| MiscFeature | Característica adicional no cubierta en otras variables. | Categórica nominal (texto) | Valores observados: Gar2, Othr, Shed (significado igual que en train.csv). **Faltantes: 1408 (96,5 %)** | Kaggle – test.csv |
| MiscVal | Valor de la característica adicional. | Numérica continua (entero) | 0 a 17.000 dólares | Kaggle – test.csv |
| MoSold | Mes de la venta. | Numérica discreta (mes) | 1 a 12 | Kaggle – test.csv |
| YrSold | Año de la venta. | Numérica discreta (año) | 2.006 a 2.010 | Kaggle – test.csv |
| SaleType | Tipo de venta. | Categórica nominal (texto) | Valores observados: COD, CWD, Con, ConLD, ConLI, ConLw, New, Oth, WD (significado igual que en train.csv). **Faltantes: 1 (0,1 %)** | Kaggle – test.csv |
| SaleCondition | Condición de la venta. | Categórica nominal (texto) | Valores observados: Abnorml, AdjLand, Alloca, Family, Normal, Partial (significado igual que en train.csv) | Kaggle – test.csv |

- **Variable**: nombre de la variable.
- **Descripción**: breve descripción de la variable.
- **Tipo de dato**: tipo de dato que contiene la variable.
- **Rango/Valores posibles**: rango o valores que puede tomar la variable.
- **Fuente de datos**: fuente de los datos de la variable.
