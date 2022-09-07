import requests
import time
import os

from config import CSV_DIRNAME, NIH_USERNAME, NIH_PASSWORD, NIH_DOWNLOAD_WAIT_TIME, NIH_DOWNLOAD_NUM_RETRIES, PUBDATE_RANGES

if __name__ == '__main__':
    
    # login
    url = 'https://icite.od.nih.gov/covid19/auth/login'
    print(url)
    json = {
        'username': NIH_USERNAME,
        'password': NIH_PASSWORD
    }
    response = requests.post(url, json=json)
    print(response.status_code)
    results = response.json()
    access_token = results['accessToken']
    print('access_token = {}'.format(access_token))

    # try searching for all pub dates
    for start_date, end_date in PUBDATE_RANGES:
        
        print()
        print('searching for articles from {} to {}'.format(start_date, end_date))

        # save search
        url = 'https://icite.od.nih.gov/covid19/searchwebapp/covid19/secure/saveSearch'
        print()
        print(url)
        cookies = {
            'user': NIH_USERNAME,
            'session': access_token
        }
        json = {
            'selectedFacets': {},
            'excludedFacets': {},
            'selectedAndOr': {},
            'excludedAndOr': {},
            'visibleFacetsList': [],
            'query': '',
            'searchFields': [
                'abstract',
                'authors.affiliationNormalized',
                'authors.fullName',
                'condition',
                'doi',
                'firstAuthor.fullName',
                'fulltext',
                'lastAuthor.fullName',
                'pmid',
                'supplementalText',
                'id',
                'title'
            ],
            'orOperator': False,
            'selectedFilters': {
                'pubDate': [
                    start_date,
                    end_date
                ]
            }
        }
        response = requests.post(url, cookies=cookies, json=json)
        print(response.status_code)
        results = response.json()
        search_id = results['searchId']
        print('search_id = {}'.format(search_id))

        # search
        url = 'https://icite.od.nih.gov/covid19/searchwebapp/covid19/secure/search?searchId={}'.format(search_id)
        print()
        print(url)
        cookies = {
            'user': NIH_USERNAME,
            'session': access_token
        }
        response = requests.post(url, cookies=cookies)
        print(response.status_code)
        results = response.json()
        total_count = results['totalCount']
        print('total_count = {}'.format(total_count))

        # export
        url = 'https://icite.od.nih.gov/covid19/searchwebapp/covid19/secure/exportForAnonymous'
        print()
        print(url)
        cookies = {
            'user': NIH_USERNAME,
            'session': access_token
        }
        json = {
            'searchId': search_id,
            'portfolioId': None,
            'exportFields': [
                'doi',
                'latestVersion',
                'pmcId',
                'pmid',
                'pubDate',
                'pubTypes',
                'publishedAs',
                'recordSource',
                'title',
                'abstract',
                'condition',
                'chemicalsDrugs',
                'target',
                'devices',
                'authors.fullName',
                'authorCount',
                'citedByPmidCount',
                'issn',
                'journalName',
                'zuliaScore',
                'id'
            ],
            'exportTitle': '',
            'exportFormat': 'csv',
            'shouldHyperlinkIds': True,
            'includeVisCategories': False,
            'includeLinkToSource': False,
            'idsToExportFromVis': None,
            'baseUrl': 'https://icite.od.nih.gov/covid19/search/'
        }
        response = requests.post(url, cookies=cookies, json=json)
        print(response.status_code)
        export_id = response.text
        print('export_id = {}'.format(export_id))

        # download exported file
        for retry in range(NIH_DOWNLOAD_NUM_RETRIES):
            url = 'https://icite.od.nih.gov/covid19/file/secure/download/{}'.format(export_id)
            print()
            print(url)
            cookies = {
                'user': NIH_USERNAME,
                'session': access_token
            }
            response = requests.get(url, cookies=cookies)
            print(response.status_code)
            if response.status_code == 200:
                csv_filename = '{}_{}.csv'.format(start_date, end_date)
                print('saving into {} ...'.format(csv_filename))
                with open(os.path.join(CSV_DIRNAME, csv_filename), 'wb') as csv_file:
                    csv_file.write(response.content)
                break
            else:
                time.sleep(NIH_DOWNLOAD_WAIT_TIME)
