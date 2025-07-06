import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import numpy as np
import scipy.stats as ss
import geojson
import pandas as pd

with open("scripts\limits_IT_regions.geojson") as f:
    gj = geojson.load(f)

mashup_1 = pd.read_csv("datasets\mashup_1.csv")
mashup_2 = pd.read_csv("datasets\mashup_2.csv")

filt_mashup_1 = mashup_1[(mashup_1['DS'] == "d1")].reset_index(drop=True)
filt_mashup_2 = mashup_1[(mashup_1['DS'] == "d6")].reset_index(drop=True)
occ_rate_dict = {"Region":[],"Year":[],"Value":[],"DS":[],"institution_count":[]}
for ind, row in filt_mashup_1.iterrows():
  val = row["Value"]
  per = filt_mashup_2["Value"][ind]
  occ_rate = int((per * val)/100)
  occ_rate_dict["Region"].append(row["Region"])
  occ_rate_dict["Year"].append(row["Year"])
  occ_rate_dict["Value"].append(occ_rate)
  occ_rate_dict["DS"].append("occ_rate")
  occ_rate_dict["institution_count"].append(row["institution_count"])


new = pd.DataFrame.from_dict(occ_rate_dict)
filt_mashup_1 = pd.concat([filt_mashup_1, new], ignore_index=True)

g = sns.catplot(filt_mashup_1, kind="bar", x = 'Region',
            y = 'Value',
            hue = 'DS',
            col="Year",
            errorbar = None
            )

g.set_xticklabels(rotation=90)
g.set_titles("Available Accomodations vs Occupancy Rate ({col_var}: {col_name})")

filt = mashup_1[(mashup_1['DS'] == "d4")].reset_index(drop=True)
filt = filt.groupby(["Region","institution_count"])["Value"].mean().astype("float")
filt = filt.to_frame().reset_index()
fig = px.scatter(filt, x="Region", y="institution_count",
                 size='Value', title="Arrivals vs Institution Count")
fig.update_xaxes(tickangle=90)
#fig.show()

filt = mashup_1[(mashup_1['DS'] == "d2") | (mashup_1['DS'] == "d5")]
filt = filt.groupby(["Region","Year","institution_count"])["Value"].sum().astype("float")
filt = filt.to_frame().reset_index()

fig = px.choropleth(filt, geojson=gj, color="Value" ,
                    locations="Region", featureidkey="properties.reg_name",
                    projection="mercator", hover_name='Region', facet_col = "Year", hover_data ="institution_count",
                    title ="Nights Spent (via Collaborative Platforms & Accomodation Establishments)"
                   )
fig.update_geos(fitbounds="locations", visible=False)
#fig.show()

filt = mashup_1[(mashup_1['DS'] == "d3")]

filt2 = filt[["Region","institution_count"]].copy().drop_duplicates().reset_index(drop=True)

fig, ax1 = plt.subplots(figsize=(12,6))
sns.lineplot(data = filt2["institution_count"] , marker='o', sort = False, ax=ax1)
ax2 = ax1.twinx()

sns.barplot(x = 'Region',
            y = 'Value',
            hue = 'Year',
            data = filt,
            ax=ax2,alpha=0.5
            )

ax1.tick_params(labelrotation=90)
plt.title("Total Collective Accommodation Establishments vs Institution Count")


adj = mashup_1.groupby(["Region","institution_count","DS"])["Value"].mean().astype("float")
adj = adj.to_frame().reset_index()
d1 = adj[(adj['DS'] == "d1")]
d1 = d1.rename(columns={"Value":"Available Places (Bedrooms & Bedplaces)"})
d2 = adj[(adj['DS'] == "d2")]
d2 = d2.rename(columns={"Value":"Nightly Stay (Collaborative Platforms)"})
d3 = adj[(adj['DS'] == "d3")]
d3 = d3.rename(columns={"Value":"Total Collective Accommodation Establishments"})
d4 = adj[(adj['DS'] == "d4")]
d4 = d4.rename(columns={"Value":"Arrivals"})
d5 = adj[(adj['DS'] == "d5")]
d5 = d5.rename(columns={"Value":"Nightly Stay (Accomodation Establishments)"})
d6 = adj[(adj['DS'] == "d6")]
d6 = d6.rename(columns={"Value":"Occupancy Rate"})

new = d1.drop(columns="DS").merge(d2.drop(columns="DS"), how = "outer", on=["Region","institution_count"]).reset_index(drop=True)
new = new.merge(d3.drop(columns="DS"), how = "outer", on=["Region","institution_count"]).reset_index(drop=True)
new = new.merge(d4.drop(columns="DS"), how = "outer", on=["Region","institution_count"]).reset_index(drop=True)
new = new.merge(d5.drop(columns="DS"), how = "outer", on=["Region","institution_count"]).reset_index(drop=True)
new = new.merge(d6.drop(columns="DS"), how = "outer", on=["Region","institution_count"]).reset_index(drop=True)
new = new.fillna("")
new = new.drop(columns="Region")
cor = new.corr()

fig, ax = plt.subplots(figsize=(12, 8))
sns.heatmap(cor, ax = ax, annot=True)
#plt.show()

filt = mashup_2.groupby(["Territory","institution_count","DS"])["Observation"].mean().astype("float")
filt = filt.to_frame().reset_index()
fig = px.line(filt, x="Territory", y="Observation", color='DS', title="Economic Data Overview")
fig.update_xaxes(tickangle=90)
#fig.show()

filt = mashup_2.groupby(["Territory","institution_count","DS"])["Observation"].mean().astype("float")
filt = filt.to_frame().reset_index()
fig = px.scatter(filt, x="Observation", y="institution_count", facet_col = "DS",color="Territory", title="GDP & Employment in Persons (hundreds) & Household Net Income vs Institution Count")
#fig.show()

filt = mashup_2.groupby(["Territory","institution_count","DS"])["Observation"].mean().astype("float")
filt = filt.to_frame().reset_index()

filt1 = filt[(filt['DS'] == "d1")]
filt2 = filt[(filt['DS'] == "d2")]
filt3 = filt[(filt['DS'] == "d3")]

fig = px.choropleth(filt1, geojson=gj, color="Observation" ,
                    locations="Territory", featureidkey="properties.reg_name",
                    projection="mercator", hover_name='Territory', hover_data ="institution_count",
                    title="Average GDP between 2021-2023 per Region"
                   )
fig.update_geos(fitbounds="locations", visible=False)
#fig.show()

fig = px.choropleth(filt2, geojson=gj, color="Observation" ,
                    locations="Territory", featureidkey="properties.reg_name",
                    projection="mercator", hover_name='Territory', hover_data ="institution_count",
                    title="Average Employment in Persons (hundreds) between 2021-2023 per Region"
                   )
fig.update_geos(fitbounds="locations", visible=False)
#fig.show()

fig = px.choropleth(filt3, geojson=gj, color="Observation" ,
                    locations="Territory", featureidkey="properties.reg_name",
                    projection="mercator", hover_name='Territory', hover_data ="institution_count",
                    title="Average Household Net Income between 2021-2023 per Region"
                   )
fig.update_geos(fitbounds="locations", visible=False)
#fig.show()

fig = px.choropleth(filt3, geojson=gj, color="institution_count" ,
                    locations="Territory", featureidkey="properties.reg_name",
                    projection="mercator", hover_name='Territory',
                    title="Institution Count per Region"
                   )
fig.update_geos(fitbounds="locations", visible=False)
#fig.show()

adj = mashup_2.groupby(["Territory","institution_count","DS"])["Observation"].mean().astype("float")
adj = adj.to_frame().reset_index()
d1 = adj[(adj['DS'] == "d1")]
d1 = d1.rename(columns={"Observation":"GDP"})
d2 = adj[(adj['DS'] == "d2")]
d2 = d2.rename(columns={"Observation":"Employment in Persons (hundreds)"})
d3 = adj[(adj['DS'] == "d3")]
d3 = d3.rename(columns={"Observation":"Household Net Income"})

new = d1.drop(columns="DS").merge(d2.drop(columns="DS"), how = "outer", on=["Territory","institution_count"]).reset_index(drop=True)
new = new.merge(d3.drop(columns="DS"), how = "outer", on=["Territory","institution_count"]).reset_index(drop=True)
new = new.fillna("")
new = new.drop(columns="Territory")
cor = new.corr()

fig, ax = plt.subplots(figsize=(12, 8))
sns.heatmap(cor, ax = ax, annot=True)
#plt.show()

#fig.write_html("fig.html", full_html=False, include_plotlyjs='cdn')