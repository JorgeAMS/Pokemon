from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import JsonResponse

import requests     
from .models import pokemon, basestats, evolutions

# Create your views here.

class MainView(TemplateView):
    template_name = "pokeinfo/index.html"

    def get(self, request):
        print("######################")
        print(basestats.objects.all())
        print("######################")
        return render (request, self.template_name)

    def post(self, request):

        exists = True
        name = ""
        evo1 = ""
        evo2 = ""
        evo3 = ""
        height = 0
        weight = 0
        stats = ""
        stats_name = ""
        evo_chain = ""

        id = str(request.POST.get('pokeid'))
        name_url = "https://pokeapi.co/api/v2/evolution-chain/"+id+"/"
        wh_url = "https://pokeapi.co/api/v2/pokemon/"+id+"/"
        evo_url = "https://pokeapi.co/api/v2/evolution-chain/"+id+"/"

        try:
            name_response = requests.request("GET", name_url)
            if name_response.status_code == 200:
                name = name_response.json().get('chain')['species']['name']
            else:
                exists = False
                print("Id not found at {}, please check.".format(name_url))

            wh_response = requests.request("GET", wh_url)
            if wh_response.status_code == 200:
                height = wh_response.json().get('height')
                weight = wh_response.json().get('weight')
                stats = wh_response.json().get('stats')
            else:
                exists = False
                print("Id not found at {}, please check.".format(wh_url))   

            if exists:
                try:
                    pokemon.objects.get_or_create(id=id, name=name, height=height, weight=weight)
                    for stat in stats:
                        try:
                            print("Created stat: {}".format(stat.get('stat')['name']))
                            basestats.objects.get_or_create(poke_id=pokemon(id=id), stat=stat.get('stat')['name'])
                        except Exception as e:
                            print("Couldn't create object due to: {}".format(e))
                except Exception as e:
                    print("Couldn't create object due to: {}".format(e))

                for stat in stats:
                    stats_name = stats_name + stat.get('stat')['name'] + ", "

            evo_response = requests.request("GET", evo_url)
            if evo_response.status_code == 200:
                try:
                    evolution1 = evo_response.json().get('chain')['species']['name']
                    evo1 = evolution1 + " -> "
                    evolutions.objects.get_or_create(poke_id=pokemon(id=id), evolution_secuence=1, evolution=evolution1)

                except:
                    pass
                try:
                    evolution2 = evo_response.json().get('chain')['evolves_to'][0]['species']['name']
                    evo2 = evolution2 + " -> "
                    evolutions.objects.get_or_create(poke_id=pokemon(id=id), evolution_secuence=2, evolution=evolution2)
                except:
                    pass
                try:
                    evo3 = evo_response.json().get('chain')['evolves_to'][0]['evolves_to'][0]['species']['name']
                    evolutions.objects.get_or_create(poke_id=pokemon(id=id), evolution_secuence=3, evolution=evo3)
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

class ServiceView(TemplateView):
    def get(self, request):
        pokemon_name = str(request.GET.get('name'))
        try:
            data = pokemon.objects.get(name=pokemon_name)
            stats_data = basestats.objects.filter(poke_id=data.id)
            evolutions_data = evolutions.objects.filter(poke_id=data.id)

            stats_list = []
            evo_dict = {}
            counter = 0
            
            for stat in stats_data:
                stats_list.append(stat.stat)
            
            for evo in evolutions_data:
                evo_dict.update( {evo.evolution_secuence:evo.evolution} )

            return JsonResponse({
                    'name': pokemon_name,
                    'height':data.height,
                    "weight":data.weight,
                    "id":data.id,
                    "base_stats":stats_list,
                    "evolutions":evo_dict,
                })
        except:
            return JsonResponse({
                    'error':'Pokemon not found in our database.',
                })
