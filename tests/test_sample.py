from library.zip_codes import german_city, grand_rapids


class TestZipAPI:

    def test_get_south_jordan_zip(self, api, zipper):
        req = zipper.get(f'{api}.us/us/84095')
        res = req.json()
        assert req.status_code == 200
        assert res.get('post code') == '84095'
        assert res.get('country') == 'United States'
        assert len(res.get('places')) > 0

        places = res.get('places')
        cities_in_zip = [place['place name'] for place in places]
        assert 'South Jordan' in cities_in_zip

    def test_get_canadian_zip(self, api, zipper):
        zip_code = 'T1M'
        req = zipper.get(f'{api}.us/ca/{zip_code}')
        res = req.json()
        assert req.status_code == 200
        assert res.get('post code') == zip_code
        assert res.get('country') == "Canada"

        places = res.get('places')
        cities_in_zip = [place['place name'] for place in places]
        assert 'Coaldale' in cities_in_zip

    def test_get_grand_rapids(self, api, zipper):
        data = grand_rapids()
        req = zipper.get(f'{api}.us/us/{data.get('post_code')}')
        res = req.json()
        assert req.status_code == 200
        assert res.get('post code') == data.get('post_code')
        assert res.get('country') == data.get('country')
        
        places = res.get('places')
        cities_in_zip = [place['place name'] for place in places]
        assert data.get('places')[0].get('place name') in cities_in_zip

    def test_get_german_city(self, api, zipper):
        data = german_city()
        req = zipper.get(f'{api}.us/de/{data.get('post_code')}')
        res = req.json()
        
        assert req.status_code == 200
        assert res.get('post code') == data.get('post_code')
        assert res.get('country') == data.get('country')
        
        places = res.get('places')
        cities_in_zip = [place['place name'] for place in places]
        assert data.get('places')[0].get('place name') in cities_in_zip
        