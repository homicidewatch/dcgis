"""
Configuration describing the shapefiles to be loaded.
"""
import re
from datetime import date

from django.contrib.humanize.templatetags.humanize import ordinal

import utils

def district_normalizer(name):
    """
    Police district names are formatted like as "Third_District",
    so we need to get just the first part of that.
    """
    if "_" in name:
        return name.split('_')[0]
    else:
        return name

# This SHAPEFILES dictionary is a sample. You should delete (or comment out)
# the first entry if you don't care about neighborhoods in Chicago.
SHAPEFILES = {
    # This key should be the plural name of the boundaries in this set
    #'Neighborhoods': {
    #    # Path to a shapefile, relative to /data
    #    'file': 'neighborhoods/Neighboorhoods.shp',
    #    # Generic singular name for an boundary of from this set
    #    'singular': 'Neighborhood',
    #    # Should the singular name come first when creating canonical identifiers for this set?
    #    # (e.g. True in this case would result in "Neighborhood South Austin" rather than "South Austin Neighborhood")
    #    'kind_first': False,
    #    # Function which each feature wall be passed to in order to extract its "external_id" property
    #    # The utils module contains several generic functions for doing this
    #    'ider': utils.simple_namer(['PRI_NEIGH_']),
    #    # Function which each feature will be passed to in order to extract its "name" property
    #    'namer': utils.simple_namer(['PRI_NEIGH']),
    #    # Authority that is responsible for the accuracy of this data
    #    'authority': 'City of Chicago',
    #    # Geographic extents which the boundary set encompasses
    #    'domain': 'Chicago',
    #    # Last time the source was checked for new data
    #    'last_updated': date(2010, 12, 12),
    #    # A url to the source of the data
    #    'href': 'http://www.cityofchicago.org/city/en/depts/doit/supp_info/gis_data.html',
    #    # Notes identifying any pecularities about the data, such as columns that were deleted or files which were merged
    #    'notes': '',
    #    # Encoding of the text fields in the shapefile, i.e. 'utf-8'. If this is left empty 'ascii' is assumed
    #    'encoding': ''
    #    # SRID of the geometry data in the shapefile if it can not be inferred from an accompanying .prj file
    #    # This is normally not necessary and can be left undefined or set to an empty string to maintain the default behavior
    #    #'srid': ''
    #},
    
    'Cities': {
        'file': 'DCBndyPly/DCGIS_DCBndyPly.shp',
        'singular': 'City',
        'kind_first': False,
        'ider': utils.simple_namer(['CITY_NAME']),
        'namer': utils.simple_namer(['CITY_NAME']),
        'authority': 'DC Office of the Chief Technology Officer',
        'domain': 'Washington, DC',
        'last_updated': date(2011, 3, 2),
        'href': 'http://data.dc.gov/Metadata.aspx?id=74',
        'notes': '',
        'encoding': '',
    },
    
    'Wards': {
        'file': 'Ward02Ply/Ward02Ply.shp',
        'singular': 'Ward',
        'kind_first': True,
        'ider': utils.simple_namer(['WARD_ID']),
        'namer': utils.simple_namer(['WARD_ID']),
        'authority': 'DC Office of the Chief Technology Officer',
        'domain': 'Washington, DC',
        'last_updated': date(2011, 2, 26),
        'href': 'http://data.dc.gov/Metadata.aspx?id=126',
        'notes': '',
        'encoding': '',
    },
    
    'Neighborhood Clusters': {
        'file': 'NbhClusPly/NbhClusPly.shp',
        'singular': 'Neighborhood Cluster',
        'kind_first': False,
        'ider': utils.simple_namer(['GIS_ID']),
        'namer': utils.simple_namer(['NBH_NAMES']),
        'authority': 'DC Office of the Chief Technology Officer',
        'domain': 'Washington, DC',
        'last_updated': date(2011, 2, 26),
        'href': 'http://data.dc.gov/Metadata.aspx?id=163',
        'notes': '',
        'encoding': '',
    },
    
    'ANC Districts': {
        'file': 'ANC02Ply/ANC02Ply.shp',
        'singular': 'ANC District',
        'kind_first': True,
        'ider': utils.simple_namer(['GIS_ID']),
        'namer': utils.simple_namer(['ANC_ID']),
        'authority': 'DC Office of the Chief Technology Officer',
        'domain': 'Washington, DC',
        'last_updated': date(2011, 2, 26),
        'href': 'http://data.dc.gov/Metadata.aspx?id=148',
        'notes': '',
        'encoding': '',
    },
    
    'Quadrants': {
        'file': 'DcQuadPly/DcQuadPly.shp',
        'singular': 'Quadrant',
        'kind_first': False,
        'ider': utils.simple_namer(['GIS_ID']),
        'namer': utils.simple_namer(['NAME']),
        'authority': 'DC Office of the Chief Technology Officer',
        'domain': 'Washington, DC',
        'last_updated': date(2011, 2, 26),
        'href': 'http://data.dc.gov/Metadata.aspx?id=83',
        'notes': '',
        'encoding': '',
    },
    
    'Census Block Groups': {
        'file': 'BlockGroupPly/BlockGroupPly.shp',
        'singular': 'Census Block Group',
        'kind_first': True,
        'ider': utils.simple_namer(['BLKGRP']),
        'namer': utils.simple_namer(['BLKGRP']),
        'authority': 'DC Office of the Chief Technology Officer',
        'domain': 'Washington, DC',
        'last_updated': date(2011, 2, 26),
        'href': 'http://data.dc.gov/Metadata.aspx?id=302',
        'notes': '',
        'encoding': '',
    },
    
    'Census Tracts': {
        'file': 'TractPly/TractPly.shp',
        'singular': 'Census Tract',
        'kind_first': True,
        'ider': utils.simple_namer(['TRACT']),
        'namer': utils.simple_namer(['TRACT']),
        'authority': 'DC Office of the Chief Technology Officer',
        'domain': 'Washington, DC',
        'last_updated': date(2011, 2, 26),
        'href': 'http://data.dc.gov/Metadata.aspx?id=119',
        'notes': '',
        'encoding': '',
    },
    
    'No Fly Zones': {
        'file': 'NoFlyZonePly/NoFlyZonePly.shp',
        'singular': 'No Fly Zone',
        'kind_first': False,
        'ider': utils.simple_namer(['NAME']),
        'namer': utils.simple_namer(['NAME']),
        'authority': 'DC Office of the Chief Technology Officer',
        'domain': 'Washington, DC',
        'last_updated': date(2011, 2, 26),
        'href': 'http://data.dc.gov/Metadata.aspx?id=341',
        'notes': '',
        'encoding': '',
    },
    
    'Voting Precincts': {
        'file': 'VotePre08Ply/VotePre08Ply.shp',
        'singular': 'Voting Precinct',
        'kind_first': True,
        'ider': utils.simple_namer(['GIS_ID']),
        'namer': utils.simple_namer(['NAME'], normalizer=lambda n: n.replace('Precinct ', '')),
        'authority': 'DC Office of the Chief Technology Officer',
        'domain': 'Washington, DC',
        'last_updated': date(2011, 2, 27),
        'href': 'http://data.dc.gov/Metadata.aspx?id=508',
        'notes': '',
        'encoding': '',
    },
    
    'Elementary School Attendance Zones': {
        'file': 'ESBndyPly/ESBndyPly.shp',
        'singular': 'Elementary School Attendance Zone',
        'kind_first': False,
        'ider': utils.simple_namer(['SCHOOLNAME']),
        'namer': utils.simple_namer(['SCHOOLNAME']),
        'authority': 'DC Office of the Chief Technology Officer',
        'domain': 'Washington, DC',
        'last_updated': date(2011, 2, 28),
        'href': 'http://data.dc.gov/Metadata.aspx?id=180',
        'notes': '',
        'encoding': '',
    },
    
    'Middle School Attendance Zones': {
        'file': 'MSBndyPly/MSBndyPly.shp',
        'singular': 'Middle School Attendance Zone',
        'kind_first': False,
        'ider': utils.simple_namer(['SCHOOLNAME']),
        'namer': utils.simple_namer(['SCHOOLNAME']),
        'authority': 'DC Office of the Chief Technology Officer',
        'domain': 'Washington, DC',
        'last_updated': date(2011, 2, 28),
        'href': 'http://data.dc.gov/Metadata.aspx?id=181',
        'notes': '',
        'encoding': '',
    },
    
    'Senior High School Attendance Zones': {
        'file': 'SHSBndyPly/SHSBndyPly.shp',
        'singular': 'Senior High School Attendance Zone',
        'kind_first': False,
        'ider': utils.simple_namer(['SCHOOLNAME']),
        'namer': utils.simple_namer(['SCHOOLNAME']),
        'authority': 'DC Office of the Chief Technology Officer',
        'domain': 'Washington, DC',
        'last_updated': date(2011, 2, 28),
        'href': 'http://data.dc.gov/Metadata.aspx?id=63',
        'notes': '',
        'encoding': '',
    },
    
    'School Election Districts': {
        'file': 'SchEDisPly/SchEDisPly.shp',
        'singular': 'School Election District',
        'kind_first': True,
        'ider': utils.simple_namer(['GIS_ID']),
        'namer': utils.simple_namer(['NAME']),
        'authority': 'DC Office of the Chief Technology Officer',
        'domain': 'Washington, DC',
        'last_updated': date(2011, 2, 28),
        'href': 'http://data.dc.gov/Metadata.aspx?id=182',
        'notes': '',
        'encoding': '',
    },
    
    'Police Districts': {
        'file': 'PolDistPly/PolDistPly.shp',
        'singular': 'District',
        'kind_first': False,
        'ider': utils.simple_namer(['GIS_ID']),
        'namer': utils.simple_namer(['NAME'], normalizer=district_normalizer),
        'authority': 'DC Office of the Chief Technology Officer',
        'domain': 'Washington, DC',
        'last_updated': date(2011, 3, 1),
        'href': 'http://data.dc.gov/Metadata.aspx?id=187',
        'notes': '',
        'encoding': '',
    },
    
    'Police Service Areas': {
        'file': 'PolSAPly/PolSAPly.shp',
        'singular': 'Police Service Area',
        'kind_first': True,
        'ider': utils.simple_namer(['GIS_ID']),
        'namer': utils.simple_namer(['NAME']),
        'authority': 'DC Office of the Chief Technology Officer',
        'domain': 'Washington, DC',
        'last_updated': date(2011, 3, 1),
        'href': 'http://data.dc.gov/Metadata.aspx?id=120',
        'notes': '',
        'encoding': '',
    },
    
    'Zip Codes': {
        'file': 'ZipCodePly/ZipCodePly.shp',
        'singular': 'Zip Code',
        'kind_first': True,
        'ider': utils.simple_namer(['GIS_ID']),
        'namer': utils.simple_namer(['ZIPCODE']),
        'authority': 'DC Office of the Chief Technology Officer',
        'domain': 'Washington, DC',
        'last_updated': date(2011, 3, 1),
        'href': 'http://data.dc.gov/Metadata.aspx?id=130',
        'notes': '',
        'encoding': '',
    }
    
}
