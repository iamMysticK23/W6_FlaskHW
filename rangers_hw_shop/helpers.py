import requests
import requests_cache



requests_cache.install_cache(cache_name = 'image_cache', backend='sqlite', expire_after=900)



def get_image(search):
   

    url = "https://google-search72.p.rapidapi.com/imagesearch"

    querystring = {"q": search,"gl":"us","lr":"lang_en","num":"1","start":"0"}

    headers = {
        "X-RapidAPI-Key": "9355ca4dffmshc8cdab31b941a31p14159djsna664b84460b4",
        "X-RapidAPI-Host": "google-search72.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    # getting image from API
    data = response.json()
    img_url = data['items'][0]['originalImageUrl'] # getting img url we want
    return img_url

