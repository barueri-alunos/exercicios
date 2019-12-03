#imprima a venda da Vivian e o time do Rodrigo

equipes = [
{
   "nome": "Alexandre",
   "vendas": 300,
   "time": [
       {
           "nome": "Vivian",
           "vendas": 100,
        },
       {
           "nome": "Flávio",
           "vendas": 350,
       }
   ]
},
{
       "nome": "Rodrigo",
       "vendas": 450,
       "time":
           {
               "nome": "Rafael",
               "vendas": 200,
           }
   }
]

valor_vivian = (equipes[0]['time'][0]['vendas'])
print(valor_vivian)

time_rodrigo = (equipes[1]['time'])
print(time_rodrigo)