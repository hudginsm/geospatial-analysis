import pandas as pd
import geopandas as gpd
from flask import Flask, render_template

app = Flask(__name__)

def strip_smoke_free(text):
    return text.split('Smoke Free')[0]
def clean_df(df: pd.DataFrame) -> pd.DataFrame:
    df.drop(df.iloc[:, 5:11], axis=1, inplace=True)
    df['Name'] = df ['Name'].apply(strip_smoke_free)
    df = df[df['Name'].str.strip().astype(bool)]
    return df
@app.route("/")
def show_map():
    jj_df = pd.read_html('https://www.jcdh.org/SitePages/Programs-Services/Scores-Lists/Food/FoodServScores.aspx?Search=jimmy%20johns',flavor='bs4')[1]
    jm_df = pd.read_html('https://www.jcdh.org/SitePages/Programs-Services/Scores-Lists/Food/FoodServScores.aspx?Search=jersey%20mikes',flavor='bs4')[1]
    sw_df = pd.read_html ('https://www.jcdh.org/SitePages/Programs-Services/Scores-Lists/Food/FoodServScores.aspx?Search=subway',flavor='bs4')[1]
    fh_df = pd.read_html ('https://www.jcdh.org/SitePages/Programs-Services/Scores-Lists/Food/FoodServScores.aspx?Search=firehouse',flavor='bs4')[1]

    jj_df = clean_df(jj_df)
    jm_df = clean_df(jm_df)
    sw_df = clean_df(sw_df)
    fh_df = clean_df(fh_df)

    jj_df['Company'] = 'Jimmy Johns'
    jm_df['Company'] = 'Jersey Mikes'
    sw_df['Company'] = 'Subway'
    fh_df['Company'] = 'Firehouse'

    jj_gdf = gpd.tools.geocode(jj_df['Name'], provider='arcgis')
    jj_gdf.columns = ['geometry','Address']
    jm_gdf = gpd.tools.geocode(jm_df['Name'], provider='arcgis')
    jm_gdf.columns = ['geometry','Address']
    sw_gdf = gpd.tools.geocode(sw_df['Name'], provider='arcgis')
    sw_gdf.columns = ['geometry','Address']
    fh_gdf = gpd.tools.geocode(fh_df['Name'], provider='arcgis')
    fh_gdf.columns = ['geometry','Address']

    jj_gdf = jj_gdf.merge(jj_df, left_index=True, right_index=True, suffixes=('_gdf','_df'))
    jm_gdf = jm_gdf.merge(jm_df, left_index=True, right_index=True, suffixes=('_gdf','_df'))
    sw_gdf = sw_gdf.merge(sw_df, left_index=True, right_index=True, suffixes=('_gdf','_df'))
    fh_gdf = fh_gdf.merge(fh_df, left_index=True, right_index=True, suffixes=('_gdf','_df'))

    gdf = pd.concat([jj_gdf,jm_gdf,sw_gdf,fh_gdf])
    gdf = gdf.to_crs(epsg=4326)
    gdf.head(1)

    m = gdf.explore(
        'Company'
        ,cmap=["firebrick","blue","fuchsia","darkgreen"]
        ,tooltip=['Permit','Score']
        ,popup=True
        ,marker_type='circle_marker'
        ,marker_kwds={'radius':5,'fill':True}
        ,zoom_start=10.5
    )
    return m.get_root().render()

if __name__ == "__main__":
    app.run(debug=True)