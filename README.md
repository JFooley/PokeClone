# Dao's Guide
Este é um projeto usando pygame de um jogo no estilo de Pokemon de um universo fantasioso de minha autoria.

# Sinopse
Neste universo, as pessoas convivem Daos: espíritos de diferentes formas, elementos e que coexistem de forma não hostil com os seres vivos em todo o mundo.
Todas as pessoas são capazes de ver e interagir com os Daos, porém, algumas delas nascem com uma alta sensibilidade a eles e são capazes de guiar esses espíritos para que eles o obedeçam. Essas pessoas são chamadas de Guias Dao.
Os guias são capazes de aprisionar esses espíritos em esferas (semelhantes a bolinhas de gude) que carregam consigo em colares e podem canalizar sua energia nelas para invocar os Dao capturado. Guiar um Dao não é uma tarefa fácil, quanto mais experiente o guia é, mais Daos ele consegue carregar consigo sem que eles escapem.
Ser guia é como uma profissão, os guias competem entre si em torneios e batalhas que testam sua força de vontade e seus espíritos e os ajudam a evoluir ainda mais!

# Progresso:
- Ainda está bem no início, porém as funções para geracao os Daos, movimentos, chart de efetividade, batalhar, calculo de dano e etc. estão parcialmente prontas, então é possível utilizar elas no terminal para simular batalhas.
- Algumas funções de geração aleatória de movimentos, Daos e Guias adversários estão prontas e/ou em desenvolvimento.
- A cena de batalha está quase toda completa na questão de visual, UI reativa e etc. A integração com objeto da Batalha permite que a cena faça um tracking das informações envolvidas e exiba com a UI que se altera a depender do estado da batalha. Os botões possuem integração pra feedback visual do input realizado e se alteram visualmente a depender de qual tipo de informação está sendo exibida (Texto simples, Move ou Dao), mostrando a tipagem do movimento ou do Dao exibido.
- A cena de batalha está com a base do comportamento implementado, sendo assim já é possível navegar entre a telas e cada uma delas tem seu comportamento básico funcional. Apenas a lógica da batalha em si que ainda não está integrada.
- O sistema de exibição das animações dos Daos está implementado, mudando de acordo com o estado do Dao em batalha. Entretanto, como não há animações ainda, os dão não serão exibidos.

# Features e observações:
- Os Daos e movimentos são criados com base em tabelas CSV, compatíveis com o esquema dos movimentos e status dos pokemons. Ou seja, é possível criar Daos a partir dos status base de pokemons. 
- O esquema de input está modularizado e foi feito de forma genérica para que pode ser mapeado para diferentes teclas ou até outros dispositivos.
- Um behaviour base de teste está implementado para que a batalha possa ser iniciada com atores e etc., e testar o funcionamento da UI e demais componentes.