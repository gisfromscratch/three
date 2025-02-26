"""
A dict of information needed to query city Open311 servers.
"""


class CityNotFound(Exception):
    pass


def find_info(name=None):
    """Find the needed city server information."""
    if not name:
        return list(servers.keys()) 
    name = name.lower()
    if name in servers:
        info = servers[name]
    else:
        raise CityNotFound("Could not find the specified city: %s" % name)
    return info


servers = {
    'bainbridge': {
        'endpoint': 'http://seeclickfix.com/bainbridge-island/open311/'
    },
    'baltimore': {
        'endpoint': 'http://311.baltimorecity.gov/open311/v2/'
    },
    'bloomington': {
        'endpoint': 'https://bloomington.in.gov/crm/open311/v2/'
    },
    'bonn': {
        'endpoint': 'https://anliegen.bonn.de/georeport/v2/'
    },
    'boston': {
        'endpoint': 'https://mayors24.cityofboston.gov/open311/v2/'
    },
    'brookline': {
        'endpoint': 'http://spot.brooklinema.gov/open311/v2/'
    },
    'chicago': {
        'endpoint': 'http://311api.cityofchicago.org/open311/v2/',
        'discovery': 'http://311api.cityofchicago.org/open311/discovery.json'
    },
    'corona': {
        'endpoint': 'http://seeclickfix.com/corona/open311/'
    },
    'darwin': {
        'endpoint': 'http://seeclickfix.com/aus_darwin/open311/'
    },
    'dc': {
        'endpoint': 'http://app.311.dc.gov/CWI/Open311/v2/',
        'format': 'xml',
        'jurisdiction': 'dc.gov'
    },
    'district of columbia': {
        'endpoint': 'http://app.311.dc.gov/CWI/Open311/v2/',
        'format': 'xml',
        'jurisdiction': 'dc.gov'
    },
    'deleon': {
        'endpoint': 'http://seeclickfix.com/de-leon/open311/'
    },
    'dunwoody': {
        'endpoint': 'http://seeclickfix.com/dunwoody_ga/open311/'
    },
    'fontana': {
        'endpoint': 'http://seeclickfix.com/fontana/open311/'
    },
    'grand rapids': {
        'endpoint': 'http://grcity.spotreporters.com/open311/v2/'
    },
    'hillsborough': {
        'endpoint': 'http://seeclickfix.com/hillsborough/open311/'
    },
    'howard county': {
        'endpoint': 'http://seeclickfix.com/md_howard-county/open311/'
    },
    'huntsville': {
        'endpoint': 'http://seeclickfix.com/huntsville/open311/'
    },
    'macon': {
        'endpoint': 'http://seeclickfix.com/macon/open311/'
    },
    'manor': {
        'endpoint': 'http://seeclickfix.com/manor/open311/'
    },
    'new haven': {
        'endpoint': 'http://seeclickfix.com/new-haven/open311/'
    },
    'newark': {
        'endpoint': 'http://seeclickfix.com/newark_2/open311/'
    },
    'newberg': {
        'endpoint': 'http://seeclickfix.com/newberg/open311/'
    },
    'newnan': {
        'endpoint': 'http://seeclickfix.com/newnan/open311/'
    },
    'olathe': {
        'endpoint': 'http://seeclickfix.com/olathe/open311/'
    },
    'raleigh': {
        'endpoint': 'http://seeclickfix.com/raleigh/open311/'
    },
    'richmond': {
        'endpoint': 'http://seeclickfix.com/richmond/open311/'
    },
    'roosevelt island': {
        'endpoint': 'http://seeclickfix.com/roosevelt-island/open311/'
    },
    'russell springs': {
        'endpoint': 'http://seeclickfix.com/russell-springs/open311/'
    },
    'san francisco': {
        'endpoint': 'https://open311.sfgov.org/V2/',
        'format': 'xml',
        'jurisdiction': 'sfgov.org'
    },
    'sf': {
        'endpoint': 'https://open311.sfgov.org/V2/',
        'format': 'xml',
        'jurisdiction': 'sfgov.org'
    },
    'toronto': {
        'endpoint': 'https://secure.toronto.ca/webwizard/ws/',
        'jurisdiction': 'toronto.ca'
    },
    'tucson': {
        'endpoint': 'http://seeclickfix.com/tucson/open311/'
    },
}
