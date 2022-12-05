from prettytable import PrettyTable

table=PrettyTable()

table.add_column("Pokrmon_name",["Pikachu","Squirtle"])
table.add_column("type",["Electric","Water"])

print(table)