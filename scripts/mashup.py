import pandas as pd

cult_inst = pd.read_csv("datasets\cultural_inst.csv")

df_cult = cult_inst["Region"].value_counts().astype("int64")
df_cult = df_cult.to_frame().reset_index()
df_cult = df_cult.rename(columns={"count":"institution_count"})
df_cult.loc[15, "Region"] = "Friuli Venezia Giulia"
df_cult.loc[18, "Region"] = "Valle d'Aosta"

mashup_1 = pd.DataFrame()
df1 = pd.read_csv("datasets\df_1.csv").drop_duplicates()
df2 = pd.read_csv("datasets\df_2.csv").drop_duplicates()
df3 = pd.read_csv("datasets\df_3.csv").drop_duplicates()
df4 = pd.read_csv("datasets\df_4.csv").drop_duplicates()
df5 = pd.read_csv("datasets\df_5.csv").drop_duplicates()
df6 = pd.read_csv("datasets\df_6.csv").drop_duplicates()

df1 = df1.drop(df1.columns[0], axis=1)
df2 = df2.drop(df2.columns[0], axis=1)
df3 = df3.drop(df3.columns[0], axis=1)
df4 = df4.drop(df4.columns[0], axis=1)
df5 = df5.drop(df5.columns[0], axis=1)
df6 = df6.drop(df6.columns[0], axis=1)

df1_mod = df1[df1["Unit of measurement"]=="Number"]
df1_mod = df1_mod[df1_mod["Accommodation_Capacity"]!="Establishments"]
df1_mod = df1_mod[df1_mod["Economic activity"]=="Hotels; holiday and other short-stay accommodation; camping grounds, recreational vehicle parks and trailer parks"]
df1_mod = df1.groupby(["Region","Year"])["Value"].mean().astype("int64")
df1_mod = df1_mod.to_frame().reset_index()
df1_mod["DS"] = "d1"

df2_mod = df2[df2["Residence_Type"]=="Total"]
df2_mod = df2_mod.groupby(["Region","Year"])["Value"].sum().astype("int64")
df2_mod = df2_mod.to_frame().reset_index()
df2_mod["DS"] = "d2"

df3_mod = df3[df3["Indicator"]=="nights spent"]
df3_mod = df3_mod[df3_mod["Accommodation_Type"]=="total collective accommodation establishments"]
df3_mod = df3.groupby(["Region","Year"])["Value"].sum().astype("int64")
df3_mod = df3_mod.to_frame().reset_index()
df3_mod["DS"] = "d3"

df4_mod = df4.groupby(["Region","Year"])["Value"].sum().astype("int64")
df4_mod = df4_mod.to_frame().reset_index()
df4_mod["DS"] = "d4"

df5_mod = df5.groupby(["Region","Year"])["Value"].sum().astype("int64")
df5_mod = df5_mod.to_frame().reset_index()
df5_mod["DS"] = "d5"

df6_mod = df6.groupby(["Region","Year"])["Value"].mean().astype("float")
df6_mod = df6_mod.to_frame().reset_index()
df6_mod["DS"] = "d6"

mashup_1 = df1_mod.merge(df2_mod, how = "outer", on=["Region","Year","Value","DS"]).reset_index(drop=True)
mashup_1 = mashup_1.merge(df3_mod, how = "outer", on=["Region","Year","Value","DS"]).reset_index(drop=True)
mashup_1 = mashup_1.merge(df4_mod, how = "outer", on=["Region","Year","Value","DS"]).reset_index(drop=True)
mashup_1 = mashup_1.merge(df5_mod, how = "outer", on=["Region","Year","Value","DS"]).reset_index(drop=True)
mashup_1 = mashup_1.merge(df6_mod, how = "outer", on=["Region","Year","Value","DS"]).reset_index(drop=True)
mashup_1 = mashup_1.merge(df_cult, how = "outer", on = "Region").reset_index(drop=True)
mashup_1 = mashup_1.fillna("")

df_1 = pd.read_csv("datasets\gdp.csv")
df_2 = pd.read_csv("datasets\Employment.csv")
df_3 = pd.read_csv("datasets\income.csv")

df_1_mod = df_1.groupby(["Territory","TIME_PERIOD"])["Observation"].sum()
df_1_mod = df_1_mod.to_frame().reset_index()
new_rows_df1 = pd.DataFrame({"Territory":["Marche","Marche","Marche"],"TIME_PERIOD":[2021,2022,2023],"Observation":[0.0,0.0,0.0]})
df_1_mod = pd.concat([df_1_mod, new_rows_df1], ignore_index=True)
df_1_mod["DS"] = "d1"

df_2_mod = df_2.groupby(["Territory","TIME_PERIOD"])["Observation"].sum()
df_2_mod = df_2_mod.to_frame().reset_index()
new_rows_df2 = pd.DataFrame({"Territory":["Isole","Isole","Isole"],"TIME_PERIOD":[2021,2022,2023],"Observation":[0.0,0.0,0.0]})
df_2_mod = pd.concat([df_2_mod, new_rows_df2], ignore_index=True)
df_2_mod["DS"] = "d2"
df_2_mod["Observation"] = df_2_mod["Observation"]*10

df_3_mod = df_3[["Territory","TIME_PERIOD","Obs_d2"]]
df_3_mod = df_3_mod.rename(columns={"Obs_d2":"Observation"})
df_3_mod["DS"] = "d3"

df_cult_mod = df_cult.copy()
df_cult_mod = df_cult_mod.drop(16)
df_cult_mod.loc[15, "Region"] = df_1_mod["Territory"][15]
df_cult_mod.loc[18, "Region"] = df_1_mod["Territory"][58]

bolzano = cult_inst.query('Provincia == "Bolzano/Bozen" ')["Provincia"].count()
trento = cult_inst.query('Provincia == "Trento" ')["Provincia"].count()
new_rows = pd.DataFrame({"Region":[df_1_mod["Territory"][36],df_1_mod["Territory"][39],df_3_mod["Territory"][63]],"institution_count":[bolzano,trento,0.0]})
df_cult_mod = pd.concat([df_cult_mod, new_rows], ignore_index=True)

mashup_2 = pd.DataFrame()
mashup_2 = df_1_mod.merge(df_2_mod, how = "outer", on=["Territory","TIME_PERIOD","Observation","DS"]).reset_index(drop=True)
mashup_2 = mashup_2.merge(df_3_mod, how = "outer", on=["Territory","TIME_PERIOD", "Observation","DS"]).reset_index(drop=True)
df_cult_mod = df_cult_mod.rename(columns={"Region":"Territory"})
mashup_2 = mashup_2.merge(df_cult_mod, how = "outer", on="Territory").reset_index(drop=True)
mashup_2 = mashup_2.fillna("")

mashup_1.to_csv("mashup_1.csv")
mashup_2.to_csv("mashup_2.csv")