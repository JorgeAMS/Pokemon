from django.shortcuts import render
from django.views.generic.base import TemplateView
import requests     

# Create your views here.

class GEtPokeInfo():
    pass



class MainView(TemplateView):
    template_name = "pokeinfo/index.html"

    def get(self, request):
        return render (request, self.template_name)

    def post(self, request):
        id = str(request.POST.get('pokeid'))
        name_url = "https://pokeapi.co/api/v2/evolution-chain/"+id+"/"
        wh_url = "https://pokeapi.co/api/v2/pokemon/"+id+"/"
        evo_url = "https://pokeapi.co/api/v2/evolution-chain/"+id+"/"

        try:
            name_response = requests.request("GET", name_url)
            if name_response.status_code == 200:
                name = name_response.json().get('chain')['species']['name']
            else:
                print("Id not found at {}, please check.".format(name_url))

            wh_response = requests.request("GET", wh_url)
            if wh_response.status_code == 200:
                height = wh_response.json().get('height')
                weight = wh_response.json().get('weight')
                stats = wh_response.json().get('stats')
                stats_name = ""
                for stat in stats:
                    stats_name = stats_name + stat.get('stat')['name'] + ", "
            else:
                print("Id not found at {}, please check.".format(wh_url))   

            # chain -> species -> name
            # chain -> envolves_to -> species -> name
            # chain -> envolves_to -> envolves_to -> species -> name

            evo_response = requests.request("GET", evo_url)
            if evo_response.status_code == 200:
                #evolution_chain = evo_response.json().get('chain')['species'] + " -> " +  evo_response.json().get('chain')['envolves_to']['species']['name'] + " -> " + evo_response.json().get('chain')['envolves_to']['envolves_to']['species']['name'] 
                evo1 = ""
                evo2 = ""
                evo3 = ""
                try:
                    evo1 = evo_response.json().get('chain')['species']['name'] + " -> "
                except:
                    pass
                try:
                    evo2 = evo_response.json().get('chain')['evolves_to'][0]['species']['name'] + " -> "
                except:
                    pass
                try:
                    evo3 = evo_response.json().get('chain')['evolves_to'][0]['evolves_to'][0]['species']['name']
                except:
                    pass
                
                evo_chain = evo1 + evo2 + evo3
            else:
                print("Id not found at {}, please check.".format(evo_url)) 

        except Exception as e:
            print("It has been an error: {}".format(e))
            
        return render (request, self.template_name, {
            'name':name,
            'base_stats':stats_name,
            'height':height,
            'weight':weight,
            'id':id,
            'evolutions': evo_chain,
        })