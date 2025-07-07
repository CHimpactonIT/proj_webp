from rdflib import Graph, Namespace, Literal, URIRef
from rdflib.namespace import DCTERMS, PROV, XSD, RDF, RDFS
import os

DCAT = Namespace("https://www.w3.org/ns/dcat#")
ADMS = Namespace("http://www.w3.org/ns/adms#")
CHimpactonIT = Namespace("http://chimpactonit.github.io/proj_webp//")
CC = Namespace("http://creativecommons.org/ns#")

g = Graph()
catalog_g = Graph()
g.bind("dcat3", DCAT)
g.bind("dct", DCTERMS)
g.bind("prov", PROV)
g.bind("adms", ADMS)
g.bind("xsd", XSD)
g.bind("CHimpactonIT", CHimpactonIT)
g.bind("cc", CC)

catalog_g.bind("dcat", DCAT)
catalog_g.bind("dct", DCTERMS)
catalog_g.bind("prov", PROV)
catalog_g.bind("adms", ADMS)
catalog_g.bind("xsd", XSD)
catalog_g.bind("cc", CC)
catalog_g.bind("CHimpactonIT", CHimpactonIT)


datasets = [
    {
        "id": "D1",
        "title": "Establishments, bedrooms, and bed-places in tourist accommodation (NUTS 2 region)",
        "description": "This dataset provides information on the number of tourist accommodation establishments, bedrooms, and bed places across different NUTS 2 regions in Italy.",
        "modified": "2025-06-27",
        "publisher": "Eurostat",
        "creator": "Eurostat",
        "rights_holder": "Eurostat",
        "format": ".csv, .tsv, .xlsx, SDMX (.xml, .json)",
        "license": "https://creativecommons.org/licenses/by/4.0/"
    },
    {
        "id": "D2",
        "title": "Guest nights spent at short-stay accommodations via collaborative economy platforms (NUTS 3 region)",
        "description": "This dataset presents the number of guest nights booked through short-term rental platforms (e.g., Airbnb, Booking.com).",
        "modified": "2025-07-02",
        "publisher": "Eurostat",
        "creator": "Eurostat",
        "rights_holder": "Eurostat",
        "format": ".csv, .tsv, .xlsx, SDMX (.xml, .json)",
        "license": "https://creativecommons.org/licenses/by/4.0/"
    },
    {
        "id": "D3",
        "title": "Occupancy in collective tourist accomodation by type of accomodation",
        "description": "This dataset provides detailed monthly occupancy statistics for different types of tourist accommodations across Italy, categorized by NACE rev. 2 industry codes.",
        "modified": "",
        "publisher": "ISTAT",
        "creator": "ISTAT",
        "rights_holder": "ISTAT",
        "format": ".csv, .tsv, .xlsx, SDMX (.xml, .json)",
        "license": "https://creativecommons.org/licenses/by/4.0/"
    },
    {
        "id": "D4",
        "title": "Arrivals at tourist accommodation establishments by NUTS 2 region",
        "description": "This dataset tracks the number of tourist arrivals at accommodation establishments across NUTS 2 regions in Italy.",
        "modified": "2025-06-27",
        "publisher": "Eurostat",
        "creator": "Eurostat",
        "rights_holder": "Eurostat",
        "format": ".csv, .tsv, .xlsx, SDMX (.xml, .json)",
        "license": "https://creativecommons.org/licenses/by/4.0/"
    },
    {
        "id": "D5",
        "title": "Nights spent at tourist accommodation establishments by NUTS 2 region",
        "description": "This dataset reports the total number of nights spent by tourists in accommodations across NUTS 2 regions.",
        "modified": "2025-06-27",
        "publisher": "Eurostat",
        "creator": "Eurostat",
        "rights_holder": "Eurostat",
        "format": ".csv, .tsv, .xlsx, SDMX (.xml, .json)",
        "license": "https://creativecommons.org/licenses/by/4.0/"
    },
    {
        "id": "D6",
        "title": "Occupancy in tourist accommodation, by NUTS 2 region",
        "description": "This dataset provides net occupancy rates of bed places and bedrooms in hotels and similar accommodations (NACE Rev. 2 activity I55.1) at the NUTS 2 regional level.",
        "modified": "2025-06-27",
        "publisher": "Eurostat",
        "creator": "Eurostat",
        "rights_holder": "Eurostat",
        "format": ".csv, .tsv, .xlsx, SDMX (.xml, .json)",
        "license": "https://creativecommons.org/licenses/by/4.0/"
    },
    {
        "id": "D7",
        "title": "Luoghi della cultura",
        "description": "Data from DBUnico 2.0 describing state and non-state cultural sites, managed and updated by the General Directorate for Organization.",
        "modified": "2025-06-27",
        "publisher": "MiC – Direzione generale Organizzazione",
        "creator": "MiC – Direzione generale Organizzazione",
        "rights_holder": "MiC – Direzione generale Organizzazione",
        "format": ".csv, .tsv, .xlsx, SDMX (.xml, .json)",
        "license": "https://creativecommons.org/licenses/by/4.0/"
    },
    {
        "id": "D8",
        "title": "Gross domestic product supply side",
        "description": "This dataset provides a breakdown of Italy's GDP by analyzing the value added by different economic sectors, such as agriculture, industry, and services.",
        "modified": "",
        "publisher": "ISTAT",
        "creator": "ISTAT",
        "rights_holder": "ISTAT",
        "format": ".csv, .tsv, .xlsx, SDMX (.xml, .json)",
        "license": "https://creativecommons.org/licenses/by/4.0/"
    },
    {
        "id": "D9",
        "title": "Employment by Economic Sector (2010 Classification)",
        "description": "This dataset provides employment data categorized by economic sector based on the 2010 classification.",
        "modified": "",
        "publisher": "ISTAT",
        "creator": "ISTAT",
        "rights_holder": "ISTAT",
        "format": ".csv, .tsv, .xlsx, SDMX (.xml, .json)",
        "license": "https://creativecommons.org/licenses/by/4.0/"
    },
    {
        "id": "D10",
        "title": "Household Net Income by Source of Income",
        "description": "This dataset provides information on household net income, broken down by different sources of income (e.g., wages, pensions, business income) at various territorial levels.",
        "modified": "",
        "publisher": "ISTAT",
        "creator": "ISTAT",
        "rights_holder": "ISTAT",
        "format": ".csv, .tsv, .xlsx, SDMX (.xml, .json)",
        "license": "https://creativecommons.org/licenses/by/4.0/"
    },
]


for ds in datasets:
    ds_uri = URIRef(CHimpactonIT[ds["id"]])
    catalog_g.add((URIRef("chimpactonit.github.io/proj_webp/"), DCAT.Dataset, Literal(ds["id"])))
    g.add((ds_uri, RDF.type, DCAT.Dataset))
    g.add((ds_uri, DCAT.title, Literal(ds["title"], lang="en")))
    g.add((ds_uri, DCTERMS.identifier, Literal(ds["id"])))
    g.add((ds_uri, DCTERMS.title, Literal(ds["title"], lang="en")))
    g.add((ds_uri, DCTERMS.description, Literal(ds["description"], lang="en")))
    g.add((ds_uri, DCTERMS.publisher, Literal(ds["publisher"])))
    g.add((ds_uri, DCTERMS.creator, Literal(ds["creator"])))
    g.add((ds_uri, DCTERMS.rightsHolder, Literal(ds["rights_holder"])))
    g.add((ds_uri, DCAT.distribution, Literal(ds["format"])))
    g.add((ds_uri, DCTERMS.language, Literal("en")))
    g.add((ds_uri, DCTERMS.license, URIRef(ds["license"])))



catalog_uri = URIRef(CHimpactonIT["catalog"])
catalog_g.add((catalog_uri, RDF.type, DCAT.Catalog))
catalog_g.add((catalog_uri, DCTERMS.title, Literal("CH Impact on IT - Datasets Catalogue", lang="en")))
catalog_g.add((catalog_uri, DCTERMS.identifier, Literal("CHImpactonITCatalogue")))
catalog_g.add((catalog_uri, DCTERMS.description, Literal("This catalog contains datasets about cultural heritage institutions, tourism activities and economic data in Italy, based on regions.", lang="en")))
catalog_g.add((catalog_uri, DCTERMS.publisher, Literal("CHimpactonIT")))
catalog_g.add((catalog_uri, DCTERMS.issued, Literal("2025-06-15", datatype=XSD.date)))
catalog_g.add((catalog_uri, DCTERMS.modified, Literal("2025-07-06", datatype=XSD.date)))
catalog_g.add((catalog_uri, DCTERMS.language, Literal("en")))
catalog_g.add((catalog_uri, DCTERMS.license, URIRef("https://creativecommons.org/licenses/by/4.0/")))
catalog_g.add((catalog_uri, DCTERMS.identifier,  Literal("CHImpactonITCatalogue", datatype=XSD.string)))

license_uri = URIRef("https://creativecommons.org/licenses/by/4.0/")
catalog_g.add((catalog_uri, DCTERMS.license, license_uri))

catalog_g.add((license_uri, RDF.type, CC.License))
catalog_g.add((license_uri, CC.legalcode, URIRef("http://creativecommons.org/licenses/by/4.0/")))
catalog_g.add((license_uri, CC.permits, CC.Reproduction))
catalog_g.add((license_uri, CC.permits, CC.Distribution))
catalog_g.add((license_uri, CC.permits, CC.DerivativeWorks))
catalog_g.add((license_uri, CC.requires, CC.Notice))
catalog_g.add((license_uri, CC.requires, CC.Attribution))
catalog_g.add((license_uri, RDFS.label, Literal("Creative Commons CC-BY 4.0", lang="en")))


output_dir = "serialization"
os.makedirs(output_dir, exist_ok=True)



datasets_file = os.path.join(output_dir, "serial_datasets.ttl")
catalog_file = os.path.join(output_dir, "serial_catalog.ttl")

with open(datasets_file, "w", encoding="utf-8") as f:
    f.write(g.serialize(format="turtle"))

with open(catalog_file, "w", encoding="utf-8") as f:
    f.write(catalog_g.serialize(format="turtle"))