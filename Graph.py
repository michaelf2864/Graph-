import matplotlib.pyplot as p
import networkx as nw

list = ['Билл Гейтс, компания: Microsoft, увлечения: чтение, бридж, пиклбол, благотворительность', 'Джефф Безос, компания: Amazon, Blue Origin, увлечения: чтение, сон']
graph = nw.Graph()
names = []
companies = []
hobbies = []
edges = []

for i in range(len(list)):
    names.append(list[i][:list[i].index(",")])
for i in range(len(list)):
    words = list[i][list[i].index("компания"):list[i].index(", увлечения")]
    print(words)
    words1 = [company.strip() for company in words.split(": ")[1].split(",")]
    companies += words1
    for n in range(len(words1)):
        edges.append((list[i][:list[i].index(",")], words1[n]))
for i in range(len(list)):
    words = list[i][list[i].index("увлечения"):]
    words1 = [hobby.strip() for hobby in words.split(": ")[1].split(",")]
    hobbies += words1
    for n in range(len(words1)):
        edges.append((list[i][:list[i].index(",")], words1[n]))

graph.add_nodes_from(names)
graph.add_nodes_from(companies)
graph.add_nodes_from(hobbies)
graph.add_edges_from(edges)

colors = []
for node in graph.nodes():
    if node in names:
        colors.append("red")
    if node in companies:
        colors.append("blue")
    if node in hobbies:
        colors.append("green")

pos = nw.spring_layout(graph)
nw.draw(graph, node_color=colors, with_labels=True, font_weight="bold")
p.show()