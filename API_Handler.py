'''
TODO
* better exception handling
'''



# python standard libraries
import requests

# dependencies
import qasync



class API_Handler:
    URI = 'https://api.tarkov.dev/graphql'
    def __init__(self):
        pass



    def post(self, payload):
        response = requests.post(f'{self.URI}', json={'query': payload})
        if response.status_code != 200:
            raise Exception('Query Failed')
        return response.json()



    @qasync.asyncSlot()
    async def download_image(self, url, filename):
        response = requests.get(url)
        with open(filename, 'wb') as file:
            for chunk in response:
                file.write(chunk)
        return filename



    def get_everything(self):
        query = '''
        {
            traders {
                id
                name
            }

            items {
                id
                name
                normalizedName
                shortName
                iconLink
            }

            tasks {
                id
                name
                trader { id }
                factionName
                objectives {
                    ... on TaskObjectiveItem {
                        id
                        type
                        item {
                            id
                            types
                        }
                        count
                        foundInRaid
                        dogTagLevel
                        maxDurability
                        minDurability
                    }
                }
            }

            hideoutStations {
                name
                levels {
                    id
                    level
                    itemRequirements {
                        id
                        item { id }
                        count
                    }
                }
            }
        }
        '''

        return self.post(query)['data']



    def get_traders(self):
        query = '''
        {
            traders {
                id
                name
            }
        }
        '''
        return self.post(query)['data']['traders']



    def get_items(self):
        query = '''
        {
            items {
                id
                name
                normalizedName
                shortName
                iconLink
            }
        }
        '''
        return self.post(query)['data']['items']



    def get_tasks(self):
        '''
        combines tasks and hideout
        '''

        query = '''
        {
            tasks {
                id
                name
                trader { id }
                factionName
                objectives {
                    ... on TaskObjectiveItem {
                        id
                        type
                        item {
                            id
                            types
                        }
                        count
                        foundInRaid
                        dogTagLevel
                        maxDurability
                        minDurability
                    }
                }
            }

            hideoutStations {
                name
                levels {
                    id
                    level
                    itemRequirements {
                        id
                        item { id }
                        count
                    }
                }
            }
        }
        '''
        response = self.post(query)
        return (response['data']['tasks'], response['data']['hideoutStations'])